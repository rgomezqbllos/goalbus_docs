import re

text = "> ¡Hola, Alan! </h1>"
tag_map = {"¡Hola, Alan!": "Hello, John Smith!"}

sorted_sources = sorted(tag_map.keys(), key=len, reverse=True)
escaped = [re.escape(s) for s in sorted_sources]
pattern = r'>\s*(' + '|'.join(escaped) + r')\s*<'
compiled = re.compile(pattern)

def replacer(m):
    src = m.group(1).strip()
    return f">{tag_map[src]}<"

new_text = compiled.sub(replacer, text)
print(f"Original: {text}")
print(f"New: {new_text}")
print(f"Match found: {compiled.search(text) is not None}")
