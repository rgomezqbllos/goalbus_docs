#!/usr/bin/env python3
"""
GoalBus DOM Localization Pipeline v2.0
======================================
Parametric, multi-language HTML localization for GoalBus screenshots.

Key improvements over v1:
  - Any source → any target language (not hardcoded ES→PT_BR)
  - Clean JSON storage (no >...< wrappers in data, match strategy in _match field)
  - Structured 'translate' command for AI-assisted workflow
  - Consistent build logic for all entry types
"""

import os
import sys
import shutil
import csv
import json
import re
from collections import defaultdict

# Evita UnicodeEncodeError en consolas Windows con codificación heredada.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CSV_FILE = "translation_data.csv"
GLOBAL_JSON = "global_translations.json"

# Maps folder names → ISO language codes.  Add new languages here.
FOLDER_TO_LANG = {
    "Español":      "ES",
    "Espan\u0303ol": "ES",   # macOS NFD normalization
    "Portugues":    "PT_BR",
    "English":      "EN",
    "Frances":      "FR",
    "Italiano":     "IT",
    "Deutsch":      "DE",
}

# Reverse map: lang code → canonical folder name
LANG_TO_FOLDER = {
    "ES":    "Español",
    "PT_BR": "Portugues",
    "EN":    "English",
    "FR":    "Frances",
    "IT":    "Italiano",
    "DE":    "Deutsch",
}

# The ordered list of language columns in the CSV
CSV_LANGS = ["ES", "PT_BR", "EN", "FR"]

# Form field component types and their injection strategy
TAG_TO_TYPE = {
    'input':               'input_value',
    'textarea':            'input_value',
    'gs-input':            'input_value',
    'gs-text-area':        'input_value',
    'gs-number-input':     'input_value',
    'gs-color-picker':     'input_value',
    'gs-select':           'field_value',
    'gs-autocomplete':     'field_value',
    'gs-multi-select':     'field_value',
    'select':              'field_value',
    'gs-checkbox':         'checkbox_checked',
    'gs-date-picker':      'date_picker',
    'gs-date-picker-range':'date_picker',
    'gs-timepicker':       'input_value',
}

# CSS class patterns for inputs that lack data-qa-id
CLASS_INPUT_PATTERNS = [
    ("gs-text-ellipsis", "stop"),
]


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_folder_name(path):
    return os.path.basename(os.path.normpath(path))


def detect_language_from_path(path):
    """Detect language code and folder name from any part of the path."""
    for dir_name, lang_code in FOLDER_TO_LANG.items():
        if dir_name in path:
            return lang_code, dir_name
    return None, None


def find_html_file(folder_path):
    """Return the first GoalBus HTML file in folder_path, or None."""
    if not os.path.isdir(folder_path):
        return None
    for name in ["GoalBus.html", "GoalBus Settings.html", "GoalBus_Settings.html"]:
        candidate = os.path.join(folder_path, name)
        if os.path.exists(candidate):
            return candidate
    for f in sorted(os.listdir(folder_path)):
        if f.endswith(".html") and os.path.isfile(os.path.join(folder_path, f)):
            return os.path.join(folder_path, f)
    return None


def load_global_dict():
    if not os.path.exists(GLOBAL_JSON):
        return {}
    with open(GLOBAL_JSON, "r", encoding="utf-8") as f:
        return json.load(f)


def save_global_dict(d):
    with open(GLOBAL_JSON, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)


def _is_asset_folder(path):
    """Return True if this is a browser-saved assets folder, not a translatable page."""
    name = os.path.basename(path)
    return name.endswith("_files") or name in ("js", "js(1)", "fonts", "assets")


def resolve_folders(folder_path):
    """Given a path, return all PAGE subfolders that contain a main HTML file.
    Skips _files/ asset directories. If the path itself is a page, returns [path]."""
    if _is_asset_folder(folder_path):
        return []
    if find_html_file(folder_path):
        # Verify it's a real page folder (contains GoalBus*.html at root level)
        for f in os.listdir(folder_path):
            if f.endswith(".html") and not f.startswith("login"):
                return [folder_path]
        return []
    results = []
    for root, dirs, files in os.walk(folder_path):
        # Prune asset folders so os.walk doesn't descend into them
        dirs[:] = [d for d in dirs if not _is_asset_folder(d)]
        if _is_asset_folder(root):
            continue
        if any(f.endswith(".html") and not f.startswith("login") for f in files):
            results.append(root)
    return sorted(results)


def derive_source_path(target_path, source_lang_code):
    """Given a target path like 'Portugues/P4/P4_imagen1', derive the source path."""
    source_folder = LANG_TO_FOLDER.get(source_lang_code)
    if not source_folder:
        return None
    # Replace the language folder segment
    for folder_name in FOLDER_TO_LANG:
        if folder_name in target_path:
            return target_path.replace(folder_name, source_folder)
    return None


