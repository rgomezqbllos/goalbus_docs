import os
import sys
import shutil
import csv
import json
import re
from collections import defaultdict

CSV_FILE = "translation_data.csv"
GLOBAL_JSON = "global_translations.json"

LANG_DIRS = {
    "Español": "ES",
    "Portugues": "PT_BR",
    "English": "EN",
    "Frances": "FR"
}

# CSS class patterns for inputs that lack data-qa-id.
# Each entry: (css_class_substring, label_prefix)
# init will detect these and assign field_id = "class:CLASSNAME:INDEX"
CLASS_INPUT_PATTERNS = [
    ("gs-text-ellipsis", "stop"),   # stop-name inputs in route editors
]

# All form field component types and their injection strategy
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


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_folder_name(path):
    return os.path.basename(os.path.normpath(path))

def detect_language_from_path(path):
    for dir_name, lang_code in LANG_DIRS.items():
        if dir_name in path:
            return lang_code, dir_name
    return None, None

def find_html_file(folder_path):
    """Return the first GoalBus HTML file found in folder_path, or None."""
    if not os.path.isdir(folder_path):
        return None
    for name in ["GoalBus.html", "GoalBus Settings.html", "GoalBus_Settings.html"]:
        candidate = os.path.join(folder_path, name)
        if os.path.exists(candidate):
            return candidate
    # Fallback: any .html in the folder root
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


def get_canonical_set(global_dict):
    """
    Build a set of every plain-text core stored in global_translations.json.

    Handles three stored formats:
      1. Wrapped:    ">Texto<"           → adds "Texto" and ">Texto<"
      2. Attribute:  'aria-label="X"'   → adds "X"
      3. Plain:      "Texto"            → adds "Texto", ">Texto<"
    And edge cases like "> Texto" (starts-with-only > from legacy data).
    """
    canonical = set()
    for trans in global_dict.values():
        es_val = trans.get("ES", "")
        if not es_val:
            continue
        canonical.add(es_val)                  # exact match always registered

        if es_val.startswith(">") and es_val.endswith("<"):
            # Standard wrapped: ">Texto<"
            inner = es_val[1:-1].strip()
            canonical.add(inner)
            canonical.add(inner.lower())

        elif re.search(r'(?:aria-label|placeholder|title|alt)="([^"]+)"', es_val):
            # Attribute-format entry: extract the value part
            m = re.search(r'"([^"]+)"', es_val)
            if m:
                val = m.group(1).strip()
                canonical.add(val)
                canonical.add(val.lower())

        elif ">" in es_val and es_val.startswith(">"):
            # Legacy partial: "> Texto" or ">Texto" (no closing <)
            inner = es_val.lstrip(">").strip()
            canonical.add(inner)
            canonical.add(inner.lower())
            canonical.add(f">{inner}<")

        elif ">" in es_val:
            # Complex format with inline content: 'class="...">Texto<'
            m = re.search(r'>([^<]+)<', es_val)
            if m:
                inner = m.group(1).strip()
                canonical.add(inner)
                canonical.add(inner.lower())

        else:
            # Plain text entry (no wrapper)
            plain = es_val.strip()
            canonical.add(plain)
            canonical.add(plain.lower())
            canonical.add(f">{plain}<")

    return canonical


