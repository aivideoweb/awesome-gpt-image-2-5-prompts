#!/usr/bin/env python3
"""Validate recipe records, local Markdown links, exact-prompt records and images."""
import hashlib
import json
import re
import struct
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
def require(condition, message):
    if not condition:
        errors.append(message)
def read_json(path):
    return json.loads((ROOT/path).read_text(encoding='utf-8'))
def anchors(path):
    content=path.read_text(encoding='utf-8')
    found=set(re.findall(r'<a\s+id="([^"]+)"',content))
    counts={}
    for heading in re.findall(r'^#{1,6}\s+(.+)$',content,re.M):
        heading=re.sub(r'[^\w\- ]','',heading.strip().lower()).replace(' ','-')
        n=counts.get(heading,0); counts[heading]=n+1
        found.add(heading if n==0 else f'{heading}-{n}')
    return found

def main():
    catalog=read_json('data/catalog.json')
    locales=read_json('data/locales.json')
    exported=read_json('data/prompts.json')
    manifest=read_json('assets/manifest.json')['assets']
    recipes=[r for p in catalog['packs'] for r in p['recipes']]
    ids=[r['id'] for r in recipes+locales]
    require(len(ids)==len(set(ids)), 'Duplicate recipe IDs')
    require(len(recipes)==94 and len(locales)==12, 'Update documented recipe totals for this release')
    require(sum(r.get('languages')==['en'] for r in recipes)==16, 'Expected 16 English-only workflow recipes')
    require(len(catalog['packs'])==15, 'Expected 15 core packs')
    require(len({r['language'] for r in locales})==12, 'Expected 12 language briefs')
    require(len(exported['core'])==len(recipes), 'Exported core count mismatch')
    require(exported['localized']==locales, 'Stale localized export: rebuild catalog')
    byid={r['id']:r for r in exported['core']}
    sources=read_json('data/x-sources.json')['sources']
    require(len(sources)==9, 'Expected nine X source records')
    source_recipes={r['id']:r for r in recipes if r.get('source_reference')}
    require(set(source_recipes)=={s['id'] for s in sources}, 'X source-to-recipe mismatch')
    for source in sources:
        require(source_recipes[source['id']]['source_reference']==source, 'Stale X source metadata')
        require(re.fullmatch(r'https://x\.com/[A-Za-z0-9_]+/status/\d+',source['url']) is not None, 'Invalid X post URL')
        require(source['photo_url'].startswith(source['url']+'/photo/'), 'X photo belongs to a different post')
        require(urlsplit(source['image_url']).netloc=='pbs.twimg.com', 'Unexpected source image host')
        require(source['image_role']=='external-source-preview' and bool(source['rights']), 'Missing external image disclosure')
    for r in recipes:
        languages = r.get('languages', ['en','zh'])
        require(languages in [['en'], ['en','zh']], f'{r["id"]}: unsupported recipe languages')
        for field in ['title','brief','constraints','revision','review']:
            require(set(r[field])==set(languages),f'{r["id"]}: missing translation in {field}')
            require(all(r[field].values()),f'{r["id"]}: empty {field}')
        require(r['mode'] in ['edit','generate'],f'{r["id"]}: invalid mode')
        require(re.fullmatch(r'\d+:\d+',r['ratio']) is not None,f'{r["id"]}: invalid ratio')
        require(len(r['brief']['en'].split())>=35,f'{r["id"]}: brief too short')
        require('{{' not in r['brief']['en'],f'{r["id"]}: unresolved example placeholder')
        exported_r=byid.get(r['id'],{})
        for field in r:
            require(exported_r.get(field)==r[field],f'{r["id"]}: stale exported {field}')
        for lang in languages:
            require(r['brief'][lang] in exported_r.get('prompt',{}).get(lang,''),f'{r["id"]}: missing full prompt')
        for lang, prompt in r.get('compact_prompt',{}).items():
            require(lang in languages and 0 < len(prompt) <= 2000, f'{r["id"]}: compact prompt must fit the free tool')
            require(bool(r.get('compact_note')), f'{r["id"]}: missing compact-version status')
        for step in r.get('additional_edits',[]):
            require(step['anchor'].startswith(r['id'].lower()+'-'), f'{r["id"]}: additional edit anchor must name its recipe')
            require(bool(step['input']) and bool(step['title']) and bool(step['review']), f'{r["id"]}: additional edit needs input, title and review')
            require('en' in step['prompt'] and set(step['prompt']) <= {'en','zh'}, f'{r["id"]}: invalid additional edit languages')
            require(all(0 < len(text) <= 2000 for text in step['prompt'].values()), f'{r["id"]}: additional edit must fit the free tool')
    for pack in catalog['packs']:
        page = ROOT/'prompts'/f'{pack["slug"]}.md'
        targets = anchors(page)
        for r in pack['recipes']:
            for lang in r.get('languages',['en','zh']):
                require(f'{r["id"].lower()}-{lang}' in targets, f'{r["id"]}: missing direct prompt anchor')
            for step in r.get('additional_edits',[]):
                require(step['anchor'] in targets, f'{r["id"]}: missing additional edit anchor')
    for name, lang in [('README.md','en'),('README_zh.md','zh')]:
        text = (ROOT/name).read_text()
        for recipe in ['p002','p084','p094']:
            require(f'#{recipe}-{lang})' in text, f'{name}: featured prompt must open its execution language')
    require(len(manifest)==145,'Expected 145 recorded images')
    covered={a['recipe_id'] for a in manifest if a.get('role') not in ('input','draft')}
    require(set(ids).issubset(covered), 'Every recipe must have a generated result')
    require({a['path'] for a in manifest}=={str(p.relative_to(ROOT)) for p in (ROOT/'assets/images').glob('*.png')}, 'Unrecorded or missing PNG files')
    require(len({a['path'] for a in manifest})==len(manifest),'Duplicate image records')
    for a in manifest:
        path=ROOT/a['path']
        require(path.is_file(),f'Missing image: {path}')
        if not path.is_file(): continue
        data=path.read_bytes()
        require(data.startswith(b'\x89PNG\r\n\x1a\n'),f'Invalid PNG: {path}')
        require(struct.unpack('>II',data[16:24])==(a['width'],a['height']),f'Dimension mismatch: {path}')
        require(hashlib.sha256(data).hexdigest()==a['sha256'],f'Hash mismatch: {path}')
        require(a['recipe_id'] in ids+['COVER'],f'Unknown recipe: {a["recipe_id"]}')
        prompt=ROOT/a['prompt_path']
        require(prompt.is_file() and prompt.stat().st_size>100,f'Missing exact prompt: {prompt}')
        require(bool(a['review']),f'Missing review: {path}')
        require(a['model_id'] is None, f'Unexpected model claim: {path}')
        for source in a['input_images']:
            require((ROOT/source).is_file(),f'Missing image input: {source}')
    files=list(ROOT.rglob('*.md'))
    link_count=0
    for path in files:
        if '.git' in path.parts: continue
        content=path.read_text(encoding='utf-8')
        require(content.count('```')%2==0,f'Unclosed code fence: {path}')
        # Remove fenced examples before checking document links.
        content=re.sub(r'```.*?```','',content,flags=re.S)
        targets = re.findall(r'!?\[[^\]]*\]\(([^\s)]+)(?:\s+"[^"]*")?\)', content)
        targets += re.findall(r'(?:src|href)="([^"]+)"', content)
        for target in targets:
            target=target.strip('<>')
            parsed=urlsplit(target)
            if parsed.scheme or parsed.netloc: continue
            link_count+=1
            dest=(path.parent/unquote(parsed.path)).resolve() if parsed.path else path
            require(dest.exists(),f'Broken link in {path.relative_to(ROOT)}: {target}')
            if dest.is_file() and dest.suffix=='.md' and parsed.fragment:
                require(unquote(parsed.fragment) in anchors(dest),f'Broken anchor in {path.relative_to(ROOT)}: {target}')
    # Readers must be able to find every pack in both full overview tables.
    for name, heading in [('README.md', '## Prompt library'), ('README_zh.md', '## 按实际工作选场景')]:
        overview = (ROOT / name).read_text().split(heading, 1)[1].split('\n## ', 1)[0]
        for pack in catalog['packs']:
            require(f'prompts/{pack["slug"]}.md' in overview, f'{name}: pack missing from overview table: {pack["slug"]}')
    from build_readme_showcase import START, END, render
    for name, lang in [('README.md', 'en'), ('README_zh.md', 'zh')]:
        text = (ROOT / name).read_text()
        require(START in text and END in text, f'{name}: missing inline showcase')
        if START in text and END in text:
            block = START + text.split(START, 1)[1].split(END, 1)[0] + END
            require(block == render(lang), f'{name}: stale inline showcase')
            require(block.count('](prompts/') == 16 and block.count('```text') == 0,
                    f'{name}: expected all 16 precise categories in the directory')
            require(len(re.findall(r'!\[', block)) == 0,
                    f'{name}: directory should remain a compact lookup table')
    readmes = read_json('data/readme-locales.json')['versions']
    require(len(readmes) == 16, 'Expected 16 README entry languages')
    for entry in readmes:
        page = ROOT / entry['path']
        require(page.is_file(), f'Missing language entry: {page}')
        if not page.is_file():
            continue
        text = page.read_text()
        tool_base = 'https://videoweb.ai/cn/' if page.name == 'README_zh.md' else 'https://videoweb.ai/'
        for url in [tool_base + 'model/gpt-image-2-5/', tool_base + 'free-gpt-image-2-5/', 'https://videoweb.ai/affiliate-program/']:
            require(url in text, f'{page.name}: missing VideoWeb entry {url}')
        if page.name not in ('README.md', 'README_zh.md'):
            require('assets/images/videoweb-cover.png' in text, f'{page.name}: missing brand cover')
        require(str(len(ids)) in text, f'{page.name}: missing current recipe total')
        if entry['path'] in [f'README_{lang}.md' for lang in ['de','hi','id','it','ko','pt','ru','th','tw','vi']]:
            require(str(len(catalog['packs']) + 1) in text.splitlines()[8] and '15' not in text.splitlines()[8], f'{page.name}: stale pack total')
    for video in read_json('data/video-sources.json')['videos']:
        require(video['source_url'].startswith('https://x.com/'), 'Video source must identify its original X post')
        require(urlsplit(video['media_url']).netloc == 'video.twimg.com', 'Unexpected video host')
        require(bool(video['rights']) and bool(video['verification']), 'Missing video rights or access notes')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'PASS: {len(ids)} recipes, 12 languages, {len(manifest)} PNGs, {len(files)} Markdown files, {link_count} local links.')

if __name__=='__main__':
    main()
