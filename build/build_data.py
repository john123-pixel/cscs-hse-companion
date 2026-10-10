"""Builds data/app_data.json (the content embedded in index.html) from the extracted data.
Run:  python3 build/build_data.py   then   python3 build/build_app.py
"""
import json, os
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q = {q['id']: q for q in json.load(open(f'{R}/data/questions_all.json'))}
sel = json.load(open(f'{R}/data/selection_300.json'))['sets']
alt = json.load(open(f'{R}/data/image_alt.json'))
bands = json.load(open(f'{R}/data/diagnostic_score_bands.json'))['bands']
CH = {1:'Legal Responsibilities, Site Roles, and Documentation',2:'Risk Assessment',3:'Accidents and Fire',
      4:'Hazardous Substances, Noise, Vibration and Manual Handling',5:'Occupational Health and Welfare',6:'PPE and Signage',
      7:'Working at Height',8:'Excavations, Confined Spaces and Electrical',9:'Plant, Vehicles and Lifting',10:'Environmental Protection'}
def rec(q):
    L = 'ABCD'
    r = {'id': q['id'], 'ch': q['chapter'], 'ref': q['ref'], 'stem': q['stem'],
         'o': [q['options'][x] for x in L], 'c': L.index(q['correct_letter']),
         'why': [q['why_wrong'].get(x, '') if x != q['correct_letter'] else '' for x in L],
         'ex': q['explanation'], 'cm': q['common_mistake']}
    assert len(set(r['o'])) == 4 and all(r['why'][i] for i in range(4) if i != r['c']), q['id']
    if q['image']:
        r['img'] = f"images/q/{q['id']}.webp"; r['alt'] = alt[q['id']]
        assert os.path.exists(f"{R}/{r['img']}"), q['id']
    return r
bank = [rec(Q[i]) for s in sel for i in s['questions']]
diag = [rec(Q[f'diag-q{n}']) for n in range(1, 16)]
out = {'chapters': CH, 'bank': bank, 'sets': [s['questions'] for s in sel], 'diag': diag, 'diagBands': bands}
json.dump(out, open(f'{R}/data/app_data.json', 'w'), ensure_ascii=False, separators=(',', ':'))
print('bank', len(bank), 'diag', len(diag), 'bytes', os.path.getsize(f'{R}/data/app_data.json'))
