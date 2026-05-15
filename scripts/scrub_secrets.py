import os
import re

def scrub_mapbox_tokens(root_dir):
    # Regex for Mapbox public tokens (pk.ey...)
    token_pattern = re.compile(rb'pk\.ey[A-Za-z0-9._-]+')
    
    scrub_count = 0
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.endswith('.js') or '.js' in file:
                path = os.path.join(root, file)
                try:
                    with open(path, 'rb') as f:
                        data = f.read()
                    
                    if token_pattern.search(data):
                        new_data = token_pattern.sub(b'[SCRUBBED]', data)
                        with open(path, 'wb') as f:
                            f.write(new_data)
                        print(f"Scrubbed Mapbox token in {path}")
                        scrub_count += 1
                except Exception as e:
                    print(f"Error processing {path}: {e}")
    
    print(f"Finished scrubbing. Total files modified: {scrub_count}")

if __name__ == "__main__":
    scrub_mapbox_tokens(".")
