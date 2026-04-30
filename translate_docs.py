#!/usr/bin/env python3
"""
translate_docs.py
Translates Markdown documentation files from one language to another
using Helsinki-NLP/opus-mt models (fully offline, CPU-friendly).

Usage:
    pip install -r requirements_translation.txt
    python translate_docs.py                      # translate all 26 files
    python translate_docs.py --force              # re-translate even if output exists
    python translate_docs.py --file P1_Entendiendo_el_rol_del_planificador_y_el_flujo_end_to_end.md
"""

import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path

import torch
import yaml
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

# ═════════════════════════════════════════════════════════════════════════════
# TRANSLATION PROFILES — uncomment ONE block, leave the rest commented
# Speed guide:  ★★★ fast (~33 min / 26 files)   ★☆☆ slow (~6 h / 26 files)
# ═════════════════════════════════════════════════════════════════════════════

# ── Directory roots (used by all profiles) ────────────────────────────────────
BASE_DIR = Path(__file__).parent
_ES  = BASE_DIR / "Maestros Finales" / "Archivos Maestros (ES)"
_EN  = BASE_DIR / "Maestros Finales" / "Master Files (EN)"
_PT  = BASE_DIR / "Maestros Finales" / "Arquivos Mestres (PT_BR)"
_FR  = BASE_DIR / "Maestros Finales" / "Fichiers Maîtres (FR)"
_IT  = BASE_DIR / "Maestros Finales" / "Archivi Maestri (IT)"
_DE  = BASE_DIR / "Maestros Finales" / "Master Files (DE)"

# ── Profile A: ES → EN  ★★★  (opus-mt direct, ~33 min) ──────────────────────
# MODEL_NAME = "Helsinki-NLP/opus-mt-es-en"
# TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
# SRC_DIR = _ES;  TGT_DIR = _EN

# ── Profile B: ES → FR  ★★★  (opus-mt direct, ~33 min) ──────────────────────
# MODEL_NAME = "Helsinki-NLP/opus-mt-es-fr"
# TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
# SRC_DIR = _ES;  TGT_DIR = _FR

# ── Profile C: EN → PT_BR  ★★★  (opus-mt via EN pivot, ~33 min) ─────────────
# Requires EN files already generated (Profile A).
# opus-mt-en-ROMANCE translates English to PT, IT, FR, etc. with a language tag.
# MODEL_NAME = "Helsinki-NLP/opus-mt-en-ROMANCE"
# TGT_LANG_TAG = ">>pt<<";  NLLB_SRC = "";  NLLB_TGT = ""
# SRC_DIR = _EN;  TGT_DIR = _PT

# ── Profile D: EN → IT  ★★★  (opus-mt via EN pivot, ~33 min) ────────────────
# MODEL_NAME = "Helsinki-NLP/opus-mt-en-ROMANCE"
# TGT_LANG_TAG = ">>it<<";  NLLB_SRC = "";  NLLB_TGT = ""
# SRC_DIR = _EN;  TGT_DIR = _IT

# ── Profile E: EN → DE  ★★★  (opus-mt direct, ~33 min) ──────────────────────
# MODEL_NAME = "Helsinki-NLP/opus-mt-en-de"
# TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
# SRC_DIR = _EN;  TGT_DIR = _DE

# ── Profile F: any pair  ★☆☆  (NLLB-200, ~6 h on CPU — last resort) ─────────
# NLLB codes: spa_Latn ES · por_Latn PT · fra_Latn FR · ita_Latn IT · ...
# MODEL_NAME = "facebook/nllb-200-distilled-600M"
# TGT_LANG_TAG = "";  NLLB_SRC = "spa_Latn";  NLLB_TGT = "por_Latn"
# SRC_DIR = _ES;  TGT_DIR = _PT

# ── Profile A: ES → EN  ★★★  (ACTIVE) ───────────────────────────────────────
MODEL_NAME = "Helsinki-NLP/opus-mt-es-en"
TGT_LANG_TAG = "";  NLLB_SRC = "";  NLLB_TGT = ""
SRC_DIR = _ES;  TGT_DIR = _EN

# ── Active target language (used to label logs) ───────────────────────────────
TGT_LANG = "en"

