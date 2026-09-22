#!/usr/bin/env python3
"""Render bilingual Markdown and machine-readable full prompts from authored data."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
CTA = '[Use GPT Image 2.5 / 开始创作](https://videoweb.ai/model/gpt-image-2-5/) · [Free, no signup / 免注册体验](https://videoweb.ai/free-gpt-image-2-5/)'
def build():
    data = json.loads((ROOT/'data/catalog.json').read_text())
    manifest = json.loads((ROOT/'assets/manifest.json').read_text())
    examples = {}
    core_count = sum(len(pack['recipes']) for pack in data['packs'])
    bilingual_count = sum('zh' in r['brief'] for p in data['packs'] for r in p['recipes'])
    english_only_count = core_count - bilingual_count
    for asset in manifest['assets']:
        if asset.get('role') not in ('input', 'draft'):
            examples.setdefault(asset['recipe_id'], []).append(asset)
    index = ['# Prompt index · 提示词索引', '', '[English](../README.md) · [简体中文](../README_zh.md)', '', CTA, '',
             f'{bilingual_count} bilingual recipes + {english_only_count} English-only workflow recipes + 12 language-specific recipes. Translations and follow-ups are not counted as separate recipes.', '',
             f'{bilingual_count} 条中英双语配方 + {english_only_count} 条英文工作流配方 + 12 条语言专用配方；翻译和后续修改不重复计数。', '',
             '| ID | English | 中文 | Mode | Ratio |', '| --- | --- | --- | --- | --- |']
    full=[]
    for pack in data['packs']:
        lines=[f'# {pack["title"]["en"]} · {pack["title"]["zh"]}', '', '[All recipes / 全部配方](README.md)', '', CTA, '',
               f'Images 2.5 workflow focus: **{pack["focus"]}**.', '',
               'Copy one language block. For edits, attach the images named in the prompt in that order. Requested ratios are creative targets; verify actual output dimensions.', '',
               '任选一种语言复制。编辑任务须按提示顺序附参考图；比例为创作目标，输出后核对实际尺寸。', '']
        if pack.get('source_url'):
            source_label = pack.get('source_label', 'OpenAI launch article')
            guide = pack.get('guide', 'launch-examples.md')
            lines += [f'Scenario inspiration: [{source_label}]({pack["source_url"]}). Briefs adapted and expanded by flaq.ai; each entry discloses whether an image has been generated. [Example guide](../docs/{guide}).', '']
        lines += [f'- [{r["id"]} · {r["title"]["en"]}](#{r["id"].lower()})' for r in pack['recipes']]
        for r in pack['recipes']:
            languages = r.get('languages', ['en', 'zh'])
            translated_title = ' / '+r['title']['zh'] if 'zh' in languages else ''
            chinese_link = f'[{r["title"]["zh"]}]({pack["slug"]}.md#{r["id"].lower()}-zh)' if 'zh' in languages else 'English workflow'
            index.append(f'| {r["id"]} | [{r["title"]["en"]}]({pack["slug"]}.md#{r["id"].lower()}-en) | {chinese_link} | {r["mode"]} | {r["ratio"]} |')
            lines += ['', f'<a id="{r["id"].lower()}"></a>', f'## {r["id"]} · {r["title"]["en"]}{translated_title}', '',
                      f'**Mode:** {r["mode"]} · **Target:** {r["ratio"]} · **Author:** {r.get("author", "flaq.ai team")}', '']
            direct = [f'[{label}](#{r["id"].lower()}-{lang})' for lang,label in [('en','English prompt'),('zh','中文提示词')] if lang in languages]
            if r.get('compact_prompt'):
                direct += [f'[Free-tool version / 免费工具版](#{r["id"].lower()}-en-compact)']
            direct += [f'[{step["title"]}](#{step["anchor"]})' for step in r.get('additional_edits',[])]
            lines += ['**Copy prompt / 复制提示词：** ' + ' · '.join(direct), '']
            if languages == ['en']:
                lines += ['**Language:** English. Expanded adaptation; see the result status and source information below.', '']
            if r.get('usage'):
                u = r['usage']
                lines += [f'**Best for:** {u["best_for"]}', '', f'**Inputs:** {u["inputs"]}', '',
                          f'**Production check:** {u["review_workflow"]} {u["delivery"]}', '']
            if r.get('source_reference'):
                s = r['source_reference']
                lines += [f'**Scenario source:** [{s["author"]} ({s["handle"]}) on X]({s["url"]}) · Published {s["published"]} · Checked {s["checked"]}.', '',
                          f'**Source idea:** {s["source_summary"]}', '',
                          f'**Source access:** {s.get("verification", "Inherited upstream source record; checked on the date above.")}', '',
                          f'**What changed:** {s["adaptation"]}', '',
                          f'[![External source preview for {r["id"]}: {s["source_summary"]}]({s["image_url"]})]({s["photo_url"]})', '',
                          f'**External reference image:** [View the original photo on X]({s["photo_url"]}). This is the source author’s image, not a rendering of the adapted prompt below. It is hosted remotely and is outside this repository’s MIT license. The model attribution is the author’s claim, not an independent verification. [Curation notes](../docs/x-community.md).', '']
            if r.get('source_reference', {}).get('prompt_url'):
                lines += [f'**Original prompt reply:** [Read the author’s prompt]({r["source_reference"]["prompt_url"]}).', '']
            if r['id'] in examples:
                lines += ['**Generated example / 已生成示例：** Exact executed prompts and review notes are in the [generation log](../docs/generation-log.md). These examples do not verify every template variation.', '']
                for a in examples[r['id']]:
                    if a.get('role') == 'input':
                        continue
                    if a.get('input_images'):
                        lines += ['**Example inputs, in order / 示例输入顺序：**', '']
                        for n, source_path in enumerate(a['input_images'], 1):
                            lines += [f'[Input {n} / 输入 {n}](../{source_path})', '']
                    lines += [f'![{a["alt"]}](../{a["path"]})', '', f'[{a["label"]}: exact prompt / 实际提示词](../{a["prompt_path"]})', '', f'**Observed review:** {a["review"]}', '']
            else:
                lines += ['**Status / 状态：** Authored template; not rendered in this release / 已编写，当前版本尚未生成实测图。', '']
            if r.get('adjustments'):
                lines += ['### Customize / 微调参数', '',
                          'Use the complete prompt below as a working default. Replace the named detail in that prompt; do not append a conflicting value. Adjust one item at a time. / 下方是可直接使用的默认配方；修改时替换对应描述，不要追加冲突条件，每次先调整一项。', '',
                          '| Parameter / 参数 | Current example / 当前值 | Try instead / 可改为 | Preserve / 保留 |',
                          '| --- | --- | --- | --- |']
                for a in r['adjustments']:
                    lines.append('| ' + ' | '.join(a[k]['en']+' / '+a[k]['zh'] for k in ['name','default','options','preserve']) + ' |')
                lines += ['']
            if r.get('customization'):
                c = r['customization']
                lines += ['### Customize', '', f'**{c["parameter"]}:** {c["default"]}. **Alternatives:** {c["alternatives"]}. **Preserve:** {c["preserve"]}.', '']
            complete={}
            for lang,label in [('en','English'),('zh','简体中文')]:
                if lang not in languages:
                    continue
                if lang=='en':
                    text=f'Asset: {r["title"][lang]}. Target aspect ratio: {r["ratio"]}. Mode: {r["mode"]}.\n'+r['brief'][lang]+'\nConstraints: '+r['constraints'][lang]+'\nRender only explicitly requested image text. Do not add unrelated logos, signatures or captions.'
                else:
                    text=f'交付物：{r["title"][lang]}。目标比例：{r["ratio"]}。模式：'+('新建' if r['mode']=='generate' else '编辑')+'。\n'+r['brief'][lang]+'\n约束：'+r['constraints'][lang]+'\n只渲染明确要求的图中文字，不添加无关标识、签名或说明。'
                complete[lang]=text
                lines += [f'<a id="{r["id"].lower()}-{lang}"></a>', f'### {label}', '']
                if r['mode'] == 'generate':
                    lines += ['No reference upload required. / 无需上传参考图。', '']
                else:
                    inputs = next((a['input_images'] for a in examples.get(r['id'],[]) if a.get('input_images')), [])
                    input_links = ' → '.join(f'[Input {n} / 输入 {n}](../{path})' for n,path in enumerate(inputs,1))
                    lines += ['Attach the references specified below before running. / 执行前先附下方提示词要求的参考图。' + (f' Example inputs, in order / 示例输入顺序：{input_links}。' if inputs else ''), '']
                if lang == 'zh' and r.get('translation_note'):
                    lines += [r['translation_note'], '']
                if len(text) > 2000:
                    route = f'[Use the compact version / 使用精简版](#{r["id"].lower()}-{lang}-compact).' if lang in r.get('compact_prompt',{}) else 'Use a tool that accepts this length. / 请选用支持此长度的工具。'
                    lines += [f'This full prompt has {len(text):,} characters, above the free page’s 2,000-character limit. / 此完整版超过免费页的 2,000 字符限制。 {route}', '']
                lines += ['```text',text,'```','']
                if lang in r.get('compact_prompt',{}):
                    compact = r['compact_prompt'][lang]
                    lines += [f'<a id="{r["id"].lower()}-{lang}-compact"></a>', '### Free-tool version / 免费工具版', '',
                              f'{len(compact):,} characters / 字符 · No reference upload / 无需上传参考图。', '', r['compact_note'], '',
                              'Copy this block alone into the [free tool](https://videoweb.ai/free-gpt-image-2-5/). / 只复制本段到[免费工具](https://videoweb.ai/free-gpt-image-2-5/)，不要再拼接上方完整版。', '',
                              '```text', compact, '```', '']
            lines += ['### Next edit / 后续修改', '']
            if r.get('revision_input'):
                lines += [r['revision_input'], '']
            lines += ['```text', r['revision']['en'], '```', '']
            if 'zh' in languages:
                lines += ['```text', r['revision']['zh'], '```', '']
            lines += ['**Review / 验收：** '+r['review']['en']+' '+r['review'].get('zh',''), '']
            for step in r.get('additional_edits',[]):
                lines += [f'<a id="{step["anchor"]}"></a>', f'### {step["title"]}', '', step['input'], '',
                          'VideoWeb workflow instruction; not rendered. / VideoWeb 补充的操作指令，尚未生成实测图。', '']
                for lang,label in [('en','English'),('zh','简体中文')]:
                    if lang in step['prompt']:
                        lines += [f'**{label}**', '', '```text', step['prompt'][lang], '```', '']
                lines += ['**Review / 验收：** '+step['review'], '']
            lines += ['[Back to index / 返回索引](README.md)', '']
            full.append({**r,'pack':pack['slug'],'prompt':complete,'examples':[a['path'] for a in examples.get(r['id'],[])]})
        (ROOT/'prompts'/f'{pack["slug"]}.md').write_text('\n'.join(line.rstrip() for line in lines).rstrip()+'\n')
    locales=json.loads((ROOT/'data/locales.json').read_text())
    localized=['# Multilingual image prompts · 多语言图像提示词', '', '[All recipes / 全部配方](README.md)', '', CTA, '',
        '12 complete localized briefs. These are language-specific recipes, not full translations of the entire library. Generated lettering requires fluent review before publication; see each example and its review record.', '',
        '12 条完整本地语言创作简报，不代表全库已翻译为12种语言。配图中的文字需由熟练读者审校；具体结果参见各示例及审查记录。', '']
    for r in locales:
        index.append(f'| {r["id"]} | [{r["title"]}](11-multilingual.md#{r["id"].lower()}) | {r["language"]} | generate | 2:3 |')
        localized += [f'<a id="{r["id"].lower()}"></a>',f'## {r["id"]} · {r["title"]}', '', '```text',r['prompt'],'```','', '**Review:** '+r['review'],'']
        if r.get('revision'):
            localized += ['### Next edit / 后续修改', '', 'Run this only after reviewing the first result / 首次结果审查后再单独执行。', '', '```text', r['revision'], '```', '']
        for a in examples.get(r['id'],[]):
            localized += [f'![{a["alt"]}](../{a["path"]})','',f'[Exact generation prompt / 实际生成提示词](../{a["prompt_path"]})','',f'**Observed review:** {a["review"]}','']
    (ROOT/'prompts/11-multilingual.md').write_text('\n'.join(line.rstrip() for line in localized).rstrip()+'\n')
    (ROOT/'prompts/README.md').write_text('\n'.join(index)+'\n')
    (ROOT/'data/prompts.json').write_text(json.dumps({'core':full,'localized':locales},ensure_ascii=False,indent=2)+'\n')
    print(f'Rendered {len(full)} core recipes and {len(locales)} localized recipes.')
if __name__=='__main__':
    build()