def is_noise(text):
    """Return True if text is not useful UI copy."""
    t = text.strip()
    if not t or len(t) < 3:
        return True
    if '{' in t or '}' in t or '@' in t:
        return True
    if t.startswith('http') or t.startswith('//') or t.startswith('./') or t.startswith('../'):
        return True
    if '&' in t:
        return True
    if re.match(r'^[\d\s\.,\-\+\%\/\:\(\)\[\]]+$', t):
        return True
    if '\\n' in t or '\\t' in t or '\\"' in t:
        return True
    if len(t) > 150:
        return True
    return False


def get_canonical_set(global_dict):
    """Build a set of all known source texts (case-insensitive) for dedup."""
    canonical = set()
    for entry in global_dict.values():
        for lang_code in FOLDER_TO_LANG.values():
            val = entry.get(lang_code, "")
            if val and val != "PENDING":
                canonical.add(val)
                canonical.add(val.lower())
    return canonical


# ---------------------------------------------------------------------------
# Command: init
# ---------------------------------------------------------------------------

def init_folder(source_path, target_lang="PT_BR", auto_extract=True):
    """Scan source HTML for form fields, register in CSV, create target folder."""
    source_lang, source_dir = detect_language_from_path(source_path)
    if not source_lang:
        print(f"  Error: Cannot detect language in '{source_path}'")
        print(f"    Path must contain one of: {', '.join(FOLDER_TO_LANG.keys())}")
        return

    target_folder_name = LANG_TO_FOLDER.get(target_lang, target_lang)
    target_path = source_path.replace(source_dir, target_folder_name)
    folder_name = get_folder_name(source_path)

    print(f"  init '{folder_name}' ({source_lang} → {target_lang})")

    # Create target folder
    if not os.path.exists(target_path):
        shutil.copytree(source_path, target_path)
        print(f"    Created: {target_path}")
    else:
        print(f"    Target exists: {target_path}")

    # Scan HTML for form fields
    html_file = find_html_file(source_path)
    if not html_file:
        print(f"    Warning: No HTML file in {source_path}")
        return

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    tags_pattern = '|'.join(re.escape(t) for t in TAG_TO_TYPE.keys())

    # Find fields with data-qa-id
    qa_pattern = rf'<({tags_pattern})\b[^>]*data-qa-id="([^"]+)"'
    found_fields = re.findall(qa_pattern, content, re.IGNORECASE)

    # Fallback: formly IDs
    for tag_full in re.findall(rf'<(?:{tags_pattern})\b[^>]*>', content, re.IGNORECASE):
        if 'data-qa-id="' in tag_full.lower():
            continue
        tname_match = re.match(rf'<({tags_pattern})\b', tag_full, re.IGNORECASE)
        if not tname_match:
            continue
        tname = tname_match.group(1).lower()
        id_match = re.search(r'id="formly_\d+_[^_]+_([^_]+)_\d+"', tag_full, re.IGNORECASE)
        if id_match:
            found_fields.append((tname, id_match.group(1)))

    # Load existing CSV
    headers = ['folder', 'field_id', 'type'] + CSV_LANGS
    all_data = {}
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            if reader.fieldnames:
                headers = reader.fieldnames
            for row in reader:
                group = row['folder']
                if group not in all_data:
                    all_data[group] = []
                all_data[group].append(row)

    existing_rows = {row['field_id']: row for row in all_data.get(folder_name, [])}
    new_rows = []
    seen_ids = set()

    # Process data-qa-id and formly fields
    for tag_name, qa_id in found_fields:
        if qa_id in seen_ids:
            continue
        seen_ids.add(qa_id)
        field_type = TAG_TO_TYPE.get(tag_name.lower(), 'input_value')
        if qa_id in existing_rows:
            row = existing_rows[qa_id]
            row['type'] = field_type
            new_rows.append(row)
        else:
            row = {'folder': folder_name, 'field_id': qa_id, 'type': field_type}
            for lang in CSV_LANGS:
                row[lang] = 'false' if field_type == 'checkbox_checked' else ''
            new_rows.append(row)

    # Process CSS class-indexed fields
    for css_class, label in CLASS_INPUT_PATTERNS:
        pattern = rf'<input(?![^>]*data-qa-id)[^>]*class="[^"]*{re.escape(css_class)}[^"]*"[^>]*>'
        matches = re.findall(pattern, content, re.IGNORECASE)
        for idx, _ in enumerate(matches):
            field_id = f"class:{css_class}:{idx}"
            if field_id in seen_ids:
                continue
            seen_ids.add(field_id)
            if field_id in existing_rows:
                new_rows.append(existing_rows[field_id])
            else:
                row = {'folder': folder_name, 'field_id': field_id, 'type': 'class_indexed'}
                for lang in CSV_LANGS:
                    row[lang] = ''
                new_rows.append(row)

    all_data[folder_name] = new_rows
    final_output = []
    for group_name in sorted(all_data.keys()):
        final_output.extend(all_data[group_name])

    with open(CSV_FILE, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(final_output)

    print(f"    {len(new_rows)} form fields → {CSV_FILE}")
    for r in new_rows:
        marker = " (NEW)" if not r.get('ES', '') and not r.get('PT_BR', '') else ""
        print(f"      [{r['type']}] {r['field_id']}{marker}")

    if auto_extract:
        print("    Extracting UI vocabulary → global_translations.json")
        extract_vocabulary(source_path, dry_run=False)


# ---------------------------------------------------------------------------
# Command: extract
# ---------------------------------------------------------------------------

def extract_vocabulary(source_path, dry_run=False):
    """Scan HTML for new UI text strings, add as PENDING to JSON."""
    mode = "[DRY RUN] " if dry_run else ""
    source_lang, _ = detect_language_from_path(source_path)
    if not source_lang:
        print(f"  Error: Cannot detect language in '{source_path}'")
        return

    html_file = find_html_file(source_path)
    if not html_file:
        print(f"  Error: No HTML in {source_path}")
        return

    print(f"  {mode}extract '{get_folder_name(source_path)}' (source: {source_lang})")

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip non-visible sections
    clean = re.sub(r'<script\b.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r'<style\b.*?</style>',   '', clean,   flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r'<!--.*?-->',             '', clean,   flags=re.DOTALL)
    # Ignore hidden mirror spans used by form controls to reflect field values.
    clean = re.sub(r'<span\b[^>]*class="[^"]*\bhidden\b[^"]*"[^>]*>.*?</span>',
                   '', clean, flags=re.DOTALL | re.IGNORECASE)

    # Extract text nodes and attribute values
    tag_texts  = re.findall(r'>([^<\n]+)<', clean)
    attr_texts = re.findall(r'(?:placeholder|title|aria-label|alt)="\s*([^"]{3,}?)\s*"', clean)

    raw_candidates = set()
    for t in tag_texts:
        stripped = t.strip()
        if stripped:
            raw_candidates.add(("tag", stripped))
    for t in attr_texts:
        stripped = t.strip()
        if stripped:
            raw_candidates.add(("attr", stripped))

    global_dict = load_global_dict()
    canonical = get_canonical_set(global_dict)

    # Next available ID
    max_id = 0
    for key in global_dict.keys():
        try:
            num = int(key.split('_')[-1])
            if num > max_id:
                max_id = num
        except ValueError:
            pass

    new_entries = []
    skipped_noise = 0
    skipped_dup = 0

    for match_type, txt in sorted(raw_candidates, key=lambda x: x[1]):
        if is_noise(txt):
            skipped_noise += 1
            continue
        if txt in canonical or txt.lower() in canonical:
            skipped_dup += 1
            continue
        # Avoid adding the same text twice (tag and attr)
        if any(t == txt for _, t in new_entries):
            continue
        new_entries.append((match_type, txt))

    print(f"    Scanned: {len(raw_candidates)} candidates | "
          f"noise: {skipped_noise} | existing: {skipped_dup} | new: {len(new_entries)}")

    if not new_entries:
        print("    Nothing new to add.")
        return

    print(f"\n    New terms ({len(new_entries)}):")
    for mt, txt in new_entries:
        print(f"      [{mt}] \"{txt}\"")

    if dry_run:
        print("\n    [DRY RUN] No changes. Run without --dry-run to save.")
        return

    # Determine which attribute names are used
    attr_lookup = {}
    for t in attr_texts:
        stripped = t.strip()
        # Find the specific attribute name for this text
        for m in re.finditer(r'(placeholder|title|aria-label|alt)="\s*' + re.escape(stripped) + r'\s*"', clean):
            attr_lookup[stripped] = m.group(1)

    for match_type, txt in new_entries:
        max_id += 1
        entry = {source_lang: txt, "_match": "tag"}

        if match_type == "attr" and txt in attr_lookup:
            entry["_match"] = f"attr:{attr_lookup[txt]}"

        # Set all other languages to PENDING
        for lang_code in set(FOLDER_TO_LANG.values()):
            if lang_code != source_lang and lang_code not in entry:
                entry[lang_code] = "PENDING"

        # Determine key prefix based on source folder
        folder_name = get_folder_name(source_path)
        # Use a prefix like ui_p4_ for entries from P4 pages
        page_match = re.match(r'P(\d+)', folder_name)
        if page_match:
            key = f"ui_p{page_match.group(1)}_{max_id}"
        else:
            key = f"ui_text_{max_id}"

        global_dict[key] = entry

    save_global_dict(global_dict)
    print(f"\n    Saved {len(new_entries)} PENDING entries to {GLOBAL_JSON}")


# ---------------------------------------------------------------------------
# Command: translate (AI-assisted workflow)
# ---------------------------------------------------------------------------

def translate_pending(source_lang, target_lang, export_file=None):
    """
    Export PENDING translations for AI-assisted translation.

    If export_file is given, writes a simple TSV file:
      key<TAB>source_text

    The user/AI fills in the translation and imports with 'translate --import'.
    """
    global_dict = load_global_dict()

    pending = []
    for key, entry in global_dict.items():
        src_text = entry.get(source_lang, "")
        tgt_text = entry.get(target_lang, "")
        if src_text and (tgt_text == "PENDING" or not tgt_text):
            pending.append((key, src_text, entry.get("_match", "tag")))

    if not pending:
        print(f"  No PENDING translations for {source_lang} → {target_lang}.")
        return

    print(f"  {len(pending)} entries need translation: {source_lang} → {target_lang}")

    if export_file:
        with open(export_file, "w", encoding="utf-8") as f:
            f.write(f"key\t{source_lang}\t{target_lang}\n")
            for key, text, _ in pending:
                f.write(f"{key}\t{text}\t\n")
        print(f"  Exported to: {export_file}")
        print(f"  Fill the '{target_lang}' column, then run:")
        print(f"    python3 scripts/goalbus_localize.py translate --import {export_file}")
    else:
        # Print for AI consumption (copy-paste friendly)
        print(f"\n  === PENDING: {source_lang} → {target_lang} ===")
        print(f"  (Copy this list, translate, and paste back with 'translate --import')\n")
        for key, text, match_type in pending:
            print(f"  {key}\t{text}")


def import_translations(import_file, target_lang):
    """Import translations from a TSV file back into global_translations.json."""
    global_dict = load_global_dict()
    imported = 0

    with open(import_file, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter='\t')
        for row in reader:
            key = row.get('key', '').strip()
            translation = row.get(target_lang, '').strip()
            if key and translation and key in global_dict:
                global_dict[key][target_lang] = translation
                imported += 1

    save_global_dict(global_dict)
    print(f"  Imported {imported} translations for {target_lang} from {import_file}")


# ---------------------------------------------------------------------------
# Command: build
# ---------------------------------------------------------------------------

def _build_translation_map(global_dict, source_lang, target_lang):
    """
    Pre-compute translation lookup tables for fast single-pass replacement.
    Returns (tag_map, attr_map, pending_count) where:
      tag_map:  {source_text: target_text} for tag content replacements
      attr_map: {(attr_name, source_text): target_text} for attribute replacements
    """
    tag_map = {}
    attr_map = {}
    pending = 0

    for key, entry in global_dict.items():
        stext = entry.get(source_lang, "")
        ttext = entry.get(target_lang, "")
        match_type = entry.get("_match", "tag")

        if not stext or not ttext:
            continue
        if ttext == "PENDING":
            pending += 1
            continue

        if match_type.startswith("attr:"):
            attr_name = match_type.split(":", 1)[1]
            attr_map[(attr_name, stext)] = ttext
        else:
            tag_map[stext] = ttext
            # Tag text may also appear in common attributes
            for attr in ('placeholder', 'title', 'aria-label', 'alt'):
                attr_map[(attr, stext)] = ttext

    return tag_map, attr_map, pending


def _apply_translations_fast(content, tag_map, attr_map):
    """
    Apply all translations in minimal passes:
      1. Single regex pass for tag content (>text<)
      2. Single regex pass for each attribute type
    Returns (new_content, replacement_count).
    """
    replacements = 0

    # --- Pass 1: Tag content replacement using a callback ---
    if tag_map:
        # Build a pattern that matches >...< where the inner text could be any source
        # For performance: use a single compiled regex with alternation
        # Sort by length descending so longer matches take priority
        sorted_sources = sorted(tag_map.keys(), key=len, reverse=True)
        escaped = [re.escape(s) for s in sorted_sources]

        # Chunk into groups of ~50 to avoid regex size limits
        chunk_size = 50
        for i in range(0, len(escaped), chunk_size):
            chunk = escaped[i:i+chunk_size]
            chunk_sources = sorted_sources[i:i+chunk_size]
            chunk_map = {s: tag_map[s] for s in chunk_sources}

            pattern = r'>\s*(' + '|'.join(chunk) + r')\s*<'
            compiled = re.compile(pattern)

            def tag_replacer(m):
                nonlocal replacements
                src = m.group(1).strip()
                if src in chunk_map:
                    replacements += 1
                    return '>' + chunk_map[src] + '<'
                return m.group(0)

            content = compiled.sub(tag_replacer, content)

    # --- Pass 2: Attribute replacement ---
    if attr_map:
        # Group by attribute name
        by_attr = defaultdict(dict)
        for (attr_name, stext), ttext in attr_map.items():
            by_attr[attr_name][stext] = ttext

        for attr_name, amap in by_attr.items():
            sorted_sources = sorted(amap.keys(), key=len, reverse=True)
            escaped = [re.escape(s) for s in sorted_sources]

            for i in range(0, len(escaped), chunk_size):
                chunk = escaped[i:i+chunk_size]
                chunk_sources = sorted_sources[i:i+chunk_size]
                chunk_amap = {s: amap[s] for s in chunk_sources}

                pattern = r'(\b' + re.escape(attr_name) + r'="\s*)(' + '|'.join(chunk) + r')(\s*")'
                compiled = re.compile(pattern)

                def attr_replacer(m):
                    nonlocal replacements
                    src = m.group(2).strip()
                    if src in chunk_amap:
                        replacements += 1
                        return m.group(1) + chunk_amap[src] + m.group(3)
                    return m.group(0)

                content = compiled.sub(attr_replacer, content)

    return content, replacements


def build_folder(source_path, target_path, source_lang=None, target_lang=None):
    """Apply translations + inject form data from source to target."""
    if not source_lang:
        source_lang, _ = detect_language_from_path(source_path)
    if not target_lang:
        target_lang, _ = detect_language_from_path(target_path)

    folder_name = get_folder_name(target_path)

    if not source_lang or not target_lang:
        print(f"  Error: Cannot detect languages for {source_path} → {target_path}")
        return

    print(f"  build '{folder_name}' ({source_lang} → {target_lang})")

    src_html = find_html_file(source_path)
    if not src_html:
        print(f"    Error: No HTML in {source_path}")
        return

    target_html = os.path.join(target_path, os.path.basename(src_html))

    # Copy _files dependency folder if needed
    src_files_dir = src_html.replace(".html", "_files")
    target_files_dir = target_html.replace(".html", "_files")
    if os.path.exists(src_files_dir) and not os.path.exists(target_files_dir):
        os.makedirs(os.path.dirname(target_files_dir), exist_ok=True)
        shutil.copytree(src_files_dir, target_files_dir)

    with open(src_html, "r", encoding="utf-8") as f:
        content = f.read()

    # --- Step 1: Apply global UI text translations (optimized) ---
    text_replacements = 0
    pending_skipped = 0

    if source_lang != target_lang and os.path.exists(GLOBAL_JSON):
        global_dict = load_global_dict()
        tag_map, attr_map, pending_skipped = _build_translation_map(
            global_dict, source_lang, target_lang)
        content, text_replacements = _apply_translations_fast(
            content, tag_map, attr_map)

    # --- Step 2: Inject form data from CSV ---
    fields_injected = 0
    fields_skipped = 0

    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['folder'] != folder_name:
                    continue

                field_id = row['field_id']
                field_type = row['type']
                value = row.get(target_lang)
                if value is None:
                    continue

                eid = re.escape(field_id)
                selector = rf'(?:data-qa-id="{eid}"|id="formly_\d+_[^_]+_{eid}_\d+")'

                if field_type == "input_value":
                    # Update existing value or inject new one
                    val_pattern = rf'(<[a-z0-9-]+\b[^>]*?{selector}[^>]*?)\bvalue="[^"]*"'
                    new_content, count = re.subn(val_pattern, rf'\g<1>value="{value}"',
                                                 content, flags=re.DOTALL | re.IGNORECASE)
                    if count == 0:
                        inject_pattern = rf'(<[a-z0-9-]+\b[^>]*?{selector}[^>]*?)(/?>)'
                        new_content, count = re.subn(inject_pattern, rf'\g<1> value="{value}"\g<2>',
                                                     content, flags=re.DOTALL | re.IGNORECASE)
                    if count > 0:
                        fields_injected += 1
                        content = new_content
                        # Update hidden span if exists
                        span_pat = rf'({selector}[^>]*>.*?<span[^>]+class="hidden"[^>]*>).*?(</span>)'
                        content = re.sub(span_pat, rf'\g<1>{value}\g<2>',
                                         content, flags=re.DOTALL | re.IGNORECASE)
                    else:
                        fields_skipped += 1

                elif field_type == "field_value":
                    pattern = rf'({selector}[^>]*>.*?class="[^"]*field-value[^"]*"[^>]*>).*?(</span>)'
                    new_content, count = re.subn(pattern, rf'\g<1>{value}\g<2>',
                                                 content, flags=re.DOTALL | re.IGNORECASE)
                    if count > 0:
                        fields_injected += count
                        content = new_content
                    else:
                        fields_skipped += 1

                elif field_type == "checkbox_checked":
                    should_check = str(value).lower() == "true"
                    tag_pattern = rf'(<[a-z0-9-]+\b[^>]*?{selector}[^>]*?)(/?>)'

                    def checkbox_repl(m):
                        body = re.sub(r'\s+\bchecked\b', '', m.group(1), flags=re.IGNORECASE)
                        if should_check:
                            body += ' checked'
                        return body + m.group(2)

                    new_content, count = re.subn(tag_pattern, checkbox_repl,
                                                 content, flags=re.DOTALL | re.IGNORECASE)
                    if count > 0:
                        fields_injected += 1
                        content = new_content
                    else:
                        fields_skipped += 1

                elif field_type == "date_picker":
                    pattern = rf'({selector}[^>]*>.*?<span[^>]*>).*?(</span>)'
                    new_content, count = re.subn(pattern, rf'\g<1>{value}\g<2>',
                                                 content, flags=re.DOTALL | re.IGNORECASE)
                    if count > 0:
                        fields_injected += count
                        content = new_content
                    else:
                        fields_skipped += 1

                elif field_type == "class_indexed":
                    parts = field_id.split(':', 2)
                    if len(parts) == 3:
                        _, css_class, idx_str = parts
                        idx = int(idx_str)
                        cls_pat = rf'<input(?![^>]*data-qa-id)[^>]*class="[^"]*{re.escape(css_class)}[^"]*"[^>]*>'
                        matches = list(re.finditer(cls_pat, content, re.IGNORECASE | re.DOTALL))
                        if idx < len(matches):
                            m = matches[idx]
                            old_tag = m.group(0)
                            if 'value="' in old_tag.lower():
                                new_tag = re.sub(r'\bvalue="[^"]*"', f'value="{value}"',
                                                 old_tag, flags=re.IGNORECASE)
                            else:
                                new_tag = old_tag.rstrip('>') + f' value="{value}">'
                            content = content[:m.start()] + new_tag + content[m.end():]
                            fields_injected += 1
                        else:
                            fields_skipped += 1

    # --- Step 3: Static map image ---
    map_injected = False
    for check_path in [source_path, target_path]:
        map_png = os.path.join(check_path, "GoalBus_files", "mapa.png")
        if os.path.exists(map_png):
            canvas_pat = r'<canvas[^>]*class="[^"]*mapboxgl-canvas[^"]*"[^>]*>(?:</canvas>)?'
            map_img = '<img src="./GoalBus_files/mapa.png" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Map">'
            new_content = re.sub(canvas_pat, map_img, content, flags=re.IGNORECASE)
            if new_content != content:
                content = new_content
                map_injected = True
            break

    # Write output
    os.makedirs(os.path.dirname(target_html) if os.path.dirname(target_html) else ".", exist_ok=True)
    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)

    parts = [f"{text_replacements} texts", f"{fields_injected} fields"]
    if map_injected:
        parts.append("map: OK")
    if pending_skipped:
        parts.append(f"{pending_skipped} PENDING")
    if fields_skipped:
        parts.append(f"{fields_skipped} fields not matched")
    print(f"    Done: {' | '.join(parts)}")


def build_all(source_lang="ES", target_langs=None):
    """Rebuild all pages for all (or specified) target languages."""
    if target_langs is None:
        # Build all languages that have folders
        target_langs = []
        for lang_code, folder_name in LANG_TO_FOLDER.items():
            if lang_code != source_lang and os.path.exists(folder_name):
                target_langs.append(lang_code)

    source_folder = LANG_TO_FOLDER.get(source_lang)
    if not source_folder or not os.path.exists(source_folder):
        print(f"Error: Source folder '{source_folder}' not found.")
        sys.exit(1)

    print(f"=== BUILD ALL: {source_lang} → {', '.join(target_langs)} ===")
    built = 0

    for p_folder in sorted(os.listdir(source_folder)):
        p_path = os.path.join(source_folder, p_folder)
        if not os.path.isdir(p_path) or not p_folder.startswith("P"):
            continue
        for item in sorted(os.listdir(p_path)):
            source_path = os.path.join(p_path, item)
            if not os.path.isdir(source_path) or not item.startswith("P"):
                continue

            # Build source language (injects form data only)
            build_folder(source_path, source_path, source_lang, source_lang)

            # Build each target language
            for tlang in target_langs:
                target_folder = LANG_TO_FOLDER.get(tlang, tlang)
                target_path = os.path.join(target_folder, p_folder, item)
                if os.path.exists(target_path):
                    build_folder(source_path, target_path, source_lang, tlang)
                    built += 1

    print(f"=== DONE: {built} target page(s) built ===")


# ---------------------------------------------------------------------------
# Command: status
# ---------------------------------------------------------------------------

def show_status(detail_lang=None):
    """Show translation progress for all languages."""
    print("=" * 60)
    print("TRANSLATION STATUS")
    print("=" * 60)

    global_dict = load_global_dict()
    total = len(global_dict)
    all_langs = sorted(set(FOLDER_TO_LANG.values()))

    print(f"\nGlobal Dictionary ({GLOBAL_JSON}): {total} entries")

    for lang in all_langs:
        done = sum(1 for e in global_dict.values()
                   if e.get(lang) and e[lang] != "PENDING")
        pending = sum(1 for e in global_dict.values()
                      if e.get(lang) == "PENDING")
        missing = total - done - pending
        pct = int(done / max(total, 1) * 100)
        bar = "#" * int(done / max(total, 1) * 20)
        print(f"  {lang:<8} [{bar:<20}] {pct:3d}%  done:{done} pending:{pending} missing:{missing}")

    # Detail for a specific language
    if detail_lang:
        pending_items = [(k, e.get("ES", "")) for k, e in global_dict.items()
                         if e.get(detail_lang) == "PENDING" or not e.get(detail_lang)]
        if pending_items:
            print(f"\n  NEEDS WORK ({detail_lang}) — {len(pending_items)} items:")
            for key, es_val in pending_items[:20]:
                display = es_val[:55] + "..." if len(es_val) > 55 else es_val
                print(f"    {key}: \"{display}\"")
            if len(pending_items) > 20:
                print(f"    ... and {len(pending_items) - 20} more")
        else:
            print(f"\n  All {detail_lang} translations complete!")

    # CSV form data
    print(f"\nForm Data ({CSV_FILE}):")
    if not os.path.exists(CSV_FILE):
        print("  File not found")
        return

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))

    by_folder = defaultdict(list)
    for row in rows:
        by_folder[row['folder']].append(row)

    for folder_name in sorted(by_folder.keys()):
        folder_rows = by_folder[folder_name]
        total_fields = len(folder_rows)
        counts = {}
        for lang in CSV_LANGS:
            counts[lang] = sum(1 for r in folder_rows if r.get(lang, '').strip())
        status_parts = [f"{lang}:{counts[lang]}/{total_fields}" for lang in CSV_LANGS]
        print(f"  {folder_name:<20} {total_fields} fields | {' | '.join(status_parts)}")

    print("=" * 60)