# ── Output artifacts ─────────────────────────────────────────────────────────
FILENAME_MAP_PATH = TGT_DIR / "filename_map.json"
LOG_PATH = TGT_DIR / "translation.log"

# ── Translation limits ────────────────────────────────────────────────────────
MAX_TOKENS = 400  # conservative limit; opus-mt supports ~512

# ── Domain-specific terms to keep verbatim (not translated) ──────────────────
# Add GoalBus product/module names that must not be changed by the model.
PRESERVE_TERMS = [
    # Product/brand names — never translated
    "GoalBus", "GTFS",
    # Direction labels used as UI names
    "Sentido 1", "Sentido 2",
    # NOTE: "Scheduling" and "Rostering" are intentionally NOT here.
    # They are handled by GLOSSARY: Scheduling -> Programação, Rostering -> Alocação.
]

# ── Glossary (per-profile) ────────────────────────────────────────────────────
# Point to a .md file with tables mapping source-language terms to target-language.
# Column headers are matched by substring (case-insensitive).
# Set GLOSSARY_PATH = None to disable glossary substitution.
GLOSSARY_PATH = None   # Profile A (ES -> EN): no glossary needed
GLOSSARY_SRC_COL = "EN"      # header text of source-language column
GLOSSARY_TGT_COL = "PT-BR"  # header text of target-language column

# Populated at runtime by load_glossary(); do not edit here.
GLOSSARY: dict = {}

# ── Compiled regex patterns ───────────────────────────────────────────────────
_FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)", re.DOTALL)
_HEADING_RE = re.compile(r"^(#{1,6}\s+)(.*)")
_LIST_ITEM_RE = re.compile(r"^(\s*(?:[-*]|\d+\.)\s+)(.*)")
_BLOCKQUOTE_RE = re.compile(r"^(\s*>\s+)(.*)")
_IMAGE_REF_RE = re.compile(r"^ref:\s+")
_MDLINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]*)\)")
_BOLD_RE = re.compile(r"\*\*(.*?)\*\*")
_P_PREFIX_RE = re.compile(r"^(P\d+)_")
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+")


# ─────────────────────────────────────────────────────────────────────────────
# Logging setup
# ─────────────────────────────────────────────────────────────────────────────

def setup_logging():
    TGT_DIR.mkdir(parents=True, exist_ok=True)
    # Force UTF-8 on the console so special characters (arrows, accents) don't crash
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass
    fmt = "%(asctime)s [%(levelname)s] %(message)s"
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler(LOG_PATH, encoding="utf-8"),
        ],
    )


log = logging.getLogger(__name__)


# ─────────────────────────────────────────────────────────────────────────────
# Glossary loader
# ─────────────────────────────────────────────────────────────────────────────

