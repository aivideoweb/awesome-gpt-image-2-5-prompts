#!/usr/bin/env python3
"""Keep the English and Chinese README galleries in sync with recipe sources."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED SHOWCASE -->'
END = '<!-- END GENERATED SHOWCASE -->'


# Reader tasks, deliberately separate from the chronological source packs.
GROUPS = [
    ('products', 'Products & brand design', '商品与品牌',
     'Create catalog photos, packaging and a consistent brand look.', '制作商品图、包装和品牌视觉。',
     ['P002', 'P003', 'P035'], ['01-product', '06-brand-ui', '13-customizable-studio']),
    ('posters', 'Posters, covers & publishing', '海报、封面与出版',
     'Give a message a clear visual hierarchy, including multilingual copy.', '让活动、视频和书籍的标题与画面一眼可读，也支持多语言文案。',
     ['P008', 'L003', 'P049'], ['02-social', '09-publishing', '11-multilingual']),
    ('people', 'Portraits, outfits & pets', '人像、穿搭与宠物',
     'Explore a look or edit a portrait while preserving recognizable features.', '探索服装造型，或在修图时保留人物和宠物的特征。',
     ['P013', 'P014', 'P092'], ['03-people-pets']),
    ('editing', 'Change one thing at a time', '局部修改与系列延展',
     'Change clothing, patterns or text while keeping the approved composition.', '保留已确认的画面，只换服装、花色、文字，或制作同系列图片。',
     ['P061', 'P063', 'P066'], ['04-editing', '10-production', '12-launch-examples']),
    ('information', 'Explain an idea', '知识讲解与信息图',
     'Turn a process, concept or supplied data into a visual explanation.', '把步骤、知识和给定数据整理成易懂的图示。',
     ['P025', 'P027', 'P030'], ['05-information']),
    ('spaces', 'Rooms & architecture', '室内与建筑',
     'Explore room layouts, materials and concepts from sketches.', '从空间照片或草图出发，探索家具、材质与建筑方案。',
     ['P043', 'P044', 'P048'], ['08-spaces']),
    ('stories', 'Stories & video planning', '故事、分镜与视频前期',
     'Plan characters, shot sequences and product films as still images.', '用静态图设计角色、镜头顺序和产品短片。分镜图本身不是视频。',
     ['P037', 'P084', 'P087'], ['07-stories-games', '14-sketch-to-story', '15-x-community', '16-videoweb-x-creators']),
]


def render(lang):
    zh = lang == 'zh'
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    exported = json.loads((ROOT / 'data/prompts.json').read_text())
    assets = json.loads((ROOT / 'assets/manifest.json').read_text())['assets']
    latest = {a['recipe_id']: a for a in assets
              if a.get('role') not in ('input', 'draft') and a['recipe_id'] != 'COVER'}
    byid = {r['id']: r for r in exported['core'] + exported['localized']}
    packs = {p['slug']: p for p in catalog['packs']}
    packs['11-multilingual'] = {'title': {'en': 'Multilingual posters', 'zh': '多语言海报'}, 'recipes': exported['localized']}
    lines = [START, '',
             '先按用途看代表案例，再打开需要的配方。首页精选 21 例；全部 106 例见[完整画廊](docs/gallery.md)。'
             if zh else 'Find your task, preview an example, then open its recipe. These 21 selections introduce the [full gallery of 106 recipes](docs/gallery.md).', '',
             ' · '.join(f'[{g[2] if zh else g[1]}](#browse-{g[0]})' for g in GROUPS), '']
    for key, en, cn, desc_en, desc_cn, ids, slugs in GROUPS:
        lines += [f'<a id="browse-{key}"></a>', '', f'### {cn if zh else en}', '', desc_cn if zh else desc_en, '']
        headings, cells, modes = [], [], []
        for id in ids:
            r = byid[id];a = latest[id]
            title = r['title'].get(lang, r['title']['en']) if isinstance(r['title'], dict) else r['title']
            if zh:
                title = {'L003': '日文烘焙店海报', 'P084': '九镜头音乐短片分镜', 'P087': '六画面香水发布分镜'}.get(id, title)
            slug = r.get('pack', '11-multilingual')
            link = f'prompts/{slug}.md#{id.lower()}'
            mode = ('需参考图' if zh else 'Reference needed') if r.get('mode') == 'edit' else ('文字生图' if zh else 'Text to image')
            if r.get('mode') != 'edit' and a['input_images']:
                mode += ' · 含后续修订' if zh else ' · Refined result'
            headings.append(f'[{title}]({link})')
            cells.append(f'[![{title}]({a["path"]})]({link})')
            modes.append(mode)
        lines += ['| ' + ' | '.join(headings) + ' |', '| --- | --- | --- |',
                  '| ' + ' | '.join(cells) + ' |', '| ' + ' | '.join(modes) + ' |', '',
                  ('更多配方：' if zh else 'More recipes: ') + ' · '.join(
                      f'[{packs[slug]["title"].get(lang, packs[slug]["title"]["en"])} ({len(packs[slug]["recipes"])})](prompts/{slug}.md)' for slug in slugs), '']
    lines += [END]
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    for filename, lang in [('README.md', 'en'), ('README_zh.md', 'zh')]:
        path = ROOT / filename
        old = path.read_text()
        block = render(lang)
        if START not in old or END not in old:
            raise SystemExit(f'Missing showcase markers: {filename}')
        new = re.sub(re.escape(START) + '.*?' + re.escape(END), lambda _: block, old, flags=re.S)
        if args.check and new != old:
            raise SystemExit(f'Stale showcase: {filename}')
        if not args.check:
            path.write_text(new)
    print('README showcases: 7 reader tasks and 21 selected examples per language.')


if __name__ == '__main__':
    main()
