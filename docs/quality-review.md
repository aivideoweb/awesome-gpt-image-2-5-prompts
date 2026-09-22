# Reader-focused comparison · 2026-09-22

**Current homepage:** a short introduction, two-column campaign and storyboard examples, a separate product-photo input/result pair, text/reference starting paths, the full 16-pack directory, two-column poster/portrait and character/interior examples, and single- and multi-step editing comparisons. The full 106-recipe gallery remains available. The chronological review notes below describe earlier versions.

Baseline: [Flaq AI source](https://github.com/flaqai/awesome-chatgpt-images-2-5-prompts), commit `0c74e035a713370217a1ecf29dd4a06edcc25fed`.

## Review rounds

A Sol reviewer with high reasoning reviewed the VideoWeb edition from an external reader’s perspective in three rounds. The primary editor made all changes.

- Round 1: fixed current-maintainer wording, cover alternative text, deep-page tool links, contribution-guide branding and social-preview path.
- Round 2: aligned localized pack counts, video resolution and observation scope, removed redundant source-record copies, and improved new-image alternative text.
- Round 3: verified those issues closed; no remaining material issue in the reviewed adaptation and additions prevented source-level coverage and usability.

After the review rounds, the primary editor independently compared the source and target. The original 14 core packs, 12 language-specific recipes, 139 asset records, image bytes and exact-prompt bytes were preserved. English and Chinese navigation were compared, the historical playbook count was clarified, and the publishing-notes link was restored. Both the source Flaq AI and target aivideoweb copyright notices remain in the MIT license. GitHub Markdown rendering was inspected for the cover and overview table.

## Result and limits

The edition includes 106 illustrated recipes in 16 packs, 16 README language entries and 145 PNG records. Three new bilingual X-inspired creator briefs and six images extend the source; a linked official video and separate motion-planning guide support video creators.

Catalog and gallery generation are reproducible. The validator checks recipe exports, image hashes and dimensions, local links, multilingual entry points and source records. Continuous integration rebuilds and rejects stale generated files.

This is a content and repository review. It does not verify VideoWeb uptime or actual generation/download, every model capability, native-language fluency, full video content or every suggested edit. Native X required login/returned 403; new source records disclose public-mirror access. New images use the built-in image tool without a returned model ID. These boundaries are visible to readers.

## 中文

完成三轮 Sol 高推理复查后，主编辑再次独立对比源库，确认原始103条配方及139张图的原始数据与文件完整保留，并修复历史数量表述和维护入口遗漏。当前版本在源库基础上新增3条中英配方、4张图、视频来源导览和图片转视频说明。

这次结论针对内容覆盖、读者操作路径和仓库可维护性，不等于平台生图或模型效果实测。复古开场图留白等已知缺陷仍如实记录，不隐藏失败，也不把建议中的后续操作写成已完成。

## Homepage expansion follow-up

Reader feedback requested that categories and examples be visible without opening separate documents. The English and Simplified Chinese READMEs now display all 16 categories and 106 recipe previews, with one complete prompt per category and in-page navigation. Detailed recipes and generation records remain available.

The Sol reviewer identified a Chinese locale-code mismatch and three preview-to-prompt mismatches. The editor mapped Chinese to `zh-Hans`, selected the first recoloring result for P019, and chose single-pass P032 and P087 as the copyable examples. P031 and P086 previews explicitly identify their revised results. README generation is included in CI and checked against the source data.

The previews use the original PNG files (about 221 MiB in total before browser caching or GitHub processing). This change improves browsing coverage; it does not establish fast loading on mobile connections. Original full-resolution assets and generation provenance remain intact.

The Sol follow-up confirmed both findings closed. The primary editor then independently rechecked all 106 unique homepage previews, representative prompts, source asset bytes, category navigation and the final affiliate section. No further issue in the requested homepage expansion remained.

## Reader-order revision

The previous all-image homepage was rejected by the reader as cluttered. Both main READMEs now follow a single sequence: choose a task, inspect selected examples, follow one complete edit, then explore deeper guides. Seven task groups replace the 16 chronological pack sections; each group has three visible examples and links to its related packs. Long prompts no longer interrupt the gallery. A three-image lamp case provides two copyable edits in the correct input order. Duplicate update announcements were removed and the detailed tool comparison moved to `docs/tools.md`.

Sol high-reasoning review checked the task grouping, input labels, edit sequence and retained coverage, and reported no mandatory correction. The primary editor independently compared the reader path with the source, checked all 16 pack entrances, and confirmed that recipe data, the full gallery and image records were unchanged. GitHub Markdown rendering was used to inspect title, image and input rows. This review addresses structure and usability; it is not a claim that every reader preference or mobile-network condition has been tested.

## Restoring example value and precise discovery

A direct comparison with the source identified gaps hidden by the earlier structural pass: the short homepage explained too little about who the library serves, why each example matters, how to start from text, and what an edit actually changes. Those findings were addressed in both main READMEs. Three lead examples explain copy space, character styles and shot continuity; the starter prompt appears before the full 16-pack directory. A second visual group covers posters, portraits and spaces. Candle and lamp comparisons show single-step and successive edits, with their recorded limitations.

The Sol reviewer rechecked these reader paths against the source and the asset records, with no required correction. Its wording suggestion changed “Text only” to “Text-to-image; no reference needed.” The primary editor independently rechecked the requested use cases and source coverage after review. Recipe data, all generated images and the complete gallery remain unchanged. Content checks verify preservation and links; this review does not substitute for reader feedback or a real model-generation test.

## Execution and localized-entry follow-up

A fresh Sol high-reasoning review found five concrete reader obstacles: P077 exceeded the promoted free tool’s prompt length, homepage prompt links stopped above long examples, two lead examples lacked Chinese execution text, localized entry pages retained long tool tables, and several usage or review notes were unrelated to their task.

P077 now includes a separately labeled 1,823-character compact version alongside the unchanged 2,979-character full prompt. Both retain the supplied product copy; the compact wording has not been rendered. Recipe headers and the English/Chinese index link directly to language blocks, with reference inputs beside the text. P076 and P084 have new Chinese execution translations, clearly marked as not separately rendered. The current count is 78 bilingual, 16 English-only and 12 language-specific recipes. Task-specific usage and review notes replace the identified contradictions.

A Sol high-reasoning editing agent shortened the 14 other README entry pages: generation and the following edit are separate code blocks, task links replace the long tool table, and the complete comparison remains in the linked guide. The original prompt wording is preserved across those two steps. The main homepage’s categories, visible examples and editing comparisons remain in place.

The critical Sol reviewer rechecked the final files and confirmed all five findings closed. After that review, the primary editor independently compared the source README and the final reader journey: task discovery, visible examples, copying a prompt, supplying inputs, applying a separate edit, and reaching video, maintenance and affiliate guidance. No further material correction was identified in that scope. Both main READMEs retain all 16 category entrances and 12 inline images. All 91 upstream core English prompts, 12 localized recipes, 139 image files and their exact execution prompts remain unchanged. The source main commit was rechecked against the baseline above.

GitHub Markdown rendering was inspected for the Chinese prompt landing and the Japanese generation/edit path. The three generators and content validator pass, including 106 recipes, 143 image hashes and 2,389 local links. These checks do not establish new image-generation results or independent native-language editorial review.

## Workflow continuity review

A further Sol high-reasoning critique found three inherited execution gaps and one missing VideoWeb handoff: the playbook linked a human courier to robot-specific story prompts, its ceramics wordmark led to another brand’s tea cartons, P080 combined two approval stages in one block, and the P087 video route lacked a standalone-frame instruction.

The editor added complete playbook bridge prompts with explicit approved inputs, retaining the courier throughout the story and SOFT KILN across ceramics packaging. P080 now keeps grading and background snow in separate blocks; its first-generation prompt and all executed records are unchanged. P087 has a bilingual shot-01 expansion linked from both video guides. Each additional step has its own input and review criteria. All new bridge and expansion instructions are labeled unrendered and do not increase the 106-recipe total.

The reviewer accepted three repairs but found that the brand practice link still selected the P031 draft. The editor independently checked the manifest, accepted that finding and linked the corrected `example-p031-v2.png` result. The reviewer confirmed that final issue closed. The editor also moved the original six-panel review above the new P087 single-frame step and supplied a separate one-bottle review, so readers do not apply the wrong checklist.

After the reviewer’s final response, the editor independently checked the input-to-output sequence, copyable blocks, source preservation and example states. All 91 source core generation prompts in English, 12 localized recipes, 139 PNGs and their exact execution prompts remain intact. The reusable P080 follow-up is intentionally split; source preservation is not a claim that its old combined follow-up remains the recommended instruction. GitHub Markdown output was checked for code-block separation and the new anchors. The three generators and validator pass with 106 recipes, 143 images and 2,397 local links. No additional material correction was identified in the four reviewed workflows; the new instructions have not been executed as image or video generations.


## Homepage entry review

The English and Simplified Chinese homepages now bring real examples forward without the large decorative cover. The asset remains in the repository. P002 replaces P076 in the lead group, showing the recorded kitchen-table input beside its white-background output; P076 remains accessible through its pack and the complete gallery. The three lead cases cover a new concept, an existing product photo and a performer storyboard. Their image and text links go directly to the appropriate execution language, where required input links are available.

The starting instructions distinguish text generation from existing-product editing and tell readers to replace cup-specific details before using another product photo. The Chinese tool links use the Chinese pages. The sketch-to-story directory entry reports its English-only and English/Chinese counts from catalog data. Existing candle and lamp comparisons, all 16 pack entrances, provenance, affiliate and license sections remain available.

Sol high-reasoning review found no required correction after checking the input/result records, language anchors and tool-page content. The editor accepted its optional link-consistency suggestion and aligned all three image targets with their prompt links. During GitHub Markdown rendering with a local preview stylesheet, fixed-width cup thumbnails wrapped; percentage widths corrected the inspected desktop layout. This preview is not a mobile or production conversion test.

The primary editor independently compared both homepages and the source reader journey after the review. No additional material obstacle was found in choosing a task, finding an input, copying a prompt or continuing an edit. The upstream main still matches the baseline above. All 139 source images and their exact generation-prompt files remain byte-identical; no recipe, image or execution record changed in this round.


## Source-inspired image layout

A direct comparison of the rendered GitHub pages found that the compact three-column layout made the examples harder to inspect than the source’s two-column galleries. Passing link checks and completing a reader path had not established visual parity. Both main READMEs now use two columns for independent examples and input/result pairs; only the three-stage lamp sequence keeps three columns. Short titles, one-line task/input captions and prompt links replace the longer table text. Review notes remain beside their image groups.

P002 now has a separate input/result table. The existing P076 image returns in the broader gallery alongside the interior concept, so the poster and portrait can form a second two-column pair. This creates 13 inline images per main README without adding assets or recipes. Original image proportions are preserved. The old English and Chinese gallery-section anchors remain valid, and the 16-pack directory and three copyable starter/edit blocks remain unchanged.

Sol high-reasoning review accepted the structure and identified one input-label error: P084 had been described as using a performer photo even though its recorded reference is an illustrated character. The editor changed this to a performer reference image, clarified P076’s doodle input and made P043’s caption describe specified furniture, materials and light. The primary editor checked those descriptions against the catalog and independently compared the final source and target structure, images, inputs and prompt destinations.

GitHub Markdown API output was visually inspected with an 835-pixel-wide local preview: the lead examples and poster/portrait pair are substantially larger than the previous three-column layout. Local preview styling is not identical to GitHub; published-page inspection is a separate visual check. Generators and the content validator pass. All recipe data, image files and generation records are unchanged in this round; no mobile usability or conversion result is claimed.


## Wide homepage cover

Added a separately recorded 3:1 VideoWeb banner to the English and Simplified Chinese homepages, after language navigation and before the featured examples. At an 835-pixel content width it displays about 278 pixels high. The 143 earlier assets remain intact; the new editorial cover brings the total to 144 without adding a recipe. Its exact prompt, dimensions, hash and observed deviations are recorded in the manifest and generation log. Earlier review counts in this document describe their respective historical revisions.


## Brighter creative cover

Reader feedback rejected the dark lamp banner as insufficiently engaging. A new 3:1 cover replaces it on the English and Simplified Chinese homepages: cobalt title text on warm ivory, with an orange-and-turquoise paper island, lighthouse, oversized headphones and a courier. The single connected scene presents product and story imagery without adding a thumbnail grid. The prior banner and its provenance remain available; the new record brings the total to 145 images, with 106 recipes unchanged.

The editor visually compared the new cover with the source cover: both prioritize a large readable title and tactile materials. The new banner keeps its existing display height and leaves the following two-column examples in place. Its headphone arch is slightly cropped at the upper edge, but the title, lighthouse and courier remain clear. This is a design judgment, not evidence of improved reader engagement or conversion. All 139 inherited PNGs remain byte-identical.

A Sol high-reasoning reviewer inspected both cover images and recommended keeping the revision for its clearer title hierarchy, stronger color contrast and connected miniature scene. It noted that the large headphones could briefly suggest audio, but did not consider this a required correction in context. The primary editor independently reconsidered that concern against the explicit image-library title and the following product/story examples and retained the design. Catalog, gallery, README-directory, asset and link checks pass.
