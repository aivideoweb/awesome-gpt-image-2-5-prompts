# VideoWeb AI: from a prompt to an approved still

[English README](../README.md) · [简体中文](../README_zh.md)

1. Pick a [recipe](../prompts/README.md). For quick text or single-reference work, open the [free tool](https://videoweb.ai/free-gpt-image-2-5/). For the model workflow, open [GPT Image 2.5](https://videoweb.ai/model/gpt-image-2-5/).
2. Replace fictional names and copy, choose a ratio, and upload a reference only when the recipe requires it. The free page shows a 2,000-character prompt field and one reference input. For the long tea-sheet prompt, copy the [P077 free-tool version](../prompts/14-sketch-to-story.md#p077-en-compact) alone. Multi-reference recipes need a tool that supports every required input; do not omit inputs silently.
3. Complete the tool’s verification, generate, inspect lettering and identity, then download the approved image. Re-upload it for a separate edit; change one variable at a time.
4. For motion, prepare one standalone still. With a P087 board, upload it to an image editor and run the [shot 01 expansion](../prompts/15-x-community.md#p087-single-frame); this produces a single 16:9 frame instead of a small crop of the grid. Check the bottle, label, edges and actual dimensions, then save it. With P084, its included next edit expands shot 4. These expansion instructions are not recorded video tests.
5. Open a separate [image-to-video tool](https://videoweb.ai/image-to-video/). Upload that approved standalone image, not the storyboard grid. Confirm that tool’s own duration, resolution and input controls before generating.

## Choose by deliverable

| Deliverable | Start here | Inspect before handoff |
| --- | --- | --- |
| Video cover | [P008](../prompts/02-social.md#p008) | Face, title legibility at thumbnail size, space around UI overlays |
| Product sequence | [P087 board](../prompts/15-x-community.md#p087) → [expand shot 01](../prompts/15-x-community.md#p087-single-frame) | Bottle silhouette, label and camera continuity |
| Narrative board | [P084](../prompts/14-sketch-to-story.md#p084) | Character clothing, prop position, panel count |
| Location study | [P043](../prompts/08-spaces.md#p043) | Lighting, usable camera space, objects blocking movement |

## Motion prompt after approving one frame

```text
Use the uploaded image as the opening composition. Make a slow, steady camera push toward the main subject. Keep its silhouette, surface details and position consistent. Allow only subtle ambient movement in the background. No new objects, no cuts, no changing lettering. End with a stable hold suitable for an editor to add a title.
```

This is an untested motion brief for a separate video model, not a GPT Image 2.5 video result. Review flicker, deformation, accidental text changes and frame edges throughout the clip. Add final titles in an editor when exact copy matters.

## 中文步骤

从配方索引选用途，复制一种语言的提示词，替换虚构产品和文字。免费页支持一张参考图，文字输入上限显示为2000字符；茶叶产品页的长提示词请改用 [P077 免费工具版](../prompts/14-sketch-to-story.md#p077-en-compact)，只复制精简版一段。多图配方要选择支持相应输入数量的工具。完成验证后生图，检查文字、人物与产品，再下载确认版本。

需要视频时，先准备独立单帧。若用P087，上传确认的六格总板，执行[第01格扩图指令](../prompts/15-x-community.md#p087-single-frame)，得到独立16:9画面；不要直接把整张分镜板交给视频工具。先核对瓶身、标签、边缘和实际尺寸，再保存确认稿。P084可用其后续修改指令扩展第4格。新增扩图指令尚未实测。

将确认单帧上传到独立图片转视频工具，可以先试缓慢推进镜头，要求产品外形、文字与位置保持一致。检查闪烁、变形与画面边缘；正式字幕可在剪辑软件中添加。

## Page verification

VideoWeb model, free-tool and affiliate pages were read on 2026-09-22. Browser generation, download and uptime were not tested. No-signup access still includes verification. Free image access does not imply free video or every advanced feature. [Affiliate partnerships](https://videoweb.ai/affiliate-program/) are available.
