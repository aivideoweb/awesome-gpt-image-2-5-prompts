# Awesome GPT Image 2.5 Prompts — VideoWeb AI

从一段描述或一张现有图片开始，制作商品广告、修改海报、规划视频分镜。这里提供可复制的提示词、示例图和逐步修改方法，适合电商经营者、设计师和视频创作者。

**106 条配方，每条都有生成示例。** 核心配方同时说明输入素材、允许改变的部分、必须保留的细节和结果检查方法，方便从一张概念图继续做到下一版。

[使用 GPT Image 2.5](https://videoweb.ai/cn/model/gpt-image-2-5/) · [免注册免费体验](https://videoweb.ai/cn/free-gpt-image-2-5/)

[先看三个案例](#featured-examples) · [复制生图提示词](#quick-start) · [查找全部分类](#按实际工作选场景) · [看修改前后](#editing-examples) · [视频与进阶](#learn-more)

[English](README.md) · **简体中文** · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português (Brasil)](README_pt.md) · [Italiano](README_it.md) · [Русский](README_ru.md) · [العربية](README_ar.md) · [हिन्दी](README_hi.md) · [ไทย](README_th.md) · [Bahasa Indonesia](README_id.md) · [Tiếng Việt](README_vi.md)

<a id="featured-examples"></a>

## 先看三个实际用途

| 为广告预留文案位置 | 商品照片，变成白底图 | 同一人物，九个镜头 |
| --- | --- | --- |
| [![耳机广告留白](assets/images/p094-videoweb.png)](prompts/16-videoweb-x-creators.md#p094-zh) | <a href="prompts/01-product.md#p002-zh"><img src="assets/images/cup-input.png" width="45%" alt="输入：厨房木桌上的陶瓷杯"> → <img src="assets/images/example-p002.png" width="45%" alt="结果：纯白背景上的陶瓷杯"></a> | [![九镜头音乐短片分镜](assets/images/example-p084.png)](prompts/14-sketch-to-story.md#p084-zh) |
| 产品放右侧，左侧留空，方便后期排标题。文字生图，无需参考图。 | 上传一张商品照片，换成白底并调整光线。左为输入，右为结果；也可下载示例输入图练习。 | 用同一人物参考图规划景别和镜头顺序，为短片前期讨论准备分镜。需上传人物图。 |
| [P094 · 中文提示词](prompts/16-videoweb-x-creators.md#p094-zh) | [P002 · 中文提示词与输入图](prompts/01-product.md#p002-zh) | [P084 · 中文提示词与输入图](prompts/14-sketch-to-story.md#p084-zh) |

这些示例展示创作方向，也保留检查记录：耳机结构属于概念设计；杯子的釉点和比例有轻微变化，使用前应对照杯口、把手和釉面；九镜头中的眼部特写和拿本子的动作仍需检查连续性。[查看生成记录](docs/generation-log.md)。

<a id="quick-start"></a>

## 从第一张图开始

**只有想法：** 复制下方台灯提示词，无需上传图片。先保留默认内容试一次，再替换品牌、商品和文案。

**已有商品照片：** 使用 [P002 白底商品图提示词](prompts/01-product.md#p002-zh)，先将杯子的描述和保留项改为自己的商品，再上传照片；也可以先下载[陶瓷杯示例输入图](assets/images/cup-input.png)练习。

文字生图示例：

```text
为虚构台灯品牌 TIDELINE 制作 3:2 横版产品广告。
台灯使用午夜蓝圆柱金属底座、象牙白圆盘灯罩和橙色拉环。
放在珊瑚色阶梯展台上，背景为深蓝色，光线柔和，阴影自然。
产品占画面右侧六成；左侧仅排白字“LIGHT, UNPLUGGED.”和“TIDELINE”。
呈现真实金属纹理，只保留一盏灯，不添加其他文字或产品参数。
```

生成后先检查文字、灯罩轮廓和拉环位置，保存满意的版本。[下方案例](#editing-examples)展示如何在它的基础上继续改色、改标题。[完整 P001 配方](prompts/01-product.md#p001-zh)另附约束和检查方法。

免费体验页支持文字或一张参考图，生成前需要验证。需要多张输入图的配方，请使用支持相应输入数量的工具。

## 按实际工作选场景

<!-- BEGIN GENERATED SHOWCASE -->

按具体任务查找。16 个场景包共 106 条配方；想先看效果，可浏览[完整图片画廊](docs/gallery.md)。

| 场景包 | 可以做什么 | 配方数 |
| --- | --- | --- |
| [产品摄影与电商](prompts/01-product.md) | 商品白底图、护肤静物、结构概念、材质特写、礼盒 | 6 |
| [广告、社媒与创作者封面](prompts/02-social.md) | 活动海报、视频缩略图、旅行轮播、播客封面 | 6 |
| [人像、时尚与宠物](prompts/03-people-pets.md) | 职业头像、宠物写真、外套试穿、纪念插画 | 6 |
| [精准修改与多轮工作流](prompts/04-editing.md) | 换色、去杂物、改光线、替换文字、商品抠图 | 6 |
| [信息图、教育与演示](prompts/05-information.md) | 知识讲解、数据图、地图、植物周期、流程演示 | 6 |
| [品牌识别与界面概念](prompts/06-brand-ui.md) | 字标、导视、应用界面、落地页、包装系列 | 6 |
| [漫画、角色与游戏美术](prompts/07-stories-games.md) | 漫画、角色转面、表情表、游戏图标、像素场景 | 6 |
| [建筑、室内与酒店空间](prompts/08-spaces.md) | 室内空间、材质翻新、快闪店、庭院、草图效果图 | 6 |
| [出版、印刷与编辑插画](prompts/09-publishing.md) | 书籍封面、食谱跨页、编辑插画、独立刊物 | 6 |
| [系列、本地化与制作交付](prompts/10-production.md) | 四季系列、横竖版适配、本地化、三图合成、老照修复 | 6 |
| [多语言海报](prompts/11-multilingual.md) | 中、英、日、韩、西、法、德、葡、阿拉伯、印地、泰、俄 | 12 |
| [官方发布场景原创实践](prompts/12-launch-examples.md) | 带前后对照的换装、被套换花色、改字、行程修改、蜡烛计数 | 7 |
| [可微调创作配方](prompts/13-customizable-studio.md) | 可调整人物、配色与文案的工坊肖像、咖啡海报、包装、微缩景观 | 6 |
| [从草图到故事（10 条英文、2 条中英）](prompts/14-sketch-to-story.md) | 草图探索、角色风格、人像连续修改、品牌周边、故事分镜 | 12 |
| [X 社区实用场景](prompts/15-x-community.md) | X 来源的食材文字、香水分镜、旅行卡、建筑方案、邀请函 | 6 |
| [VideoWeb 创作者 X 案例](prompts/16-videoweb-x-creators.md) | VideoWeb 新增：时装短片服装、复古开场帧、耳机广告 | 3 |

<!-- END GENERATED SHOWCASE -->

## 海报、人像与空间

| 多语言海报：安排文字层级 | 人像修改：保留身份细节 | 空间概念：安排材料与动线 |
| --- | --- | --- |
| [![日英双语烘焙海报](assets/images/komorebi-bakery.png)](prompts/11-multilingual.md#l003) | [![自然职业头像](assets/images/example-p013.png)](prompts/03-people-pets.md#p013) | [![工坊改造阅读室](assets/images/reading-room.png)](prompts/08-spaces.md#p043) |
| 用给定的日文和英文组织标题与副标题，生成后逐字检查。无需参考图。[L003 配方](prompts/11-multilingual.md#l003)。 | 上传人像，改变背景和穿着后对照五官、肤色及发际线。[P013 中英配方与输入图](prompts/03-people-pets.md#p013-zh)。 | 明确家具位置、材料和光线，先讨论空间概念；不是施工图。[P043 中英配方](prompts/08-spaces.md#p043-zh)。 |

<a id="editing-examples"></a>

## 修改前后：改变指定部分，检查其他细节

### 一次修改：三根蜡烛变成五根

| 输入图：三根蜡烛 | 修改后：五根蜡烛 |
| --- | --- |
| ![Three candles](assets/images/launch-cake-input.png) | ![Five candles](assets/images/launch-cake-edit.png) |

任务是改变数量，同时保留蛋糕、盘子和构图。成图中可见五根橙色蜡烛，奶油纹理略有变化。这个对照适合练习“明确修改对象＋列出保留项”。[P067 提示词、输入图与检查记录](prompts/12-launch-examples.md#p067-zh)。

### 连续修改：先换颜色，再换标题

| 原稿 | 第一步：换底座颜色 | 第二步：换标题 |
| --- | --- | --- |
| ![Blue lamp](assets/images/tideline-lamp.png) | ![Green lamp](assets/images/tideline-lamp-jade.png) | ![New headline](assets/images/tideline-lamp-copy.png) |

用你刚保存的台灯图继续操作；也可以下载[蓝色示例图](assets/images/tideline-lamp.png)并上传。先只改底座：

```text
只把台灯底座改为低饱和玉绿色，保持形状和金属纹理。
灯罩、拉环、文字、背景、镜头与展台均保持不变。
```

检查并保存绿色成图，以这张图作为下一步输入：

```text
只把“LIGHT, UNPLUGGED.”改为“YOUR EVENING, UPGRADED.”。
保留绿色底座、品牌名“TIDELINE”、版式、产品和光线。
```

**为什么分两步：** 每次检查一种变化，出错时可以退回上一张确认图。本例灯杆也随底座变绿，纹理和高光略有变化；需要严格保留产品细节时，还应继续修正。[实际执行提示词与完整记录](docs/editing-case-study.md)。

<a id="learn-more"></a>

## 视频与进阶指南

| 你想继续做什么 | 从这里开始 |
| --- | --- |
| 让确认后的图片进入视频制作 | [VideoWeb 图片到视频流程](docs/videoweb-workflow.md) · [官方演示视频](docs/video-guide.md) |
| 找更多 X 社区案例 | [来源、原帖与改写说明](docs/x-community.md) |
| 改善提示词或排查修图问题 | [提示词写法](docs/prompting-guide.md) · [10 条玩法路线](docs/playbook.md) |
| 了解模型、接口与工具区别 | [版本说明](docs/model-notes.md) · [升级对比](docs/images-2-vs-2-5.md) · [API 使用](docs/api-guide.md) · [在线工具对照](docs/tools.md) |
| 做其他语言的图片 | [多语言提示词](prompts/11-multilingual.md) · [语言覆盖说明](docs/localization-guide.md) |

## 关于示例与开源使用

本库由 VideoWeb AI 基于 [Flaq AI 源库](https://github.com/flaqai/awesome-chatgpt-images-2-5-prompts)维护，保留源库 103 条配方，新增 3 条创作者配方。共 16 个场景包、143 张图片；78 条配方为中英双语，16 条为英文，另有 12 条本地语言配方。

图片由项目生图工具生成，未返回底层模型名称，不代表 VideoWeb 或指定型号的实测结果。示例可能有文字、结构或细节偏差，已知问题见[生成记录](docs/generation-log.md)。X 作者原图另有来源标注，不纳入本库 MIT 许可。

[源库与维护说明](docs/upstream.md) · [贡献规范](CONTRIBUTING.md) · [原创与授权说明](docs/originality.md)

## 联盟推广合作

我们支持联盟推广合作，欢迎教程作者、视频创作者和工具评测者加入 [VideoWeb AI 联盟计划](https://videoweb.ai/affiliate-program/)。佣金、资格和结算规则以联盟页面为准。

## 许可

[MIT](LICENSE) © 2026 Flaq AI；VideoWeb AI 品牌适配与新增内容。第三方素材另行标注。
