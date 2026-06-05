import os
import shutil
import re

def create_compares():
    target_base = "compares"
    sources = ["Español", "English", "Portugues", "Frances"]
    
    # Check if compares exists and clean it
    if os.path.exists(target_base):
        print(f"Cleaning existing directory: {target_base}")
        shutil.rmtree(target_base)
    
    os.makedirs(target_base, exist_ok=True)
    print(f"Created target directory: {target_base}")
    
    for source in sources:
        if not os.path.exists(source):
            print(f"Warning: Source folder '{source}' not found. Skipping.")
            continue
            
        print(f"Processing images from: {source}")
        
        # Use os.walk to find all .png files recursively
        for root, dirs, files in os.walk(source):
            # The root will be something like 'Español/P1'
            rel_path = os.path.relpath(root, source)
            if rel_path == ".":
                continue
                
            # Get the PX part (first component of relative path)
            path_parts = rel_path.split(os.sep)
            px_dir = path_parts[0]
            
            for file in files:
                if file.lower().endswith(".png"):
                    # Get filename without extension
                    filename_ext = os.path.splitext(file)
                    filename_no_ext = filename_ext[0]
                    
                    # Normalize base folder name by stripping _old or _Old suffix
                    # We use a case-insensitive regex swap for the folder name only
                    base_folder_name = re.sub(r'_old$', '', filename_no_ext, flags=re.IGNORECASE)
                    
                    # Target path: compares/PX/BaseName/Language_PX_OriginalName.png
                    new_dest_dir = os.path.join(target_base, px_dir, base_folder_name)
                    os.makedirs(new_dest_dir, exist_ok=True)
                    
                    # Target filename with language prefix
                    new_filename = f"{source}_{file}"
                    
                    # Prefix 'old' files with '0_' to ensure they appear first in alphabetic sort
                    if re.search(r'_old\.png$', file, re.IGNORECASE):
                        new_filename = f"0_{new_filename}"
                        
                    dest_file_path = os.path.join(new_dest_dir, new_filename)
                    
                    src_file_path = os.path.join(root, file)
                    
                    # Copy file
                    shutil.copy2(src_file_path, dest_file_path)
                    
    print("Comparison structure creation complete.")

if __name__ == "__main__":
    create_compares()