# ---------------------------------------------------------------------------
# Help & CLI
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Command: pipeline
# ---------------------------------------------------------------------------

def run_pipeline(source_path, target_lang, export_file=None):
    """
    Full automation pipeline: init → extract → export pending → (AI step) → import → build_all

    Steps 1,2,3 and 5,6 are automated.
    Step 4 (translation) is handled by the caller (AI or human) between the two phases.

    Returns the export_file path so the caller can translate and re-import.
    """
    source_lang, source_dir = detect_language_from_path(source_path)
    if not source_lang:
        print(f"Error: Cannot detect language in '{source_path}'")
        sys.exit(1)

    if export_file is None:
        folder_name = get_folder_name(source_path)
        export_file = f"pending_{target_lang}_{folder_name}.tsv"

    print(f"\n{'='*60}")
    print(f"PIPELINE: {source_lang} → {target_lang}")
    print(f"Source:   {source_path}")
    print(f"{'='*60}\n")

    # --- Phase 1: INIT ---
    print("── PHASE 1/3: INIT ──────────────────────────────────────")
    folders = resolve_folders(source_path)
    if not folders:
        for root, dirs, files in os.walk(source_path):
            if any(f.endswith('.html') for f in files):
                folders.append(root)
        folders = sorted(folders)

    if not folders:
        print(f"Error: No HTML files found in '{source_path}'")
        sys.exit(1)

    for f in folders:
        init_folder(f, target_lang=target_lang, auto_extract=False)

    # --- Phase 2: EXTRACT ---
    print("\n── PHASE 2/3: EXTRACT ───────────────────────────────────")
    for f in folders:
        extract_vocabulary(f, dry_run=False)

    # --- Phase 3: EXPORT PENDING ---
    print("\n── PHASE 3/3: EXPORT PENDING ────────────────────────────")
    translate_pending(source_lang, target_lang, export_file=export_file)

    # Count how many need translation
    global_dict = load_global_dict()
    pending_count = sum(
        1 for e in global_dict.values()
        if e.get(target_lang) == "PENDING" or not e.get(target_lang)
    )

    print(f"\n{'='*60}")
    if pending_count == 0:
        print("✓ No PENDING entries — proceeding directly to build...")
        print(f"{'='*60}\n")
        build_all(source_lang=source_lang, target_langs=[target_lang])
    else:
        print(f"PAUSED -- {pending_count} entries need translation")
        print(f"   Export file: {export_file}")
        print(f"\n   Next steps:")
        print(f"   1. Fill the '{target_lang}' column in: {export_file}")
        print(f"   2. Import:  python3 scripts/goalbus_localize.py translate --import \"{export_file}\" --to {target_lang}")
        print(f"   3. Build:   python3 scripts/goalbus_localize.py build_all --from {source_lang} --to {target_lang}")
        print(f"{'='*60}\n")

    return export_file, pending_count


