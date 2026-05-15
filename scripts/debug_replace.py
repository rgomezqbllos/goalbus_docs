import json
import re

with open('Español/D1/D1_imagen3/GoalBus.Driver.html', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.read()

tag_map = {"¡Hola, Alan!": "Hello, John Smith!"}
sorted_sources = sorted(tag_map.keys(), key=len, reverse=True)
escaped = [re.escape(s) for s in sorted_sources]
pattern = r'>\s*(' + '|'.join(escaped) + r')\s*<'
compiled = re.compile(pattern)

def replacer(m):
    src = m.group(1).strip()
    print(f"Matched: '{src}'")
    return f">{tag_map[src]}<"

new_content = compiled.sub(replacer, content)

if "Hello, John Smith!" in new_content:
    print("Success: John Smith found in new content")
else:
    print("Failure: John Smith NOT found")

# Let's see why it might fail
if "¡Hola, Alan!" in content:
    print("¡Hola, Alan! is definitely in content")
    # Check for non-breaking spaces or other weirdness
    pos = content.find("¡Hola, Alan!")
    context = content[pos-5:pos+20]
    print(f"Exact context: repr({repr(context)})")