def is_noise(text):
    """
    Returns True if text is not useful UI copy and should be skipped during extract.

    Skips: empty, too short, Angular template syntax, URLs, file paths,
           pure numbers/punctuation, HTML entities, excessively long strings.
    """
    t = text.strip()
    if not t or len(t) < 3:
        return True
    # Angular / template syntax
    if '{' in t or '}' in t or '@' in t:
        return True
    # URLs and file references
    if t.startswith('http') or t.startswith('//') or t.startswith('./') or t.startswith('../'):
        return True
    # HTML entities
    if '&' in t:
        return True
    # Pure numbers / punctuation (no letters)
    if re.match(r'^[\d\s\.,\-\+\%\/\:\(\)\[\]]+$', t):
        return True
    # Escape sequences
    if '\\n' in t or '\\t' in t or '\\"' in t:
        return True
    # Very long strings (likely HTML or JS fragments)
    if len(t) > 150:
        return True
    return False


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def init_folder(source_path, target_lang_dir="Portugues"):
    source_lang, source_dir = detect_language_from_path(source_path)
    if not source_lang:
        print(f"Error: Could not detect language directory in '{source_path}'")
        print(f"  Path must contain one of: {', '.join(LANG_DIRS.keys())}")
        return

    target_path = source_path.replace(source_dir, target_lang_dir)
    folder_name = get_folder_name(source_path)

    print(f"Initializing '{folder_name}' for target '{target_lang_dir}'...")

    if not os.path.exists(target_path):
        shutil.copytree(source_path, target_path)
        print(f"  Copied: {source_path}")
        print(f"       -> {target_path}")
    else:
        print(f"  Target already exists: {target_path}")

    html_file = find_html_file(source_path)
    if not html_file:
        print(f"  Warning: No HTML file found in {source_path}")
        return

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Build regex that matches all known form tags
    tags_pattern = '|'.join(re.escape(t) for t in TAG_TO_TYPE.keys())
    combined_pattern = rf'<({tags_pattern})\b[^>]*data-qa-id="([^"]+)"'
    found_fields = re.findall(combined_pattern, content, re.IGNORECASE)

    # Read existing CSV
    all_data = {}
    headers = ['folder', 'field_id', 'type'] + [LANG_DIRS[d] for d in ["Español", "Portugues", "English", "Frances"]]

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

    existing_rows_dict = {row['field_id']: row for row in all_data.get(folder_name, [])}
    new_ordered_rows = []
    seen_ids = set()

    # --- Fields with data-qa-id ---
    for tag_name, qa_id in found_fields:
        if qa_id in seen_ids:
            continue
        seen_ids.add(qa_id)

        field_type = TAG_TO_TYPE.get(tag_name.lower(), 'input_value')
        if qa_id in existing_rows_dict:
            row = existing_rows_dict[qa_id]
            row['type'] = field_type   # refresh type in case it changed
            new_ordered_rows.append(row)
        else:
            row = {'folder': folder_name, 'field_id': qa_id, 'type': field_type}
            for lang in LANG_DIRS.values():
                row[lang] = 'false' if field_type == 'checkbox_checked' else ''
            new_ordered_rows.append(row)

    # --- Fields WITHOUT data-qa-id: detected by CSS class ---
    for css_class, label in CLASS_INPUT_PATTERNS:
        # Match <input> tags that have the target class but NO data-qa-id
        pattern = rf'<input(?![^>]*data-qa-id)[^>]*class="[^"]*{re.escape(css_class)}[^"]*"[^>]*>'
        matches = re.findall(pattern, content, re.IGNORECASE)
        for idx, _ in enumerate(matches):
            field_id = f"class:{css_class}:{idx}"
            if field_id in seen_ids:
                continue
            seen_ids.add(field_id)
            if field_id in existing_rows_dict:
                new_ordered_rows.append(existing_rows_dict[field_id])
            else:
                row = {'folder': folder_name, 'field_id': field_id, 'type': 'class_indexed'}
                for lang in LANG_DIRS.values():
                    row[lang] = ''
                new_ordered_rows.append(row)

    all_data[folder_name] = new_ordered_rows

    final_output = []
    for group_name in sorted(all_data.keys()):
        final_output.extend(all_data[group_name])

    with open(CSV_FILE, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(final_output)

    print(f"  Found {len(new_ordered_rows)} form fields -> updated {CSV_FILE}")
    if new_ordered_rows:
        for r in new_ordered_rows:
            marker = " (NEW)" if r.get('ES', '') == '' and r.get('PT_BR', '') == '' else ""
            hint = "  <- fill with stop/field name" if r['type'] == 'class_indexed' and marker else ""
            print(f"    [{r['type']}] {r['field_id']}{marker}{hint}")


def build_folder(source_path, target_path):
    source_lang, _ = detect_language_from_path(source_path)
    target_lang, _ = detect_language_from_path(target_path)
    folder_name = get_folder_name(target_path)

    if not source_lang or not target_lang:
        print(f"  Error: Could not detect language in paths:")
        print(f"    source: {source_path}")
        print(f"    target: {target_path}")
        return

    print(f"  Building '{folder_name}' ({source_lang} -> {target_lang})")

    src_html = find_html_file(source_path)
    if not src_html:
        print(f"  Error: No HTML file found in {source_path}")
        return

    target_html = os.path.join(target_path, os.path.basename(src_html))

    # Copy _files dependency folder if not yet present in target
    src_files_dir = src_html.replace(".html", "_files")
    target_files_dir = target_html.replace(".html", "_files")
    if os.path.exists(src_files_dir) and not os.path.exists(target_files_dir):
        os.makedirs(os.path.dirname(target_files_dir), exist_ok=True)
        shutil.copytree(src_files_dir, target_files_dir)
        print(f"  Copied _files folder to target.")

    with open(src_html, "r", encoding="utf-8") as f:
        content = f.read()

    # --- Step 1: Apply global UI text translations ---
    text_replacements = 0
    pending_skipped = 0
    if source_lang != target_lang and os.path.exists(GLOBAL_JSON):
        global_dict = load_global_dict()

        for key, translations in global_dict.items():
            stext = translations.get(source_lang, "")
            ttext = translations.get(target_lang, "")

            if not stext or not ttext:
                continue
            if ttext == "PENDING":
                pending_skipped += 1
                continue

            if stext.startswith(">") and stext.endswith("<"):
                inner_s = stext[1:-1]
                inner_t = ttext[1:-1] if (ttext.startswith(">") and ttext.endswith("<")) else ttext

                # Tag content replacement (handles whitespace padding)
                pattern = r'>\s*' + re.escape(inner_s) + r'\s*<'
                new_content = re.sub(pattern, '>' + inner_t + '<', content)
                if new_content != content:
                    text_replacements += 1
                content = new_content

                # Attribute replacement (placeholder, title, aria-label, alt)
                attr_pattern = r'(\b(?:placeholder|title|aria-label|alt)="\s*)' + re.escape(inner_s) + r'(\s*")'
                content = re.sub(attr_pattern, r'\g<1>' + inner_t + r'\g<2>', content)

            else:
                # Direct literal replacement (legacy / special entries)
                if stext in content:
                    text_replacements += 1
                content = content.replace(stext, ttext)

    # --- Step 2: Inject form data for target language ---
    fields_injected = 0
    fields_skipped = 0
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['folder'] != folder_name:
                    continue
                field_id  = row['field_id']
                field_type = row['type']
                value = row.get(target_lang)

                if value is None:
                    continue

                # Escape field_id for safe use in regex
                eid = re.escape(field_id)

                if field_type == "input_value":
                    # Update value="" attribute
                    pattern = rf'(data-qa-id="{eid}"[^>]*?)(?:\s+value="[^"]*")?'
                    new_content = re.sub(pattern, rf'\g<1> value="{value}"', content)
                    if new_content != content:
                        fields_injected += 1
                    else:
                        fields_skipped += 1
                    content = new_content
                    # Also update hidden span (display value)
                    pattern_span = rf'(data-qa-id="{eid}".*?<span[^>]+class="hidden">).*?(</span>)'
                    content = re.sub(pattern_span, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)

                elif field_type == "field_value":
                    pattern = rf'(data-qa-id="{eid}".*?class="field-value[^"]*">).*?(</span>)'
                    new_content = re.sub(pattern, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)
                    if new_content != content:
                        fields_injected += 1
                    else:
                        fields_skipped += 1
                    content = new_content

                elif field_type == "checkbox_checked":
                    if str(value).lower() == "true":
                        pattern = rf'(data-qa-id="{eid}"[^>]*?)(?:\s+checked)?(?=>)'
                        content = re.sub(pattern, rf'\g<1> checked', content)
                    else:
                        pattern = rf'(data-qa-id="{eid}"[^>]*?)\s+checked'
                        content = re.sub(pattern, r'\g<1>', content)
                    fields_injected += 1

                elif field_type == "date_picker":
                    pattern = rf'(data-qa-id="{eid}".*?<span[^>]*>).*?(</span>)'
                    new_content = re.sub(pattern, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)
                    if new_content != content:
                        fields_injected += 1
                    else:
                        fields_skipped += 1
                    content = new_content

                elif field_type == "class_indexed":
                    # field_id format: "class:CLASSNAME:INDEX"
                    parts = field_id.split(':', 2)
                    if len(parts) != 3:
                        fields_skipped += 1
                        continue
                    _, css_class, idx_str = parts
                    try:
                        idx = int(idx_str)
                    except ValueError:
                        fields_skipped += 1
                        continue
                    # Find all inputs with this class that lack data-qa-id
                    cls_pattern = rf'<input(?![^>]*data-qa-id)[^>]*class="[^"]*{re.escape(css_class)}[^"]*"[^>]*>'
                    all_matches = list(re.finditer(cls_pattern, content, re.IGNORECASE))
                    if idx < len(all_matches):
                        m = all_matches[idx]
                        old_tag = m.group(0)
                        # Remove any existing value attribute, then inject new one
                        new_tag = re.sub(r'\s+value="[^"]*"', '', old_tag)
                        new_tag = new_tag.rstrip('>') + f' value="{value}">'
                        content = content[:m.start()] + new_tag + content[m.end():]
                        fields_injected += 1
                    else:
                        fields_skipped += 1

    # --- Step 3: Inject static map image (replaces Mapbox canvas) ---
    map_injected = False
    map_png_path = os.path.join(os.path.dirname(src_html), "GoalBus_files", "mapa.png")
    # Also check target _files in case it was placed there directly
    map_png_target = os.path.join(target_path, "GoalBus_files", "mapa.png")
    if os.path.exists(map_png_path) or os.path.exists(map_png_target):
        canvas_pattern = r'<canvas[^>]*class="[^"]*mapboxgl-canvas[^"]*"[^>]*>(?:</canvas>)?'
        map_img = '<img src="./GoalBus_files/mapa.png" style="width:100%;height:100%;object-fit:cover;display:block;" alt="Map">'
        new_content = re.sub(canvas_pattern, map_img, content, flags=re.IGNORECASE)
        if new_content != content:
            content = new_content
            map_injected = True

    os.makedirs(os.path.dirname(target_html) if os.path.dirname(target_html) else ".", exist_ok=True)

    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)

    summary = f"  Done: {text_replacements} text replacements, {fields_injected} fields injected"
    if map_injected:
        summary += " | map: OK"
    elif not map_injected:
        summary += " | map: no mapa.png found"
    if pending_skipped:
        summary += f" ({pending_skipped} translations still PENDING)"
    if fields_skipped:
        summary += f" ({fields_skipped} form fields not matched)"
    print(summary)