def print_help():
    print("""
GoalBus DOM Localization Pipeline v2.0
=======================================

COMMANDS:
  init <source_path> [--target LANG]
      Scan HTML for form fields, create target folder, update CSV.
      Default target: PT_BR

  extract <source_path> [--dry-run]
      Find new UI texts in HTML, add as PENDING to JSON.
      Source language is detected from the path.

  translate --from LANG --to LANG [--export FILE]
      Show or export PENDING translations for AI-assisted translation.

  translate --import FILE --to LANG
      Import translations from a TSV file into the JSON dictionary.

  build <target_path> [--from LANG]
      Apply translations + inject form data into target HTML.
      Source language defaults to ES.

  pipeline <source_path> --to LANG [--export FILE]
      Run the FULL pipeline automatically:
        init -> extract -> export pending -> [PAUSED] (AI translates) -> import -> build_all
      Pauses after the export step if there are PENDING entries to translate.
      If everything is already translated, runs build_all directly.

  build_all [--from LANG] [--to LANG1,LANG2,...]
      Rebuild ALL pages. Defaults: --from ES --to all existing targets.

  status [--lang LANG]
      Show translation progress. Optional: detail for a specific language.

  help
      Show this message.

TYPICAL WORKFLOW:
  1. Place HTML:    Español/Px/Px_imagenY/GoalBus.html
  2. Init:          python3 scripts/goalbus_localize.py init Español/Px
  3. Fill CSV:      Edit translation_data.csv (ES + target columns)
  4. Extract:       python3 scripts/goalbus_localize.py extract Español/Px
  5. Translate:     python3 scripts/goalbus_localize.py translate --from ES --to PT_BR --export pending_pt.tsv
                    (AI/human fills the file)
                    python3 scripts/goalbus_localize.py translate --import pending_pt.tsv --to PT_BR
  6. Build:         python3 scripts/goalbus_localize.py build_all
  7. Status:        python3 scripts/goalbus_localize.py status --lang PT_BR

SUPPORTED LANGUAGES:
""" + "\n".join(f"  {code:<8} -> folder: {folder}" for code, folder in sorted(LANG_TO_FOLDER.items())) + """

NOTES:
  - Source language is auto-detected from the folder name in the path.
  - 'build' reads from the source folder and writes to the target folder.
  - After editing JSON or CSV, always run build_all to refresh everything.
  - Add new languages by editing FOLDER_TO_LANG and LANG_TO_FOLDER at the top.
""")