def load_glossary(path, src_col_hint: str, tgt_col_hint: str) -> dict:
    """
    Parse a markdown glossary file and return {src_term: tgt_term}.
    Tables are detected by header rows containing the column hint substrings.
    Also registers naive English plural forms (term+'s' -> tgt+'s') so that
    e.g. 'Drivers' is caught when the glossary only lists 'Driver'.
    """
    if path is None or not Path(path).exists():
        log.info("[GLOSSARY] No glossary configured or file not found — skipping")
        return {}

    result = {}
    src_hint = src_col_hint.upper()
    tgt_hint = tgt_col_hint.upper()
    src_idx = tgt_idx = None

    for raw_line in Path(path).read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line.startswith("|"):
            src_idx = tgt_idx = None
            continue

        cells = [c.strip() for c in line.split("|")[1:-1]]
        if not cells:
            continue

        upper = [c.upper() for c in cells]

        # Detect header row — only when we haven't found one yet for this table.
        # (Prevents data cells like "ESCALONAMIENTO" — which contains "EN" —
        # or notes cells that mention "PT-BR" from being mistaken for headers.)
        if src_idx is None:
            has_src = any(src_hint in c for c in upper)
            has_tgt = any(tgt_hint in c for c in upper)
            if has_src and has_tgt:
                src_idx = next(i for i, c in enumerate(upper) if src_hint in c)
                tgt_idx = next(i for i, c in enumerate(upper) if tgt_hint in c)
                continue

        # Skip separator rows (---|---|...)
        if all(re.match(r"^-+$", c.replace(" ", "")) for c in cells if c):
            continue

        if src_idx is None or tgt_idx is None:
            continue
        if len(cells) <= max(src_idx, tgt_idx):
            continue

        src_raw = cells[src_idx]
        tgt_raw = cells[tgt_idx]

        # Skip backtick terms (handled as PRESERVE_TERMS) and empty cells
        if not src_raw or not tgt_raw or src_raw.startswith("`"):
            continue
        # Skip terms identical in both languages (no substitution needed)
        if src_raw.lower() == tgt_raw.lower():
            continue

        # Handle "Term A / Term B" alternatives in source column
        src_parts = [p.strip() for p in src_raw.split("/")]
        # For target, take the first alternative only
        tgt_term = tgt_raw.split("/")[0].strip()

        for src_term in src_parts:
            if len(src_term) >= 3:
                result[src_term] = tgt_term

    # Register naive English plurals (Driver->Motorista implies Drivers->Motoristas)
    extras = {}
    for src, tgt in list(result.items()):
        # Only for single-word non-plural source terms
        if " " not in src and not src.endswith("s"):
            pl_src = src + "s"
            pl_tgt = tgt + "s" if not tgt.endswith("s") else tgt
            if pl_src not in result:
                extras[pl_src] = pl_tgt
    result.update(extras)

    log.info(f"[GLOSSARY] {len(result)} term pairs loaded from {Path(path).name}")
    return result


# ─────────────────────────────────────────────────────────────────────────────
# Frontmatter helpers
# ─────────────────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str):
    """
    Split YAML frontmatter from markdown body.
    Returns (yaml_dict, body_str) or (None, content) if no frontmatter.
    """
    m = _FRONTMATTER_RE.match(content)
    if not m:
        return None, content
    try:
        fm = yaml.safe_load(m.group(1))
    except yaml.YAMLError as exc:
        log.error(f"YAML parse error: {exc}")
        return None, content
    return fm, m.group(2)


def render_frontmatter(fm: dict) -> str:
    """Serialize a frontmatter dict back to a YAML block."""
    rendered = yaml.dump(
        fm,
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
    ).rstrip("\n")
    return f"---\n{rendered}\n---\n"


# ─────────────────────────────────────────────────────────────────────────────
# Filename helpers
# ─────────────────────────────────────────────────────────────────────────────

def title_to_filename(title_en: str, p_prefix: str) -> str:
    """Convert an English title + P-prefix into a safe filename slug."""
    clean = re.sub(r"[^\w\s\-]", "", title_en).strip()
    titled = clean.title()
    slug = re.sub(r"[\s\-]+", "_", titled)
    slug = re.sub(r"_+", "_", slug).strip("_")
    return f"{p_prefix}_{slug}.md"


def resolve_filename(es_target: str, filename_map: dict) -> str:
    """
    Map an ES .md filename to its EN equivalent.
    Tries exact match first, then falls back to P-number prefix match
    (handles the corpus inconsistency where link targets differ from actual filenames).
    """
    if es_target in filename_map:
        return filename_map[es_target]

    m = _P_PREFIX_RE.match(es_target)
    if m:
        p_num = m.group(1)
        for key, val in filename_map.items():
            if key.startswith(p_num + "_"):
                log.warning(f"[LINK] Fuzzy resolved '{es_target}' -> '{val}'")
                return val

    log.warning(f"[LINK] Unresolved link target '{es_target}' - keeping original")
    return es_target


# ─────────────────────────────────────────────────────────────────────────────
# Translator class
# ─────────────────────────────────────────────────────────────────────────────

