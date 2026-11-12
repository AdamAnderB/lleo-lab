"""Validate every local HTML destination and asset, including project-path hosting."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit,unquote
root=Path(__file__).parent
errors=[]
class Check(HTMLParser):
 def handle_starttag(self,tag,attrs):
  d=dict(attrs)
  for attr in ('href','src'):
   u=d.get(attr,'');p=urlsplit(u)
   if not p.scheme and not p.netloc and p.path:
    if p.path.startswith('/'): errors.append(f'{self.file}: absolute path breaks project hosting: {u}')
    if not (self.file.parent/unquote(p.path)).exists(): errors.append(f'{self.file}: missing {u}')
  if tag=='img' and not d.get('alt'): errors.append(f'{self.file}: image needs alt')
for f in root.glob('*.html'):
 c=Check();c.file=f;c.feed(f.read_text())
 assert '<html lang="en">' in f.read_text()
if errors: raise SystemExit('\n'.join(errors))
print(f'PASS: {len(list(root.glob("*.html")))} pages; local links, assets, image alt text, and project-path compatibility')
