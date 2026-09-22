# Source, credits and maintenance

This VideoWeb AI edition is adapted from [Flaq AI’s prompt library](https://github.com/flaqai/awesome-chatgpt-images-2-5-prompts), commit `0c74e035a713370217a1ecf29dd4a06edcc25fed`, retrieved 2026-09-22.

The baseline includes 103 recipes, 16 README entry languages and 139 PNG assets. Their original authorship, exact prompts, hashes, dates, reviews and third-party attributions are retained. The new VideoWeb cover is separate; inherited examples were not regenerated or independently tested on VideoWeb. The original cover remains in the archive for provenance.

VideoWeb AI maintains this edition. A brand change does not change the authorship of inherited recipes. Original Flaq AI copyright remains in the [MIT license](../LICENSE). X images and videos are external references, not MIT assets.

## Maintain the library

1. Edit `data/catalog.json` for authored recipes, `data/locales.json` for language-specific briefs and `data/x-sources.json` for X records.
2. Save exact executed prompts in `assets/generation/` and register generated PNGs in `assets/manifest.json`, with input order and honest visual review.
3. Run `python3 scripts/build_catalog.py`, `python3 scripts/build_gallery.py`, `python3 scripts/build_readme_showcase.py`, `python3 scripts/validate.py` and `git diff --check`.
4. Compare new upstream commits before importing. Preserve VideoWeb entry links and localization, original credits and asset hashes. Never replace checked dates with the current date unless the source was rechecked.
5. Review the English and Chinese reader journey and all language navigation. Submit changes with the [contribution guide](../CONTRIBUTING.md).

## 来源与维护

本分支基于 Flaq AI 源库，保留103条配方、16个语言入口和139张图片的原始记录。VideoWeb 负责本分支维护与新增内容，不把继承的图片写成本次重新生成或平台实测。修改数据后重新生成页面并运行检查；同步源库时保留品牌入口和原作者信息。
