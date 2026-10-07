"""Regenerate index.html (and optionally the card images) from the transcriptions.

    python tools/build.py                      # rebuild index.html only
    python tools/build.py path/to/vmod/images  # also re-export cards/*.webp (needs Pillow)

The images folder comes from unzipping "Thirty Years of Misery V1.vmod".
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS = os.path.join(ROOT, 'tools')
SRC_IMAGES = sys.argv[1] if len(sys.argv) > 1 else None

cards = []
for f in ['cards_imp.txt', 'cards_cl.txt', 'cards_fra.txt', 'cards_swe.txt', 'cards_tr.txt']:
    for line in open(os.path.join(TOOLS, f), encoding='utf-8'):
        line = line.rstrip('\n')
        if not line or line.startswith('##'): continue
        p = line.split('|')
        assert len(p) == 9, line
        img, fac, n, title, horse, boot, timing, text, flavor = p
        n = int(n)
        if fac == 'tr':
            deck = timing  # Troubles group A-D
            timing = ''
            kind = 'troubles'
        else:
            deck = 'W' if n == 1 else ('B' if (n >= 19 if fac in ('swe', 'fra') else n >= 20) else 'A')
            t = timing.lower()
            if 'battle' in t: kind = 'battle'
            elif '{rel}' in t: kind = 'religion'
            elif 'of a round' in t: kind = 'round'
            elif 'start of' in t or 'when drawing' in t: kind = 'turn'
            else: kind = 'special'
            if n == 1: kind = 'treaty'
        slug = f'{fac}-{n:02d}'
        if SRC_IMAGES:
            from PIL import Image
            Image.open(os.path.join(SRC_IMAGES, img)).convert('RGB').save(
                os.path.join(ROOT, 'cards', f'{slug}.webp'), 'WEBP', quality=82, method=6)
        cards.append(dict(id=slug, f=fac, n=n, t=title, h=int(horse) if horse else None, b=int(boot) if boot else None,
                          d=deck, k=kind, w=timing, x=text, fl=flavor, star=title.endswith('*')))

tpl = open(os.path.join(TOOLS, 'template.html'), encoding='utf-8').read()
with open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8') as out:
    out.write(tpl.replace('/*DATA*/[]', json.dumps(cards, ensure_ascii=False, separators=(',', ':'))))
print(f'{len(cards)} cards -> index.html')
