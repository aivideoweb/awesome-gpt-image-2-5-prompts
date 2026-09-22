#!/usr/bin/env python3
"""Keep the English and Chinese README galleries in sync with recipe sources."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED SHOWCASE -->'
END = '<!-- END GENERATED SHOWCASE -->'


def render(lang):
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    exported = json.loads((ROOT / 'data/prompts.json').read_text())
    assets = json.loads((ROOT / 'assets/manifest.json').read_text())['assets']
    latest = {a['recipe_id']: a for a in assets
              if a.get('role') not in ('input', 'draft') and a['recipe_id'] != 'COVER'}
    # P019's first edit matches the reusable recoloring prompt; the second edit changes text.
    latest['P019'] = next(a for a in assets if a['recipe_id'] == 'P019')
    byid = {r['id']: r for r in exported['core']}
    packs = [(p['slug'], p['title'].get(lang, p['title']['en']),
              [byid[r['id']] for r in p['recipes']]) for p in catalog['packs']]
    packs.append(('11-multilingual', '多语言海报' if lang == 'zh' else 'Multilingual posters', exported['localized']))
    packs.sort(key=lambda p: p[0])
    zh = lang == 'zh'
    lines = [START, '',
        '下面直接展示全部 16 个分类、106 条配方的图片。每类附一条完整提示词；点击其他图片可查看对应配方。'
        if zh else 'All 16 categories and 106 illustrated recipes are displayed below. Each category includes one complete prompt to copy; other images link to their full recipes.', '',
        '图片是项目生成示例，不代表 VideoWeb 或指定模型的实测结果。配方与实际执行提示词可能有差异，输入关系及已知问题见[图片生成记录](docs/generation-log.md)。修图配方需要上传参考图；多图任务需使用支持多图输入的工具。'
        if zh else 'These are project-generated examples, not verified VideoWeb or model-specific results. Reusable recipes may differ from executed prompts; see the [generation log](docs/generation-log.md) for inputs and known limitations. Editing recipes require references; use a tool supporting multiple uploads for multi-image tasks.', '']
    for slug, title, recipes in packs:
        lines += [f'<a id="showcase-{slug}"></a>', '', f'### {title} · {len(recipes)}', '', '| | | |', '| --- | --- | --- |']
        cells = []
        for r in recipes:
            name = r['title'].get(lang, r['title'].get('en')) if isinstance(r['title'], dict) else r['title']
            a = latest[r['id']]
            link = f'prompts/{slug}.md#{r["id"].lower()}'
            note = ('<br>修订后成图；完整过程见配方' if zh else '<br>Revised result; steps in recipe') if r['id'] in ('P031', 'P086') else ''
            cells.append(f'[![{name}]({a["path"]})]({link})<br>**[{r["id"]} · {name}]({link})**{note}')
        for i in range(0, len(cells), 3):
            lines.append('| ' + ' | '.join((cells[i:i+3] + [''] * 3)[:3]) + ' |')
        representative = {'06-brand-ui': 'P032', '15-x-community': 'P087'}
        locale = 'zh-Hans' if zh else 'en'
        r = next((r for r in recipes if r['id'] == representative.get(slug)
                  or r.get('language') == locale), recipes[0])
        # Editing examples expose their recorded input; generated recipes start from text.
        a = next(a for a in assets if a['recipe_id'] == r['id'] and a.get('role') not in ('input', 'draft'))
        p = r['prompt']
        chosen_lang = lang if isinstance(p, dict) and lang in p else 'en'
        prompt = p[chosen_lang] if isinstance(p, dict) else p
        lines += ['', f'**{"可直接复制" if zh else "Copy this prompt"} · {r["id"]}**', '']
        if isinstance(p, dict) and lang not in p:
            lines += ['此配方提供英文提示词，可直接复制使用。', '']
        if r.get('mode') == 'edit' and a['input_images']:
            lines += [('参考图（按顺序上传）：' if zh else 'References (upload in order): ') + ' · '.join(f'[{i+1}]({path})' for i, path in enumerate(a['input_images'])), '']
        else:
            lines += ['输入：此默认示例无需上传参考图。' if zh else 'Input: no reference upload is needed for this default example.', '']
        lines += ['```text', prompt, '```', '']
        for field, label in [('revision', '下一轮修改' if zh else 'Next edit'), ('review', '检查要点' if zh else 'Check the result')]:
            value = r.get(field, '')
            if isinstance(value, dict):
                value = value.get(lang, value.get('en', ''))
            if value:
                lines += [f'**{label}：** {value}', '']
        lines += [f'[{"本分类完整配方与使用说明" if zh else "All prompts and usage notes in this category"}](prompts/{slug}.md) · [{"回到分类目录" if zh else "Back to categories"}](#{"按实际工作选场景" if zh else "prompt-library"})', '']
    return '\n'.join(lines + [END])


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
    print('README showcases: 16 categories, 106 images and 16 complete prompts per language.')


if __name__ == '__main__':
    main()