def show_status():
    """Print a human-friendly translation status report."""
    print("=" * 50)
    print("TRANSLATION STATUS")
    print("=" * 50)

    # --- Global dictionary ---
    global_dict = load_global_dict()
    total = len(global_dict)
    langs = list(LANG_DIRS.values())

    print(f"\nGlobal Dictionary ({GLOBAL_JSON}): {total} entries")

    pending_by_lang = {lang: [] for lang in langs}
    for key, trans in global_dict.items():
        for lang in langs:
            val = trans.get(lang, "")
            if val == "PENDING" or not val:
                pending_by_lang[lang].append((key, trans.get("ES", "")))

    for lang in langs:
        pending = pending_by_lang[lang]
        translated = total - len(pending)
        bar = "#" * int(translated / max(total, 1) * 20)
        pct = int(translated / max(total, 1) * 100)
        print(f"  {lang:<8} [{bar:<20}] {pct:3d}%  {translated}/{total} done, {len(pending)} PENDING")

    # List pending PT_BR (the primary target language)
    pt_pending = pending_by_lang.get("PT_BR", [])
    if pt_pending:
        print(f"\n  PENDING (PT_BR) — {len(pt_pending)} items:")
        for key, es_val in pt_pending:
            display = es_val[:60] + "..." if len(es_val) > 60 else es_val
            print(f"    {key}: \"{display}\"")
    else:
        print("\n  All PT_BR translations complete!")

    # --- CSV form data ---
    print(f"\nForm Data ({CSV_FILE}):")
    if not os.path.exists(CSV_FILE):
        print("  File not found")
        return

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    by_folder = defaultdict(list)
    for row in rows:
        by_folder[row['folder']].append(row)

    any_incomplete = False
    for folder_name in sorted(by_folder.keys()):
        folder_rows = by_folder[folder_name]
        total_fields = len(folder_rows)
        pt_filled = sum(1 for r in folder_rows if r.get('PT_BR', '').strip())
        es_filled = sum(1 for r in folder_rows if r.get('ES', '').strip())
        status = "OK" if pt_filled == total_fields else f"INCOMPLETE ({total_fields - pt_filled} empty)"
        if pt_filled < total_fields:
            any_incomplete = True
        print(f"  {folder_name:<20} {total_fields} fields | ES:{es_filled}/{total_fields} | PT_BR:{pt_filled}/{total_fields}  {status}")

    if not any_incomplete:
        print("\n  All CSV form fields filled!")

    print("=" * 50)