class MarkdownTranslator:
    """Wraps Helsinki-NLP/opus-mt for line-level markdown translation."""

    def __init__(self):
        self.tokenizer = None
        self.model = None
        self.is_nllb = False
        self.nllb_tgt_id = None

    def load_model(self):
        self.is_nllb = bool(NLLB_SRC and NLLB_TGT)
        size_hint = "~2.4 GB" if self.is_nllb else "~200 MB"
        log.info(f"[LOAD] Loading {MODEL_NAME} (first run downloads {size_hint}) ...")
        torch.set_num_threads(os.cpu_count() or 4)
        if self.is_nllb:
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME, src_lang=NLLB_SRC)
            self.nllb_tgt_id = self.tokenizer.convert_tokens_to_ids(NLLB_TGT)
        else:
            self.tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
        self.model.eval()
        log.info(f"[LOAD] Model ready. CPU threads: {torch.get_num_threads()}")

    # ── Core translation ──────────────────────────────────────────────────────

    def translate_text(self, text: str) -> str:
        """Translate a plain string, chunking at sentence boundaries if needed."""
        text = text.strip()
        if not text:
            return text
        chunks = self._chunk_text(text)
        parts = []
        for chunk in chunks:
            if self.is_nllb:
                inputs = self.tokenizer(
                    chunk, return_tensors="pt", truncation=True, max_length=512
                )
                with torch.no_grad():
                    outputs = self.model.generate(
                        **inputs,
                        forced_bos_token_id=self.nllb_tgt_id,
                        num_beams=4,
                        max_length=512,
                    )
            else:
                tagged = f"{TGT_LANG_TAG} {chunk}" if TGT_LANG_TAG else chunk
                inputs = self.tokenizer(
                    tagged, return_tensors="pt", truncation=True, max_length=512
                )
                with torch.no_grad():
                    outputs = self.model.generate(
                        **inputs,
                        num_beams=4,
                        max_length=512,
                    )
            parts.append(
                self.tokenizer.decode(outputs[0], skip_special_tokens=True).strip()
            )
        return " ".join(parts)

    def _chunk_text(self, text: str) -> list:
        """Split text into token-safe chunks at sentence boundaries."""
        sentences = _SENTENCE_SPLIT_RE.split(text)
        chunks, current, current_len = [], [], 0
        for sent in sentences:
            sent_ids = self.tokenizer(sent, add_special_tokens=False).input_ids
            sent_len = len(sent_ids)
            if current_len + sent_len > MAX_TOKENS and current:
                chunks.append(" ".join(current))
                current, current_len = [], 0
            current.append(sent)
            current_len += sent_len
        if current:
            chunks.append(" ".join(current))
        return chunks or [text]

    # ── Term and bold-marker protection ──────────────────────────────────────────

    def _protect_text(self, text: str):
        """
        Replace PRESERVE_TERMS, GLOSSARY terms, and **bold** spans with opaque
        placeholders before translation.
        - PRESERVE_TERMS: restored verbatim (unchanged in target language)
        - GLOSSARY terms: restored as their pre-determined target-language equivalents
        - Bold spans: inner content is translated separately and wrapped with **
        Returns (protected_text, bold_markers, term_markers, glos_markers).
        """
        bold_markers = {}
        term_markers = {}
        glos_markers = {}   # {placeholder: target_term}
        counter = [0]

        # 1. Protect PRESERVE_TERMS first (longest first to avoid partial matches)
        for term in sorted(PRESERVE_TERMS, key=len, reverse=True):
            if term in text:
                key = f"XTERMX{counter[0]}X"
                term_markers[key] = term
                text = text.replace(term, key)
                counter[0] += 1

        # 2. Protect GLOSSARY terms (case-insensitive, longest first, whole-word only)
        for src_term in sorted(GLOSSARY.keys(), key=len, reverse=True):
            # Use word-boundary match so "Roster" never fires inside "Rostering"
            pattern = r'\b' + re.escape(src_term) + r'\b'
            if re.search(pattern, text, flags=re.IGNORECASE):
                key = f"XGLOSX{counter[0]}X"
                glos_markers[key] = GLOSSARY[src_term]
                text = re.sub(pattern, key, text, flags=re.IGNORECASE)
                counter[0] += 1

        # 3. Protect bold spans (inner content stored for separate translation)
        def _replace_bold(m):
            key = f"XBOLDX{counter[0]}X"
            bold_markers[key] = m.group(1)
            counter[0] += 1
            return key

        protected = _BOLD_RE.sub(_replace_bold, text)
        return protected, bold_markers, term_markers, glos_markers

    def _restore_text(
        self,
        text: str,
        bold_markers: dict,
        term_markers: dict,
        glos_markers: dict,
    ) -> str:
        # Restore bold spans — translate inner content before restoring
        for key, inner in bold_markers.items():
            inner_translated = self.translate_text(inner) if inner.strip() else inner
            text = text.replace(key, f"**{inner_translated}**")
        # Restore preserved terms verbatim
        for key, term in term_markers.items():
            text = text.replace(key, term)
        # Restore glossary terms with the pre-determined target equivalent
        for key, tgt_term in glos_markers.items():
            text = text.replace(key, tgt_term)
        return text

    def translate_inline(self, text: str) -> str:
        """Translate text that may contain **bold** markers and preserved terms."""
        protected, bold_markers, term_markers, glos_markers = self._protect_text(text)
        translated = self.translate_text(protected)
        return self._restore_text(translated, bold_markers, term_markers, glos_markers)

    # ── Link-aware translation ─────────────────────────────────────────────────

    def _translate_with_links(self, text: str, filename_map: dict) -> str:
        """
        Translate text while handling markdown links:
        - Case A (.md target): translate link text + remap filename to EN
        - Case B (anchor target): translate link text, keep anchor
        - Case C (broken link): pass through with warning
        """
        if not _MDLINK_RE.search(text):
            return self.translate_inline(text)

        parts = []
        last_end = 0
        for m in _MDLINK_RE.finditer(text):
            before = text[last_end : m.start()]
            if before:
                parts.append(self.translate_inline(before))

            link_text = m.group(1)
            link_target = m.group(2)
            translated_text = self.translate_inline(link_text)

            if link_target.endswith(".md"):
                en_target = resolve_filename(link_target, filename_map)
                parts.append(f"[{translated_text}]({en_target})")
            elif not link_target:
                log.warning(f"[WARN] Broken link (no target): [{link_text}]")
                parts.append(f"[{link_text}]")
            else:
                parts.append(f"[{translated_text}]({link_target})")

            last_end = m.end()

        after = text[last_end:]
        if after:
            parts.append(self.translate_inline(after))

        return "".join(parts)

    # ── Line dispatcher ────────────────────────────────────────────────────────

    def translate_body_line(self, line: str, filename_map: dict) -> str:
        """Route a single markdown line to the appropriate translation handler."""
        # Rule 1: image refs — must not be translated
        if _IMAGE_REF_RE.match(line):
            return line

        # Rule 2: blank lines
        if not line.strip():
            return line

        # Rule 3: ATX headings (## Title)
        m = _HEADING_RE.match(line)
        if m:
            return m.group(1) + self.translate_inline(m.group(2))

        # Rule 4: list items (preserve indentation + marker)
        m = _LIST_ITEM_RE.match(line)
        if m:
            return m.group(1) + self._translate_with_links(m.group(2), filename_map)

        # Rule 5: blockquotes
        m = _BLOCKQUOTE_RE.match(line)
        if m:
            return m.group(1) + self.translate_inline(m.group(2))

        # Rule 6: all other non-empty lines
        return self._translate_with_links(line, filename_map)

    # ── Body and frontmatter ───────────────────────────────────────────────────

    def translate_markdown_body(self, body: str, filename_map: dict) -> str:
        """Translate every line of a markdown body."""
        return "\n".join(
            self.translate_body_line(line, filename_map)
            for line in body.split("\n")
        )

    def translate_frontmatter(self, fm: dict) -> dict:
        """Translate title, shortTitle, and intro fields; leave the rest intact."""
        result = dict(fm)
        for field in ("title", "shortTitle", "intro"):
            if field in result and result[field]:
                result[field] = self.translate_inline(str(result[field]))
        return result


