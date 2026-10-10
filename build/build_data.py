"""Builds data/app_data.json (the content embedded in index.html) from the extracted data.
Run:  python3 build/build_data.py   then   python3 build/build_app.py
"""
import json, os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = {q['id']: q for q in json.load(open(f'{R}/data/questions_all.json'))}
sel = json.load(open(f'{R}/data/selection_300.json'))['sets']
alt = json.load(open(f'{R}/data/image_alt.json'))
bands = json.load(open(f'{R}/data/diagnostic_score_bands.json'))['bands']
CH = {1:'Legal Responsibilities, Site Roles, and Documentation',2:'Risk Assessment',3:'Accidents and Fire',
      4:'Hazardous Substances, Noise, Vibration and Manual Handling',5:'Occupational Health and Welfare',6:'PPE and Signage',
      7:'Working at Height',8:'Excavations, Confined Spaces and Electrical',9:'Plant, Vehicles and Lifting',10:'Environmental Protection'}
def clean(t):
    t = t.replace(' --- ', ' — ').replace('---', '—')
    return re.sub(r'\s*CHAPTER TO REVISE:.*$', '', t, flags=re.S).strip()
def rec(q):
    L = 'ABCD'
    r = {'id': q['id'], 'ch': q['chapter'], 'ref': q['ref'], 'stem': clean(q['stem']),
         'o': [clean(q['options'][x]) for x in L], 'c': L.index(q['correct_letter']),
         'why': [clean(q['why_wrong'].get(x, '')) if x != q['correct_letter'] else '' for x in L],
         'ex': clean(q['explanation']), 'cm': clean(q['common_mistake'])}
    assert len(set(r['o'])) == 4 and all(r['why'][i] for i in range(4) if i != r['c']), q['id']
    if q['image']:
        r['img'] = f"images/q/{q['id']}.webp"; r['alt'] = alt[q['id']]
        assert os.path.exists(f"{R}/{r['img']}"), q['id']
    return r
bank = [rec(Q[i]) for s in sel for i in s['questions']]
diag = [rec(Q[f'diag-q{n}']) for n in range(1, 16)]

# ---- Flashcards: only the book's boxes (50 Exam Alerts, 50 Common Mistakes, 50 Memory Aids, 36 Quick Checks)
subs = json.load(open(f'{R}/data/subchapters.json'))
def split_myth(t):
    m = re.search(r'[.!?]["”]?\s+(?=[A-Z"“])', t)
    return (t[:m.end()].strip(), t[m.end():].strip()) if m else (None, t)
cards = []
for s in subs:
    base = {'sub': s['sub'], 'ch': s['chapter'], 't': clean(s['title'])}
    cards.append(dict(base, id=f"ea-{s['sub']}", k='alert', b=clean(s['exam_alert'])))
    myth, corr = split_myth(clean(s['common_mistake']))
    cards.append(dict(base, id=f"cm-{s['sub']}", k='myth', f=myth, b=corr))
    cards.append(dict(base, id=f"ma-{s['sub']}", k='aid', b=clean(s['memory_aid'])))
    if s.get('quick_check'):
        cards.append(dict(base, id=f"qc-{s['sub']}", k='check', f=clean(s['quick_check']['q']), b=clean(s['quick_check']['a'])))
kc = {k: sum(c['k'] == k for c in cards) for k in ('alert', 'myth', 'aid', 'check')}
assert kc == {'alert': 50, 'myth': 50, 'aid': 50, 'check': 36}, kc
assert all(c['b'] for c in cards)

# ---- Reference data extracted from the book (each item carries its book location)
def opt(name):
    p = f'{R}/data/{name}'
    if not os.path.exists(p): return []
    items = json.load(open(p))
    for x in items: x.pop('quote', None); x.pop('quotes', None)   # proof quotes stay in data/ for the owner's records
    return items
signs = json.load(open(f'{R}/data/table_6_1.json'))
out = {'chapters': CH, 'bank': bank, 'sets': [s['questions'] for s in sel], 'diag': diag, 'diagBands': bands,
       'cards': cards, 'signs': signs['rows'], 'dragdrop': opt('dragdrop.json'), 'acronyms': opt('acronyms.json'),
       'keynums': opt('key_numbers.json'), 'checklist': opt('exam_checklist.json')}
json.dump(out, open(f'{R}/data/app_data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('cards', kc, 'dragdrop', len(out['dragdrop']), 'acronyms', len(out['acronyms']), 'keynums', len(out['keynums']), 'checklist', len(out['checklist']))
print('bank', len(bank), 'diag', len(diag), 'bytes', os.path.getsize(f'{R}/data/app_data.json'))