def extract_vocabulary(source_path, dry_run=False):
    """
    Scan an HTML file and add any new UI text strings to global_translations.json.

    Uses a canonical set built from all existing entries to reliably detect
    duplicates regardless of storage format (wrapped, plain, attribute-style).
    """
    mode = "[DRY RUN] " if dry_run else ""
    print(f"{mode}Extracting vocabulary from: {source_path}")

    html_file = find_html_file(source_path)
    if not html_file:
        print(f"  Error: No HTML file found in {source_path}")
        return

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Strip non-visible sections
    clean = re.sub(r'<script\b.*?</script>', '', content, flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r'<style\b.*?</style>',   '', clean,   flags=re.DOTALL | re.IGNORECASE)
    clean = re.sub(r'<!--.*?-->',             '', clean,   flags=re.DOTALL)

    # Extract text nodes and relevant attribute values
    tag_texts  = re.findall(r'>([^<\n]+)<', clean)
    attr_texts = re.findall(r'(?:placeholder|title|aria-label|alt)="\s*([^"]{3,}?)\s*"', clean)

    raw_candidates = set()
    for t in tag_texts + attr_texts:
        stripped = t.strip()
        if stripped:
            raw_candidates.add(stripped)

    # Sort for deterministic output
    candidates = sorted(raw_candidates)

    global_dict = load_global_dict()
    canonical = get_canonical_set(global_dict)

    # Determine next available ID
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

    for txt in candidates:
        if is_noise(txt):
            skipped_noise += 1
            continue
        # Check against canonical set (handles all stored formats)
        if txt in canonical or txt.lower() in canonical or f">{txt}<" in canonical:
            skipped_dup += 1
            continue
        new_entries.append(txt)

    print(f"  Scanned: {len(candidates)} candidates | "
          f"noise filtered: {skipped_noise} | "
          f"already exists: {skipped_dup} | "
          f"new: {len(new_entries)}")

    if not new_entries:
        print("  Nothing new to add.")
        return

    print(f"\n  New terms to add ({len(new_entries)}):")
    for txt in new_entries:
        print(f"    \"{txt}\"")

    if dry_run:
        print("\n  [DRY RUN] No changes made. Run without --dry-run to save.")
        return

    for txt in new_entries:
        max_id += 1
        global_dict[f"ui_text_{max_id}"] = {
            "ES":    f">{txt}<",
            "PT_BR": "PENDING",
            "EN":    "PENDING",
            "FR":    "PENDING"
        }

    save_global_dict(global_dict)
    print(f"\n  Saved {len(new_entries)} new PENDING entries to {GLOBAL_JSON}.")
    print(f"  Next step: ask AI to translate the PENDING entries, then run 'build'.")