def parse_arg(args, flag, default=None):
    """Extract --flag VALUE from args list."""
    for i, a in enumerate(args):
        if a == flag and i + 1 < len(args):
            return args[i + 1]
    return default


def has_flag(args, flag):
    return flag in args


if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
        sys.exit(0)

    action = sys.argv[1]
    args = sys.argv[2:]

    if action == "pipeline":
        if not args or args[0].startswith("--"):
            print("Error: 'pipeline' requires a source folder path.")
            print("  Usage: pipeline <source_path> --to LANG [--export FILE]")
            sys.exit(1)
        source_path = args[0]
        target_lang = parse_arg(args, "--to", "PT_BR")
        export_file = parse_arg(args, "--export")
        run_pipeline(source_path, target_lang, export_file=export_file)

    elif action == "status":
        lang = parse_arg(args, "--lang")
        show_status(detail_lang=lang)

    elif action == "translate":
        if has_flag(args, "--import"):
            import_file = parse_arg(args, "--import")
            target = parse_arg(args, "--to", "PT_BR")
            if not import_file:
                print("Error: --import requires a file path.")
                sys.exit(1)
            import_translations(import_file, target)
        else:
            source = parse_arg(args, "--from", "ES")
            target = parse_arg(args, "--to", "PT_BR")
            export = parse_arg(args, "--export")
            translate_pending(source, target, export_file=export)

    elif action == "build_all":
        source = parse_arg(args, "--from", "ES")
        to_arg = parse_arg(args, "--to")
        targets = to_arg.split(",") if to_arg else None
        build_all(source_lang=source, target_langs=targets)

    elif action in ("init", "extract", "build"):
        if not args or args[0].startswith("--"):
            print(f"Error: '{action}' requires a folder path.")
            print_help()
            sys.exit(1)

        folder_path = args[0]
        folders = resolve_folders(folder_path)

        if not folders:
            # For init/extract, also check the parent for subdirectories
            if action in ("init", "extract") and os.path.isdir(folder_path):
                print(f"Searching for subfolders in '{folder_path}'...")
                for root, dirs, files in os.walk(folder_path):
                    if any(f.endswith('.html') for f in files):
                        folders.append(root)
                folders = sorted(folders)

            if not folders:
                if action == "build":
                    # Check if source exists to give a helpful hint
                    source = parse_arg(args, "--from", "ES")
                    src_candidate = derive_source_path(folder_path, source)
                    if src_candidate and os.path.exists(src_candidate):
                        print(f"Error: No HTML found in '{folder_path}'")
                        print(f"  The target folder exists but has no pages yet.")
                        print(f"  Run init first:")
                        print(f"    python3 scripts/goalbus_localize.py init {src_candidate}")
                    else:
                        print(f"Error: No HTML files found in '{folder_path}'")
                else:
                    print(f"Error: No HTML files found in '{folder_path}'")
                sys.exit(1)

        if action == "init":
            target = parse_arg(args, "--target", "PT_BR")
            print(f"=== INIT ({len(folders)} folder(s), target: {target}) ===")
            for f in folders:
                init_folder(f, target_lang=target, auto_extract=True)

        elif action == "extract":
            dry_run = has_flag(args, "--dry-run")
            print(f"=== EXTRACT ({len(folders)} folder(s)) ===")
            for f in folders:
                extract_vocabulary(f, dry_run=dry_run)

        elif action == "build":
            source = parse_arg(args, "--from", "ES")
            print(f"=== BUILD ({len(folders)} folder(s), source: {source}) ===")
            for target_path in folders:
                source_path = derive_source_path(target_path, source)
                if not source_path or not os.path.exists(source_path):
                    # Maybe building the source itself
                    src_lang, _ = detect_language_from_path(target_path)
                    if src_lang == source:
                        build_folder(target_path, target_path, source, source)
                    else:
                        print(f"  Warning: Source not found for '{target_path}'")
                    continue
                build_folder(source_path, target_path, source)

    else:
        print(f"Unknown command: '{action}'")
        print_help()
        sys.exit(1)
