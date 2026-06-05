import json
from pathlib import Path

data = json.loads(Path(r'C:\tmp\Proyectos\goalbus_docs\global_translations.json').read_text(encoding='utf-8'))
langs = ['EN', 'PT_BR', 'DE', 'FR', 'IT']
pending = {k: v for k, v in data.items() if any(v.get(l) in (None, 'PENDING') for l in langs)}
print('Total pending:', len(pending))
for key, v in list(pending.items()):
    es = v.get('ES', '?')
    missing = [l for l in langs if v.get(l) in (None, 'PENDING')]
    print(f'  {key}  ES={repr(es)[:40]}  missing={missing}')
