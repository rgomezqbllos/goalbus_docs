import os
import sys
import shutil
import csv
import json
import re

CSV_FILE = "translation_data.csv"
GLOBAL_JSON = "global_translations.json"

# Master mapping for directory names to language codes
LANG_DIRS = {
    "Español": "ES",
    "Portugues": "PT_BR",
    "English": "EN",
    "Frances": "FR"
}

def get_folder_name(path):
    return os.path.basename(os.path.normpath(path))

def detect_language_from_path(path):
    for dir_name, lang_code in LANG_DIRS.items():
        if dir_name in path:
            return lang_code, dir_name
    return None, None

def init_folder(source_path, target_lang_dir="Portugues"):
    source_lang, source_dir = detect_language_from_path(source_path)
    if not source_lang:
        print(f"Error: Could not detect known language directory in '{source_path}'")
        return

    target_path = source_path.replace(source_dir, target_lang_dir)
    folder_name = get_folder_name(source_path)
    
    print(f"Initializing {folder_name} for target {target_lang_dir}...")
    
    # 1. Copy directory
    if not os.path.exists(target_path):
        shutil.copytree(source_path, target_path)
        print(f"Copied {source_path} -> {target_path}")
    else:
        print(f"Target {target_path} already exists. (Files will be refreshed on build)")
        
    html_file = os.path.join(source_path, "GoalBus.html")
    if not os.path.exists(html_file):
        html_file = os.path.join(source_path, "GoalBus Settings.html")
    
    if not os.path.exists(html_file):
        print(f"Warning: HTML file not found in {source_path}")
        return
    # 2. Parse all fields in document order
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    tag_to_type = {
        'input': 'input_value',
        'gs-select': 'field_value',
        'gs-checkbox': 'checkbox_checked',
        'gs-date-picker': 'date_picker',
        'gs-date-picker-range': 'date_picker'
    }
    combined_pattern = r'<(input|gs-select|gs-checkbox|gs-date-picker(?:-range)?)[^>]+data-qa-id="([^"]+)"'
    found_fields = re.findall(combined_pattern, content)
    
    # 3. Read ALL existing data and organize it
    all_data = {} # folder -> [rows]
    headers = ['folder', 'field_id', 'type'] + [LANG_DIRS[d] for d in ["Español", "Portugues", "English", "Frances"]]
    
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            headers = reader.fieldnames
            for row in reader:
                group = row['folder']
                if group not in all_data: all_data[group] = []
                all_data[group].append(row)

    # 4. Update the current folder's field list preserving HTML order
    existing_rows_dict = {row['field_id']: row for row in all_data.get(folder_name, [])}
    new_ordered_rows = []
    seen_ids = set()

    for tag_name, qa_id in found_fields:
        if qa_id in seen_ids: continue # skip duplicates in HTML if any
        seen_ids.add(qa_id)
        
        field_type = tag_to_type.get(tag_name, 'input_value')
        if qa_id in existing_rows_dict:
            row = existing_rows_dict[qa_id]
            row['type'] = field_type # update type just in case
            new_ordered_rows.append(row)
        else:
            row = {'folder': folder_name, 'field_id': qa_id, 'type': field_type}
            for lang in LANG_DIRS.values():
                row[lang] = 'false' if field_type == 'checkbox_checked' else ''
            new_ordered_rows.append(row)
    
    all_data[folder_name] = new_ordered_rows

    # 5. Write back EVERYTHING sorted by folder name
    final_output = []
    for group_name in sorted(all_data.keys()):
        final_output.extend(all_data[group_name])

    with open(CSV_FILE, "w", encoding="utf-8", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(final_output)
        
    print(f"Updated {folder_name} in {CSV_FILE} with sequential order and global sorting.")


def build_folder(source_path, target_path):
    source_lang, _ = detect_language_from_path(source_path)
    target_lang, _ = detect_language_from_path(target_path)
    folder_name = get_folder_name(target_path)
    
    if not source_lang or not target_lang:
        print(f"Error: Invalid source/target paths for {folder_name}")
        return

    print(f"  Building {folder_name} ({source_lang} -> {target_lang})")
    
    src_html = os.path.join(source_path, "GoalBus.html")
    if not os.path.exists(src_html):
        src_html = os.path.join(source_path, "GoalBus Settings.html")
        
    target_html = os.path.join(target_path, os.path.basename(src_html))

    if not os.path.exists(src_html):
        print(f"  Error: Source HTML file not found at {src_html}")
        return

    # Automatically copy the _files dependency folder if it exists in source but not in target
    src_files_dir = src_html.replace(".html", "_files")
    target_files_dir = target_html.replace(".html", "_files")
    if os.path.exists(src_files_dir) and not os.path.exists(target_files_dir):
        os.makedirs(os.path.dirname(target_files_dir), exist_ok=True)
        shutil.copytree(src_files_dir, target_files_dir)

    with open(src_html, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Apply JSON background translations using matrix
    if source_lang != target_lang and os.path.exists(GLOBAL_JSON):
        with open(GLOBAL_JSON, "r", encoding="utf-8") as f:
            global_dict = json.load(f)
        
        for key, translations in global_dict.items():
            stext = translations.get(source_lang, "")
            ttext = translations.get(target_lang, "")
            if not stext or not ttext:
                continue
                
            if stext.startswith(">") and stext.endswith("<"):
                inner_s = stext[1:-1]
                inner_t = ttext[1:-1] if (ttext.startswith(">") and ttext.endswith("<")) else ttext
                
                # 1. Flexible tag replacement (handles whitespace padding like '> Text <')
                pattern = r'>\s*' + re.escape(inner_s) + r'\s*<'
                repl = r'>' + inner_t + r'<'
                content = re.sub(pattern, repl, content)
                
                # 2. Attribute replacement (tooltips, placeholders, etc.)
                attr_pattern = r'(\b(?:placeholder|title|aria-label|alt)="\s*)' + re.escape(inner_s) + r'(\s*")'
                attr_repl = r'\g<1>' + inner_t + r'\g<2>'
                content = re.sub(attr_pattern, attr_repl, content)
            else:
                # Direct literal replacement (legacy/special keys)
                content = content.replace(stext, ttext)
    
    # 2. Inject Form Data for TARGET Language
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['folder'] == folder_name:
                    field_id = row['field_id']
                    field_type = row['type']
                    value = row.get(target_lang)
                    
                    # Skip only if the column is missing from the CSV entirely. 
                    # If the value is an empty string (""), we want to apply it to "clear" the field.
                    if value is None:
                        continue
                        
                    if field_type == "input_value":
                        pattern = rf'(data-qa-id="{field_id}"[^>]*?)(?:\s+value="[^"]*")?'
                        content = re.sub(pattern, rf'\g<1> value="{value}"', content)
                        pattern_span = rf'(data-qa-id="{field_id}".*?<span[^>]+class="hidden">).*?(</span>)'
                        content = re.sub(pattern_span, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)
                        
                    elif field_type == "field_value":
                        pattern = rf'(data-qa-id="{field_id}".*?class="field-value[^"]*">).*?(</span>)'
                        content = re.sub(pattern, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)
                        
                    elif field_type == "checkbox_checked":
                        if str(value).lower() == "true":
                            pattern = rf'(data-qa-id="{field_id}"[^>]*?)(?:\s+checked)?'
                            content = re.sub(pattern, rf'\g<1> checked', content)
                        else:
                            pattern = rf'(data-qa-id="{field_id}"[^>]*?)\s+checked'
                            content = re.sub(pattern, r'\g<1>', content)
                            
                    elif field_type == "date_picker":
                        # Matches span contents inside date picker
                        pattern = rf'(data-qa-id="{field_id}".*?<span[^>]*>).*?(</span>)'
                        content = re.sub(pattern, rf'\g<1>{value}\g<2>', content, flags=re.DOTALL)

    os.makedirs(os.path.dirname(target_html), exist_ok=True)
    
    with open(target_html, "w", encoding="utf-8") as f:
        f.write(content)

def extract_vocabulary(target_path):
    print(f"Extracting new vocabulary from {target_path}...")
    
    html_file = os.path.join(target_path, "GoalBus.html")
    if not os.path.exists(html_file):
        html_file = os.path.join(target_path, "GoalBus Settings.html")
    
    if not os.path.exists(html_file):
        print(f"Error: HTML file not found in {target_path}")
        return

    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Clean HTML: remove scripts, styles, and comments
    clean_html = re.sub(r'<script.*?>.*?</script>', '', content, flags=re.DOTALL)
    clean_html = re.sub(r'<style.*?>.*?</style>', '', clean_html, flags=re.DOTALL)
    clean_html = re.sub(r'<!--.*?-->', '', clean_html, flags=re.DOTALL)

    # 1. Find text nodes between tags
    tag_matches = re.findall(r'>([^<]+)<', clean_html)
    # 2. Find common UI attributes (placeholders, tooltips, etc.)
    attr_matches = re.findall(r'(?:placeholder|title|aria-label|alt)="\s*([^"]+?)\s*"', clean_html)
    
    all_extracted = tag_matches + attr_matches
    unique_texts = sorted(list(set([t.strip() for t in all_extracted if len(t.strip()) > 2])))

    # Load existing dictionary
    global_dict = {}
    if os.path.exists(GLOBAL_JSON):
        with open(GLOBAL_JSON, "r", encoding="utf-8") as f:
            global_dict = json.load(f)

    # Map existing ES values to avoid duplicates
    existing_es_texts = set()
    max_id = 0
    for key, trans in global_dict.items():
        if "ES" in trans:
            existing_es_texts.add(trans["ES"])
        
        # Try to track max ID to generate new ones
        try:
            id_num = int(key.split('_')[-1])
            if id_num > max_id:
                max_id = id_num
        except:
            pass

    # Find new strings
    new_entries = 0
    for txt in unique_texts:
        wrapped_txt = f">{txt}<"
        if wrapped_txt not in existing_es_texts:
            max_id += 1
            new_key = f"ui_text_{max_id}"
            global_dict[new_key] = {
                "ES": wrapped_txt,
                "PT_BR": "PENDING",
                "EN": "PENDING",
                "FR": "PENDING"
            }
            new_entries += 1

    if new_entries > 0:
        with open(GLOBAL_JSON, "w", encoding="utf-8") as f:
            json.dump(global_dict, f, indent=2, ensure_ascii=False)
        print(f"Successfully added {new_entries} new terms to {GLOBAL_JSON} as 'PENDING'.")
    else:
        print("No new terms found to add.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python goalbus_localize.py [init|build|build_all|extract] [args]")
        sys.exit(1)
        
    action = sys.argv[1]
    
    if action == "build_all":
        print("=== BUILDING ALL FOLDERS ACROSS ALL LANGUAGES ===")
        es_root = "Español"
        if os.path.exists(es_root):
            for p_folder in os.listdir(es_root):
                p_path = os.path.join(es_root, p_folder)
                if os.path.isdir(p_path) and p_folder.startswith("P"):
                    for item in os.listdir(p_path):
                        source_path = os.path.join(p_path, item)
                        if os.path.isdir(source_path) and item.startswith("P"):
                            # Build for Español (just injects data, ignores mapping)
                            build_folder(source_path, source_path)
                            
                            # Build for Portugues 
                            pt_path = os.path.join("Portugues", p_folder, item)
                            build_folder(source_path, pt_path)
                            
        print("=== ALL BUILDS COMPLETE ===")
        
    else:
        if len(sys.argv) < 3:
            print("Action requires a folder path.")
            sys.exit(1)
            
        target_path = sys.argv[2]
        if action == "init":
            init_folder(target_path)
        elif action == "extract":
            extract_vocabulary(target_path)
        elif action == "build":
            source_path = target_path.replace("Portugues", "Español").replace("English", "Español").replace("Frances", "Español")
            if not os.path.exists(source_path):
                source_path = target_path
                
            build_folder(source_path, target_path)
        else:
            print("Unknown action. Use 'init', 'build', 'build_all', or 'extract'.")