# ─────────────────────────────────────────────────────────────────────────────
# Pass 1 — build filename map
# ─────────────────────────────────────────────────────────────────────────────

def build_filename_map(src_files: list, translator: MarkdownTranslator) -> dict:
    """
    Translate only each file's title: field to derive the EN filename.
    Returns {es_filename: en_filename}.
    """
    log.info(f"[PASS1] Building filename map from {len(src_files)} source files ...")
    filename_map = {}

    for src_path in sorted(src_files):
        es_filename = src_path.name
        m = _P_PREFIX_RE.match(es_filename)
        if not m:
            log.warning(f"[PASS1] Cannot extract P-prefix from '{es_filename}' - skipping")
            continue
        p_prefix = m.group(1)

        content = src_path.read_text(encoding="utf-8")
        fm, _ = parse_frontmatter(content)

        if fm and "title" in fm:
            title_en = translator.translate_inline(str(fm["title"]))
            en_filename = title_to_filename(title_en, p_prefix)
        else:
            log.warning(f"[PASS1] No title in '{es_filename}' - using fallback")
            en_filename = f"{p_prefix}_translated.md"

        filename_map[es_filename] = en_filename
        log.info(f"[MAP] {es_filename}  ->  {en_filename}")

    return filename_map


# ─────────────────────────────────────────────────────────────────────────────
# Pass 2 — full file translation
# ─────────────────────────────────────────────────────────────────────────────

