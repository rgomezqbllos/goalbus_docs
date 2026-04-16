import os
import shutil
import glob

def sync_final():
    # Target directory
    target_base = "Final"
    
    # Source directories
    sources = ["Español", "English", "Portugues"]
    
    # Check if target exists and if it's a file, remove it
    if os.path.exists(target_base):
        if os.path.isdir(target_base):
            print(f"Cleaning existing directory: {target_base}")
            shutil.rmtree(target_base)
        else:
            print(f"Removing existing file: {target_base}")
            os.remove(target_base)
            
    # Create target directory
    os.makedirs(target_base, exist_ok=True)
    print(f"Created target directory: {target_base}")
    
    for source in sources:
        if not os.path.exists(source):
            print(f"Warning: Source directory '{source}' not found. Skipping.")
            continue
            
        print(f"Processing manual copy for: {source}")
        
        # Use os.walk to find all .png files
        for root, dirs, files in os.walk(source):
            for file in files:
                if file.lower().endswith(".png"):
                    # Original file path
                    src_file_path = os.path.join(root, file)
                    
                    # Relative path from source
                    rel_path = os.path.relpath(src_file_path, os.getcwd())
                    # This rel_path will start with 'Español/' etc.
                    
                    # Target file path
                    dest_file_path = os.path.join(target_base, rel_path)
                    
                    # Ensure destination directory exists
                    os.makedirs(os.path.dirname(dest_file_path), exist_ok=True)
                    
                    # Copy the file
                    shutil.copy2(src_file_path, dest_file_path)
                    
    print("Sync complete.")

if __name__ == "__main__":
    sync_final()
