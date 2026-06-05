"""Locale pack helper.

Loads the official platform locale packs (`Glosarios/<lang>.json`) and
provides text → translation lookup with a destination → EN → ES fallback chain.

Locale packs share semantic keys (e.g. `assignmentManagement.assignments.type.DayOff`)
across languages, so we can:
  1. Build a reverse index for the SOURCE language: `value (normalized) → key`
  2. Resolve the same key in the TARGET pack to get the translation.
  3. If missing, fall back to EN, then ES.

This module is consumed by `goalbus_localize.py`.
"""

from __future__ import annotations

import json
import re
import unicodedata
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Iterable

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
LOCALE_DIR = REPO_ROOT / "Glosarios"

LANG_TO_FILE = {
    "es": "es.json",
    "en": "en.json",
    "de": "de.json",
    "fr": "fr.json",
    "it": "it.json",
    "pt_br": "pt_br.json",
}

DEFAULT_FALLBACK_CHAIN = ("en", "es")

_PLACEHOLDER_RE = re.compile(r"\{\{?\s*([a-zA-Z0-9_.]+)\s*\}?\}")


@dataclass(frozen=True)
class LookupResult:
    """Outcome of a translation lookup."""

    text: str
    key: str | None  # semantic key from the locale pack, if found
    source: str  # 'pack:<lang>' | 'fallback:<lang>' | 'orphan'

    @property
    def is_orphan(self) -> bool:
        return self.source == "orphan"


def normalize_lang(lang: str) -> str:
    """Normalize a language code to the form used in LANG_TO_FILE."""
    return lang.strip().lower().replace("-", "_")


def _normalize_text(text: str) -> str:
    """Normalize text for reverse lookup: trim, lowercase, collapse whitespace,
    fold accents."""
    if text is None:
        return ""
    s = unicodedata.normalize("NFKC", text).strip().lower()
    s = re.sub(r"\s+", " ", s)
    return s


def normalize_placeholders(text: str) -> str:
    """Normalize all `{var}` and `{{var}}` placeholders to `{{var}}` form.

    The locale packs are inconsistent (en.json uses `{{name}}`, de.json uses
    `{name}`); we always emit the double-brace form so the rendered HTML is
    stable.
    """
    if not text:
        return text
    return _PLACEHOLDER_RE.sub(lambda m: "{{" + m.group(1) + "}}", text)


@lru_cache(maxsize=None)
def load_pack(lang: str) -> dict[str, str]:
    """Load a locale pack. Returns {} if the file is missing or unparseable.

    Cached: each pack is loaded at most once per process.
    """
    lang = normalize_lang(lang)
    fname = LANG_TO_FILE.get(lang)
    if not fname:
        return {}
    path = LOCALE_DIR / fname
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    if not isinstance(data, dict):
        return {}
    # keep only string values
    return {k: v for k, v in data.items() if isinstance(v, str)}


@lru_cache(maxsize=None)
def build_reverse_index(src_lang: str) -> dict[str, str]:
    """Build `{normalized_value → key}` for the source-language pack.

    When the same value maps to multiple keys (common for short generic words
    like "Yes"), the first key wins. This is acceptable because the lookup
    only cares about getting *some* valid key — translations of a given source
    string are typically identical across keys in the same language.
    """
    pack = load_pack(src_lang)
    index: dict[str, str] = {}
    for key, value in pack.items():
        norm = _normalize_text(value)
        if not norm:
            continue
        index.setdefault(norm, key)
    return index


def lookup_by_text(
    source_text: str,
    src_lang: str,
    target_lang: str,
    fallback_chain: Iterable[str] = DEFAULT_FALLBACK_CHAIN,
) -> LookupResult:
    """Translate `source_text` from `src_lang` to `target_lang` via the locale pack.

    Resolution order:
      1. Reverse-index the source pack to find a semantic key
      2. Look up that key in the target pack
      3. Fall through fallback_chain (e.g. EN, then ES)
      4. Return orphan if nothing matches
    """
    src_lang = normalize_lang(src_lang)
    target_lang = normalize_lang(target_lang)

    index = build_reverse_index(src_lang)
    key = index.get(_normalize_text(source_text))
    if key is None:
        return LookupResult(text=source_text, key=None, source="orphan")

    return lookup_by_key(key, target_lang, fallback_chain, original=source_text)


def lookup_by_key(
    key: str,
    target_lang: str,
    fallback_chain: Iterable[str] = DEFAULT_FALLBACK_CHAIN,
    original: str | None = None,
) -> LookupResult:
    """Resolve a known semantic `key` in the target locale, with fallbacks.

    `original` is the source-language string; returned as last resort if the
    key has no value in any fallback pack (shouldn't happen if the index was
    built from a populated pack, but kept for safety).
    """
    target_lang = normalize_lang(target_lang)
    target_pack = load_pack(target_lang)
    val = target_pack.get(key)
    if isinstance(val, str) and val.strip():
        return LookupResult(text=normalize_placeholders(val), key=key, source=f"pack:{target_lang}")

    for fb in fallback_chain:
        fb = normalize_lang(fb)
        if fb == target_lang:
            continue
        fb_pack = load_pack(fb)
        fb_val = fb_pack.get(key)
        if isinstance(fb_val, str) and fb_val.strip():
            return LookupResult(text=normalize_placeholders(fb_val), key=key, source=f"fallback:{fb}")

    return LookupResult(text=original if original is not None else "", key=key, source="orphan")


def pack_health(lang: str) -> dict[str, int]:
    """Diagnostic: report basic health of a locale pack."""
    pack = load_pack(lang)
    inconsistent_placeholders = 0
    for v in pack.values():
        # mixed `{x}` and `{{x}}` in the same string is a smell
        if re.search(r"(?<!\{)\{[a-zA-Z0-9_.]+\}(?!\})", v) and "{{" in v:
            inconsistent_placeholders += 1
    return {
        "entries": len(pack),
        "inconsistent_placeholders": inconsistent_placeholders,
    }
