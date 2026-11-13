#!/usr/bin/env python3
"""Stämplar spelens versions-id. Kör före varje commit som ändrar ett spel:

    python3 tools/stamp_version.py

För index.html och jul/index.html: räknar ett fingeravtryck (sha1) av sidans innehåll,
skriver in det i raden  var BUILD_ID = '...';  och skriver samma värde till version.json
i samma mapp. Sidan jämför sitt eget BUILD_ID med version.json varje minut och visar
bannern "Ny version finns tillgänglig" när de skiljer sig.

Eftersom id:t bygger på innehållet ändras det bara när sidan faktiskt har ändrats,
så bannern visas aldrig i onödan.
"""
import hashlib
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
PAGES = ['index.html', 'jul/index.html']
PATTERN = re.compile(r"var BUILD_ID = '[^']*';")

for page in PAGES:
    path = ROOT / page
    text = path.read_text(encoding='utf-8')
    if not PATTERN.search(text):
        print(f'{page}: ingen BUILD_ID-rad, hoppar över')
        continue
    # Nollställ id:t innan hashningen så att resultatet inte beror på föregående stämpel
    normalized = PATTERN.sub("var BUILD_ID = '';", text)
    build = hashlib.sha1(normalized.encode('utf-8')).hexdigest()[:12]
    path.write_text(PATTERN.sub(f"var BUILD_ID = '{build}';", text), encoding='utf-8')
    (path.parent / 'version.json').write_text(json.dumps({'build': build}) + '\n', encoding='utf-8')
    print(f'{page}: {build}')
