#!/usr/bin/env python3
"""Keep the English and Chinese README galleries in sync with recipe sources."""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
START = '<!-- BEGIN GENERATED SHOWCASE -->'
END = '<!-- END GENERATED SHOWCASE -->'


# The homepage directory preserves precise pack names rather than merging them.
USES = {
 '01-product': ('Catalog photos, skincare, cutaways, textures, gift boxes', '商品白底图、护肤静物、结构概念、材质特写、礼盒'),
 '02-social': ('Event posters, video thumbnails, carousels, podcast covers', '活动海报、视频缩略图、旅行轮播、播客封面'),
 '03-people-pets': ('Headshots, pet portraits, outfit try-ons, keepsakes', '职业头像、宠物写真、外套试穿、纪念插画'),
 '04-editing': ('Recolor, remove objects, relight, replace text, cut out', '换色、去杂物、改光线、替换文字、商品抠图'),
 '05-information': ('Explainers, charts, maps, plant cycles, workshop slides', '知识讲解、数据图、地图、植物周期、流程演示'),
 '06-brand-ui': ('Wordmarks, wayfinding, app screens, landing pages, packaging', '字标、导视、应用界面、落地页、包装系列'),
 '07-stories-games': ('Comics, character sheets, expressions, game icons, pixel art', '漫画、角色转面、表情表、游戏图标、像素场景'),
 '08-spaces': ('Rooms, material refreshes, shops, courtyards, sketch concepts', '室内空间、材质翻新、快闪店、庭院、草图效果图'),
 '09-publishing': ('Book covers, cookbook spreads, editorial art, zines', '书籍封面、食谱跨页、编辑插画、独立刊物'),
 '10-production': ('Seasonal variants, crop changes, localization, composites', '四季系列、横竖版适配、本地化、三图合成、老照修复'),
 '11-multilingual': ('12 language-specific posters, from English to Japanese and Arabic', '中、英、日、韩、西、法、德、葡、阿拉伯、印地、泰、俄'),
 '12-launch-examples': ('Before-and-after edits: outfits, duvet, text, itinerary, candles', '带前后对照的换装、被套换花色、改字、行程修改、蜡烛计数'),
 '13-customizable-studio': ('Adjustable portraits, coffee posters, packaging and miniatures', '可调整人物、配色与文案的工坊肖像、咖啡海报、包装、微缩景观'),
 '14-sketch-to-story': ('Sketch exploration, character styles, portrait edits, storyboards', '草图探索、角色风格、人像连续修改、品牌周边、故事分镜'),
 '15-x-community': ('Food lettering, fragrance boards, travel cards, architecture', 'X 来源的食材文字、香水分镜、旅行卡、建筑方案、邀请函'),
 '16-videoweb-x-creators': ('Fashion-film wardrobe, retro opening frames, headphone campaigns', 'VideoWeb 新增：时装短片服装、复古开场帧、耳机广告'),
}


def render(lang):
    zh = lang == 'zh'
    catalog = json.loads((ROOT / 'data/catalog.json').read_text())
    locales = json.loads((ROOT / 'data/locales.json').read_text())
    packs = {p['slug']: p for p in catalog['packs']}
    packs['11-multilingual'] = {'title': {'en': 'Multilingual posters', 'zh': '多语言海报'}, 'recipes': locales}
    lines = [START, '',
             '按具体任务查找。16 个场景包共 106 条配方；想先看效果，可浏览[完整图片画廊](docs/gallery.md)。'
             if zh else 'Find a specific task across 16 packs and 106 recipes. Prefer to choose by appearance? Open the [complete visual gallery](docs/gallery.md).', '',
             '| 场景包 | 可以做什么 | 配方数 |' if zh else '| Prompt pack | What you can make | Recipes |',
             '| --- | --- | --- |']
    for slug, pack in sorted(packs.items()):
        title = pack['title'].get(lang, pack['title']['en'])
        if slug == '14-sketch-to-story':
            english = sum(r.get('languages') == ['en'] for r in pack['recipes'])
            bilingual = sum(set(r.get('languages', ['en', 'zh'])) == {'en', 'zh'} for r in pack['recipes'])
            title = (f'从草图到故事（{english} 条英文、{bilingual} 条中英）' if zh
                     else f'Sketch-to-story ({english} English, {bilingual} English/Chinese)')
        lines.append(f'| [{title}](prompts/{slug}.md) | {USES[slug][1 if zh else 0]} | {len(pack["recipes"])} |')
    return '\n'.join(lines + ['', END])


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
    print('README directories: all 16 packs with concrete uses and current recipe counts.')


if __name__ == '__main__':
    main()
