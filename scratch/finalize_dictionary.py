import json

def finalize_pending():
    with open('global_translations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    modified = False
    for key, item in data.items():
        if item.get("PT_BR") == "PENDING":
            es_val = item["ES"].strip(">").strip("<")
            
            # Icon/Code logic: if it's alphanumeric/underscore and shortish, keep as is
            if es_val.islower() and " " not in es_val:
                item["PT_BR"] = item["ES"]
                modified = True
            elif es_val == "Mapbox homepage":
                item["PT_BR"] = ">Página inicial do Mapbox<"
                modified = True
            elif es_val == "L1 - 1 / L1 - 1":
                item["PT_BR"] = ">L1 - 1 / L1 - 1<"
                modified = True
            elif es_val == "0.0 km":
                item["PT_BR"] = ">0.0 km<"
                modified = True

    if modified:
        with open('global_translations.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("Dictionary finalized.")

finalize_pending()
