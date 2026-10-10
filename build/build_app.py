"""Embeds data/app_data.json into index.html between the APP_DATA markers."""
import os, re
R = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
html = open(f'{R}/index.html', encoding='utf-8').read()
data = open(f'{R}/data/app_data.json', encoding='utf-8').read().replace('</', '<\\/')
new = re.sub(r'/\*APP_DATA_START\*/.*?/\*APP_DATA_END\*/', lambda m: '/*APP_DATA_START*/' + data + '/*APP_DATA_END*/', html, flags=re.S)
assert new != html or '/*APP_DATA_START*/' + data in html
open(f'{R}/index.html', 'w', encoding='utf-8').write(new)
print('index.html', os.path.getsize(f'{R}/index.html'), 'bytes')