def print_help():
    print("""
GoalBus DOM Localization Pipeline
==================================

COMMANDS:
  init <source_path>              Scan page for form fields, register in CSV.
  extract <source_path>           Find new UI texts, add as PENDING to JSON.
  extract <source_path> --dry-run Preview what would be added (no changes).
  status                          Show translation progress (JSON + CSV).
  build <target_path>             Apply translations + inject form data.
  build_all                       Rebuild ALL pages in all languages.
  help                            Show this message.

TYPICAL WORKFLOW FOR A NEW PAGE:
  1. Place HTML in:  Español/Px/Px_imagenX/GoalBus.html
  2. Init:           python3 scripts/goalbus_localize.py init "Español/Px/Px_imagenX"
  3. Fill CSV:       Edit translation_data.csv — add ES and PT_BR demo values
  4. Extract:        python3 scripts/goalbus_localize.py extract "Español/Px/Px_imagenX"
     (optional)      python3 scripts/goalbus_localize.py extract "Español/Px/Px_imagenX" --dry-run
  5. Translate:      Ask AI to fill all PENDING entries in global_translations.json
  6. Check status:   python3 scripts/goalbus_localize.py status
  7. Build:          python3 scripts/goalbus_localize.py build "Portugues/Px/Px_imagenX"
     or rebuild all: python3 scripts/goalbus_localize.py build_all
  8. Open in browser and screenshot.

NOTES:
  - 'build' always reads from the Español source and writes to the target language.
  - 'build_all' rebuilds every initialized page in Portugues/.
  - After editing global_translations.json or translation_data.csv, always run build_all.
""")


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "help"):
        print_help()
        sys.exit(0)

    action = sys.argv[1]

    if action == "status":
        show_status()

    elif action == "build_all":
        print("=== BUILDING ALL PAGES ===")
        es_root = "Español"
        if not os.path.exists(es_root):
            print(f"Error: '{es_root}' directory not found. Run from project root.")
            sys.exit(1)

        built = 0
        for p_folder in sorted(os.listdir(es_root)):
            p_path = os.path.join(es_root, p_folder)
            if not os.path.isdir(p_path) or not p_folder.startswith("P"):
                continue
            for item in sorted(os.listdir(p_path)):
                source_path = os.path.join(p_path, item)
                if not os.path.isdir(source_path) or not item.startswith("P"):
                    continue

                # Build Español (only injects form data, no translation)
                build_folder(source_path, source_path)

                # Build Portugues (full translation + form data)
                pt_path = os.path.join("Portugues", p_folder, item)
                build_folder(source_path, pt_path)
                built += 1

        print(f"=== DONE: {built} page(s) built ===")

    elif action in ("init", "extract", "build"):
        if len(sys.argv) < 3:
            print(f"Error: '{action}' requires a folder path.")
            print_help()
            sys.exit(1)

        folder_path = sys.argv[2]

        if action == "init":
            init_folder(folder_path)

        elif action == "extract":
            dry_run = "--dry-run" in sys.argv
            extract_vocabulary(folder_path, dry_run=dry_run)

        elif action == "build":
            # Derive source (Español) from target path, or use path as-is if it IS Español
            source_path = folder_path
            target_lang_dir = None
            for tdir in ("Portugues", "English", "Frances"):
                if tdir in folder_path:
                    source_path = folder_path.replace(tdir, "Español")
                    target_lang_dir = tdir
                    break

            if not os.path.exists(source_path):
                print(f"Error: Source path not found: {source_path}")
                print(f"  Make sure you have the Español version of this page.")
                sys.exit(1)

            build_folder(source_path, folder_path)

    else:
        print(f"Unknown command: '{action}'")
        print_help()
        sys.exit(1)