def translate_file(
    src_path: Path,
    tgt_dir: Path,
    filename_map: dict,
    translator: MarkdownTranslator,
    force: bool = False,
):
    """Translate one .md file and write the result to tgt_dir."""
    es_filename = src_path.name
    en_filename = filename_map.get(es_filename)
    if not en_filename:
        log.error(f"[ERROR] No EN filename mapping for '{es_filename}' - skipping")
        return

    tgt_path = tgt_dir / en_filename

    if tgt_path.exists() and not force:
        log.info(f"[SKIP] {en_filename} already exists (--force to re-translate)")
        return

    content = src_path.read_text(encoding="utf-8")
    fm, body = parse_frontmatter(content)

    if fm is None:
        log.warning(f"[WARN] No frontmatter in '{es_filename}' - translating as plain body")
        output = translator.translate_markdown_body(content, filename_map)
    else:
        fm_en = translator.translate_frontmatter(fm)
        body_en = translator.translate_markdown_body(body, filename_map)
        output = render_frontmatter(fm_en) + body_en

    tgt_path.write_text(output, encoding="utf-8")
    log.info(f"[WRITTEN] {tgt_path.name}")


# ─────────────────────────────────────────────────────────────────────────────
# Entry point
# ─────────────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Translate markdown docs with Helsinki-NLP/opus-mt (offline, CPU)"
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-translate files that already exist in the target directory",
    )
    parser.add_argument(
        "--file",
        metavar="FILENAME",
        default=None,
        help="Translate a single file by its ES filename (useful for testing)",
    )
    args = parser.parse_args()

    setup_logging()
    TGT_DIR.mkdir(parents=True, exist_ok=True)

    # Load glossary into global GLOSSARY dict (must happen after setup_logging)
    global GLOSSARY
    GLOSSARY = load_glossary(GLOSSARY_PATH, GLOSSARY_SRC_COL, GLOSSARY_TGT_COL)

    src_files = [
        p for p in SRC_DIR.iterdir() if p.is_file() and p.suffix == ".md"
        if not p.name.startswith("glossary") and not p.name.startswith("translation")
    ]
    if not src_files:
        log.error(f"No .md files found in: {SRC_DIR}")
        sys.exit(1)

    log.info(f"Found {len(src_files)} source files in {SRC_DIR}")

    translator = MarkdownTranslator()
    translator.load_model()

    # Pass 1: build and save the filename map
    filename_map = build_filename_map(src_files, translator)
    FILENAME_MAP_PATH.write_text(
        json.dumps(filename_map, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    log.info(f"[MAP] Saved to {FILENAME_MAP_PATH}")

    # Pass 2: translate files
    if args.file:
        target = SRC_DIR / args.file
        if not target.exists():
            log.error(f"File not found: {target}")
            sys.exit(1)
        translate_file(target, TGT_DIR, filename_map, translator, force=args.force)
    else:
        sorted_files = sorted(src_files)
        for i, src_path in enumerate(sorted_files, 1):
            log.info(f"[PASS2] ({i}/{len(sorted_files)}) {src_path.name}")
            translate_file(src_path, TGT_DIR, filename_map, translator, force=args.force)

    log.info("[COMPLETE] Translation finished.")


if __name__ == "__main__":
    main()
