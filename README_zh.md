# Awesome ChatGPT Images 2.5 Prompts — VideoWeb AI 提示词库

**面向电商产品图、精准修图、人物宠物、广告海报、故事分镜与多语言设计的实用提示词。由 VideoWeb AI 维护，基于 Flaq AI 的开源配方扩展。**

[English](README.md) · **简体中文** · [繁體中文](README_tw.md) · [日本語](README_ja.md) · [한국어](README_ko.md) · [Español](README_es.md) · [Français](README_fr.md) · [Deutsch](README_de.md) · [Português (Brasil)](README_pt.md) · [Italiano](README_it.md) · [Русский](README_ru.md) · [العربية](README_ar.md) · [हिन्दी](README_hi.md) · [ไทย](README_th.md) · [Bahasa Indonesia](README_id.md) · [Tiếng Việt](README_vi.md)

![VideoWeb AI GPT Image 2.5 提示词库封面](assets/images/videoweb-cover.png)

[浏览全部图片与分类](#按实际工作选场景) · [查看修图案例](docs/editing-case-study.md) · [提示词写法](docs/prompting-guide.md) · [API 使用](docs/api-guide.md) · [图片生成记录](docs/generation-log.md)

## 在 VideoWeb AI 开始

**[使用 GPT Image 2.5](https://videoweb.ai/model/gpt-image-2-5/) · [免注册免费体验](https://videoweb.ai/free-gpt-image-2-5/)**

推荐使用 VideoWeb 的 GPT Image 2.5 页面持续创作；免费体验页支持文字或一张参考图，提交前需要验证。先选配方、检查图片，再继续修改。


## 三步开始

1. 从下表选择场景，复制其中一个语言版本，把虚构品牌、商品和文案替换成你的内容。
2. 新建图直接使用；编辑图按提示顺序上传素材，并说明每张图的用途。
3. 检查结果并保存确认稿，再使用条目中的后续修改。开启新对话时，请重新附上确认稿。

先试试这个原创简版：

```text
为虚构台灯品牌制作3:2横版产品广告。
台灯使用午夜蓝圆柱金属底座、象牙白圆盘灯罩和橙色拉环。
放在珊瑚色阶梯展台上，深蓝背景，阴影自然可信。
左侧仅排白字“LIGHT, UNPLUGGED.”和“TIDELINE”。
呈现真实材料纹理，只保留一盏灯，不添加其他文案或产品参数。
```

确认图片后继续：

```text
只把台灯底座改为低饱和玉绿色，保持形状和金属纹理。
灯罩、拉环、文字、背景、镜头与展台均保持不变。
```

[查看详细版](prompts/01-product.md#p001)；本库展示图的[实际执行提示词](assets/generation/tideline-lamp.txt)另有记录。

## 按实际工作选场景

| 场景包 | 包含内容 | 数量 |
| --- | --- | --- |
| [产品摄影与电商](#showcase-01-product) | 台灯广告、陶瓷杯白底图、护肤静物、磨豆机结构、运动鞋特写、礼盒 | 6 |
| [广告与社交媒体](#showcase-02-social) | 活动海报、视频封面、旅行轮播、午餐广告、播客封面、市集主视觉 | 6 |
| [人物、时尚与宠物](#showcase-03-people-pets) | 职业头像、宠物探险照、外套试穿、生活抓拍、双人插画、宠物水彩 | 6 |
| [精准编辑](#showcase-04-editing) | 局部换色、去杂物、光照调整、定点换字、草图添加物件、透明抠图 | 6 |
| [信息图与教育](#showcase-05-information) | 雨水花园、风味图、示例数据图、街区地图、植物生长、流程演示 | 6 |
| [品牌与界面](#showcase-06-brand-ui) | 字标、导视、移动应用、落地页、包装系列、创作者看板 | 6 |
| [故事与游戏](#showcase-07-stories-games) | 六格故事、角色转面、表情表、物品图标、等距屋顶、像素海港 | 6 |
| [建筑与空间](#showcase-08-spaces) | 阅读室、公寓翻新、精品客房、快闪店、庭院、小亭效果图 | 6 |
| [出版与插画](#showcase-09-publishing) | 书封、食谱跨页、年度回顾、编辑隐喻、水墨画、独立刊物 | 6 |
| [系列与制作交付](#showcase-10-production) | 四季系列、横转竖、本地化、三图合成、老照修复、分镜扩展 | 6 |
| [12种语言配方](#showcase-11-multilingual) | 中、英、日、韩、西、法、德、葡、阿拉伯、印地、泰、俄语 | 12 |
| [官方发布场景原创实践](#showcase-12-launch-examples) | 宠物换装、儿童肖像、被套花色、城市文字、立方体、行程卡、蜡烛计数 | 7 |
| [可微调创作配方](#showcase-13-customizable-studio) | 工坊人像、咖啡流程、收藏包装、灯塔微缩、纪念贺卡、陶艺拼贴 | 6 |
| [从草图到故事：英文工作流](#showcase-14-sketch-to-story) | 草图、密集排版、人像编辑、品牌周边、动作表、MV及剧情分镜 | 12 |
| [X 社区来源配方](#showcase-15-x-community) | 食材文字、香水分镜、交通海报、纸艺旅行卡、建筑方案、野餐邀请 | 6 |
| [VideoWeb 创作者配方](#showcase-16-videoweb-x-creators) | 时装短片服装概念、复古开场帧、耳机广告 | 3 |

<!-- BEGIN GENERATED SHOWCASE -->

下面直接展示全部 16 个分类、106 条配方的图片。每类附一条完整提示词；点击其他图片可查看对应配方。

图片是项目生成示例，不代表 VideoWeb 或指定模型的实测结果。配方与实际执行提示词可能有差异，输入关系及已知问题见[图片生成记录](docs/generation-log.md)。修图配方需要上传参考图；多图任务需使用支持多图输入的工具。

<a id="showcase-01-product"></a>

### 产品摄影与电商 · 6

| | | |
| --- | --- | --- |
| [![无线台灯广告主图](assets/images/tideline-lamp.png)](prompts/01-product.md#p001)<br>**[P001 · 无线台灯广告主图](prompts/01-product.md#p001)** | [![陶瓷杯白底商品图](assets/images/example-p002.png)](prompts/01-product.md#p002)<br>**[P002 · 陶瓷杯白底商品图](prompts/01-product.md#p002)** | [![护肤品成分氛围图](assets/images/example-p003.png)](prompts/01-product.md#p003)<br>**[P003 · 护肤品成分氛围图](prompts/01-product.md#p003)** |
| [![手摇磨豆机结构概念图](assets/images/example-p004.png)](prompts/01-product.md#p004)<br>**[P004 · 手摇磨豆机结构概念图](prompts/01-product.md#p004)** | [![运动鞋材质特写](assets/images/example-p005.png)](prompts/01-product.md#p005)<br>**[P005 · 运动鞋材质特写](prompts/01-product.md#p005)** | [![礼盒开箱平铺图](assets/images/example-p006.png)](prompts/01-product.md#p006)<br>**[P006 · 礼盒开箱平铺图](prompts/01-product.md#p006)** |

**可直接复制 · P001**

输入：此默认示例无需上传参考图。

```text
交付物：无线台灯广告主图。目标比例：3:2。模式：新建。
为虚构品牌 TIDELINE 创作无线台灯广告。午夜蓝金属矮圆柱底座搭配象牙白圆盘灯罩和橙色织物拉环，放在珊瑚色阶梯展台上。深蓝背景，灯罩底部暖光，右侧产品占六成；左侧白字仅为“LIGHT, UNPLUGGED.”与“TIDELINE”。呈现真实金属微纹理及柔和阴影。
约束：仅一盏灯，不编造续航参数，不添加文字。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只将底座改为低饱和玉绿色，保留灯罩、拉环、构图和文字。

**检查要点：** 逐字检查文案，比较灯罩轮廓及拉环位置。

[本分类完整配方与使用说明](prompts/01-product.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-02-social"></a>

### 广告、社媒与创作者封面 · 6

| | | |
| --- | --- | --- |
| [![社区修理日海报](assets/images/example-p007.png)](prompts/02-social.md#p007)<br>**[P007 · 社区修理日海报](prompts/02-social.md#p007)** | [![单一主题视频缩略图](assets/images/example-p008.png)](prompts/02-social.md#p008)<br>**[P008 · 单一主题视频缩略图](prompts/02-social.md#p008)** | [![慢旅行轮播封面](assets/images/example-p009.png)](prompts/02-social.md#p009)<br>**[P009 · 慢旅行轮播封面](prompts/02-social.md#p009)** |
| [![街区餐厅午餐海报](assets/images/example-p010.png)](prompts/02-social.md#p010)<br>**[P010 · 街区餐厅午餐海报](prompts/02-social.md#p010)** | [![播客编辑风封面](assets/images/example-p011.png)](prompts/02-social.md#p011)<br>**[P011 · 播客编辑风封面](prompts/02-social.md#p011)** | [![秋日市集活动主视觉](assets/images/example-p012.png)](prompts/02-social.md#p012)<br>**[P012 · 秋日市集活动主视觉](prompts/02-social.md#p012)** |

**可直接复制 · P007**

输入：此默认示例无需上传参考图。

```text
交付物：社区修理日海报。目标比例：2:3。模式：新建。
制作社区修理日海报，奶油再生纸质感。小螺丝刀、橙色线轴、修好的蓝杯俯拍围成松散圆环。深蓝大标题“FIX IT TOGETHER”，下方“SAT 14 NOV”“10:00–16:00”“RIVER HALL”，朱红细线串联排版，平面印刷稿并保留宽边距。
约束：活动为虚构示例，不添加二维码、赞助商、价格或未提供信息。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 仅将日期换成“SAT 21 NOV”，保持层级与换行。

**检查要点：** 检查日期、时间连接号及手机尺寸可读性。

[本分类完整配方与使用说明](prompts/02-social.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-03-people-pets"></a>

### 人像、时尚与宠物 · 6

| | | |
| --- | --- | --- |
| [![自然职业头像](assets/images/example-p013.png)](prompts/03-people-pets.md#p013)<br>**[P013 · 自然职业头像](prompts/03-people-pets.md#p013)** | [![宠物探险家肖像](assets/images/example-p014.png)](prompts/03-people-pets.md#p014)<br>**[P014 · 宠物探险家肖像](prompts/03-people-pets.md#p014)** | [![亚麻外套虚拟穿搭](assets/images/example-p015.png)](prompts/03-people-pets.md#p015)<br>**[P015 · 亚麻外套虚拟穿搭](prompts/03-people-pets.md#p015)** |
| [![胶片周末生活照](assets/images/example-p016.png)](prompts/03-people-pets.md#p016)<br>**[P016 · 胶片周末生活照](prompts/03-people-pets.md#p016)** | [![双人纪念插画](assets/images/example-p017.png)](prompts/03-people-pets.md#p017)<br>**[P017 · 双人纪念插画](prompts/03-people-pets.md#p017)** | [![宠物纪念水彩](assets/images/example-p018.png)](prompts/03-people-pets.md#p018)<br>**[P018 · 宠物纪念水彩](prompts/03-people-pets.md#p018)** |

**可直接复制 · P013**

参考图（按顺序上传）：[1](assets/images/adult-input.png)

```text
交付物：自然职业头像。目标比例：4:5。模式：编辑。
图1为获同意的成年人照片。制作北向大窗旁的自然职业头像，暖灰影棚背景柔和虚化，纯炭灰圆领上衣。胸部以上平视构图，保留皮肤纹理和自然微笑。
约束：保留身份、年龄、肤色、五官比例、发型和独特印记，不美颜塑形。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 仅将背景换成低饱和橄榄色影棚墙。

**检查要点：** 对照原图检查眼距、鼻子、下颌、雀斑和发际线。

[本分类完整配方与使用说明](prompts/03-people-pets.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-04-editing"></a>

### 精准修改与多轮工作流 · 6

| | | |
| --- | --- | --- |
| [![商品配色局部修改](assets/images/tideline-lamp-jade.png)](prompts/04-editing.md#p019)<br>**[P019 · 商品配色局部修改](prompts/04-editing.md#p019)** | [![去除桌面杂物](assets/images/example-p020.png)](prompts/04-editing.md#p020)<br>**[P020 · 去除桌面杂物](prompts/04-editing.md#p020)** | [![室内窗光转傍晚](assets/images/example-p021.png)](prompts/04-editing.md#p021)<br>**[P021 · 室内窗光转傍晚](prompts/04-editing.md#p021)** |
| [![海报文案定点替换](assets/images/example-p022.png)](prompts/04-editing.md#p022)<br>**[P022 · 海报文案定点替换](prompts/04-editing.md#p022)** | [![草图引导添加花盆](assets/images/example-p023.png)](prompts/04-editing.md#p023)<br>**[P023 · 草图引导添加花盆](prompts/04-editing.md#p023)** | [![干净商品抠图](assets/images/example-p024.png)](prompts/04-editing.md#p024)<br>**[P024 · 干净商品抠图](prompts/04-editing.md#p024)** |

**可直接复制 · P019**

参考图（按顺序上传）：[1](assets/images/tideline-lamp.png)

```text
交付物：商品配色局部修改。目标比例：3:2。模式：编辑。
图1为已确认商品广告。只将台灯圆柱底座由午夜蓝改为低饱和玉绿色，保持原阳极金属纹理和可信高光渐变，不改象牙白灯罩或橙色拉环，将周围广告视为锁定稿。
约束：尽量保持全部文字、位置、比例、镜头、背景和阴影。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 在已确认绿色版本上，仅将“LIGHT, UNPLUGGED.”改为“YOUR EVENING, UPGRADED.”，保留绿色。

**检查要点：** 比较各版本底座边缘、金属光泽、拉环和排版。

[本分类完整配方与使用说明](prompts/04-editing.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-05-information"></a>

### 信息图、教育与演示 · 6

| | | |
| --- | --- | --- |
| [![雨水花园三步科普](assets/images/example-p025.png)](prompts/05-information.md#p025)<br>**[P025 · 雨水花园三步科普](prompts/05-information.md#p025)** | [![新手咖啡风味轮](assets/images/example-p026.png)](prompts/05-information.md#p026)<br>**[P026 · 新手咖啡风味轮](prompts/05-information.md#p026)** | [![示例数据柱状图](assets/images/example-p027-v2.png)](prompts/05-information.md#p027)<br>**[P027 · 示例数据柱状图](prompts/05-information.md#p027)** |
| [![虚构街区步行地图](assets/images/example-p028.png)](prompts/05-information.md#p028)<br>**[P028 · 虚构街区步行地图](prompts/05-information.md#p028)** | [![植物生命周期教学卡](assets/images/example-p029.png)](prompts/05-information.md#p029)<br>**[P029 · 植物生命周期教学卡](prompts/05-information.md#p029)** | [![工作坊流程演示页](assets/images/example-p030.png)](prompts/05-information.md#p030)<br>**[P030 · 工作坊流程演示页](prompts/05-information.md#p030)** |

**可直接复制 · P025**

输入：此默认示例无需上传参考图。

```text
交付物：雨水花园三步科普。目标比例：3:2。模式：新建。
制作课堂信息图“WHERE RAIN GOES”，三等宽面板依次展示屋顶落雨、水进入种植浅盆地、水渗入土壤，标签仅“COLLECT”“SLOW”“SOAK”。简洁剖面、深蓝箭头、奶油背景和绿植，水流路线与文字分离。
约束：不表现为净化饮用水，不编造效率百分比。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只提升箭头对比，保持步骤和文字。

**检查要点：** 检查水流方向及土壤剖面是否清楚表达下渗。

[本分类完整配方与使用说明](prompts/05-information.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-06-brand-ui"></a>

### 品牌识别与界面概念 · 6

| | | |
| --- | --- | --- |
| [![独立陶艺品牌字标](assets/images/example-p031-v2.png)](prompts/06-brand-ui.md#p031)<br>**[P031 · 独立陶艺品牌字标](prompts/06-brand-ui.md#p031)**<br>修订后成图；完整过程见配方 | [![博物馆导视系统](assets/images/example-p032.png)](prompts/06-brand-ui.md#p032)<br>**[P032 · 博物馆导视系统](prompts/06-brand-ui.md#p032)** | [![读书会移动应用概念](assets/images/example-p033.png)](prompts/06-brand-ui.md#p033)<br>**[P033 · 读书会移动应用概念](prompts/06-brand-ui.md#p033)** |
| [![工作坊预约落地页概念](assets/images/example-p034.png)](prompts/06-brand-ui.md#p034)<br>**[P034 · 工作坊预约落地页概念](prompts/06-brand-ui.md#p034)** | [![茶叶包装家族](assets/images/example-p035.png)](prompts/06-brand-ui.md#p035)<br>**[P035 · 茶叶包装家族](prompts/06-brand-ui.md#p035)** | [![创作者工作台概念](assets/images/example-p036.png)](prompts/06-brand-ui.md#p036)<br>**[P036 · 创作者工作台概念](prompts/06-brand-ui.md#p036)** |

**可直接复制 · P032**

输入：此默认示例无需上传参考图。

```text
交付物：博物馆导视系统。目标比例：3:2。模式：新建。
为虚构工艺博物馆设计导视概念板，三块统一哑光深蓝标牌，象牙无衬线大字“GALLERY →”“WORKSHOP ↑”“CAFÉ ←”，各有统一几何方块符号。正面展示，下方窄材料细节条。
约束：保持箭头方向和字号一致，不作紧急出口或无障碍认证声明。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只将材质改为涂漆木板，保留深蓝和象牙色。

**检查要点：** 检查箭头与可读性，实际导视另行验证。

[本分类完整配方与使用说明](prompts/06-brand-ui.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-07-stories-games"></a>

### 漫画、角色与游戏美术 · 6

| | | |
| --- | --- | --- |
| [![修补纸月亮六格故事](assets/images/paper-moon-story.png)](prompts/07-stories-games.md#p037)<br>**[P037 · 修补纸月亮六格故事](prompts/07-stories-games.md#p037)** | [![原创角色转面表](assets/images/example-p038.png)](prompts/07-stories-games.md#p038)<br>**[P038 · 原创角色转面表](prompts/07-stories-games.md#p038)** | [![吉祥物四表情表](assets/images/example-p039-v2.png)](prompts/07-stories-games.md#p039)<br>**[P039 · 吉祥物四表情表](prompts/07-stories-games.md#p039)** |
| [![温馨游戏物品图标](assets/images/example-p040-v2.png)](prompts/07-stories-games.md#p040)<br>**[P040 · 温馨游戏物品图标](prompts/07-stories-games.md#p040)** | [![等距屋顶花园游戏场景](assets/images/example-p041.png)](prompts/07-stories-games.md#p041)<br>**[P041 · 等距屋顶花园游戏场景](prompts/07-stories-games.md#p041)** | [![像素港湾游戏背景](assets/images/example-p042.png)](prompts/07-stories-games.md#p042)<br>**[P042 · 像素港湾游戏背景](prompts/07-stories-games.md#p042)** |

**可直接复制 · P037**

输入：此默认示例无需上传参考图。

```text
交付物：修补纸月亮六格故事。目标比例：3:2。模式：新建。
创作3×2六格无字故事：奶油色修理机器人、单只琥珀眼、青绿围裙，在阁楼发现破纸月亮，拿起两半，选橙线，缝合，挂起，最后坐在月光下。水粉彩铅质感、象牙格缝、暖桃和灰青绿、墨蓝暮色。
约束：保持各格机器人和工作室可辨识一致，恰好六格，无对白。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 仅改第三格：机器人选线时月亮仍未缝合。

**检查要点：** 检查动作顺序、围裙一致性及是否提前出现修好状态。

[本分类完整配方与使用说明](prompts/07-stories-games.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-08-spaces"></a>

### 建筑、室内与酒店空间 · 6

| | | |
| --- | --- | --- |
| [![旧工坊改造阅读室](assets/images/reading-room.png)](prompts/08-spaces.md#p043)<br>**[P043 · 旧工坊改造阅读室](prompts/08-spaces.md#p043)** | [![小公寓材质翻新](assets/images/example-p044.png)](prompts/08-spaces.md#p044)<br>**[P044 · 小公寓材质翻新](prompts/08-spaces.md#p044)** | [![精品客房软装概念](assets/images/example-p045.png)](prompts/08-spaces.md#p045)<br>**[P045 · 精品客房软装概念](prompts/08-spaces.md#p045)** |
| [![补充装快闪店概念](assets/images/example-p046.png)](prompts/08-spaces.md#p046)<br>**[P046 · 补充装快闪店概念](prompts/08-spaces.md#p046)** | [![庭院种植设计概念](assets/images/example-p047.png)](prompts/08-spaces.md#p047)<br>**[P047 · 庭院种植设计概念](prompts/08-spaces.md#p047)** | [![草图转小亭效果图](assets/images/example-p048.png)](prompts/08-spaces.md#p048)<br>**[P048 · 草图转小亭效果图](prompts/08-spaces.md#p048)** |

**可直接复制 · P043**

输入：此默认示例无需上传参考图。

```text
交付物：旧工坊改造阅读室。目标比例：3:2。模式：新建。
拍摄旧自行车工坊改造的小阅读室：左侧弧形陶土软凳、中间桦木长桌四把椅、后方旧钢窗、右侧窄书架、窗边一棵橄榄树。保留混凝土梁和修补水磨石，入口平视、垂直线端正、柔和晨光、材料木纹可见。
约束：无人、无标识和招牌，动线可信；概念图非施工文件。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 仅把长凳面料改深青绿，保持建筑和家具位置。

**检查要点：** 清点椅子，检查走道、窗结构和桌支撑。

[本分类完整配方与使用说明](prompts/08-spaces.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-09-publishing"></a>

### 出版、印刷与编辑插画 · 6

| | | |
| --- | --- | --- |
| [![果园主题书籍封面](assets/images/example-p049.png)](prompts/09-publishing.md#p049)<br>**[P049 · 果园主题书籍封面](prompts/09-publishing.md#p049)** | [![食谱编辑跨页概念](assets/images/example-p050.png)](prompts/09-publishing.md#p050)<br>**[P050 · 食谱编辑跨页概念](prompts/09-publishing.md#p050)** | [![年度回顾封面](assets/images/example-p051-v2.png)](prompts/09-publishing.md#p051)<br>**[P051 · 年度回顾封面](prompts/09-publishing.md#p051)** |
| [![注意力主题编辑插画](assets/images/example-p052.png)](prompts/09-publishing.md#p052)<br>**[P052 · 注意力主题编辑插画](prompts/09-publishing.md#p052)** | [![植物水墨装饰画](assets/images/example-p053.png)](prompts/09-publishing.md#p053)<br>**[P053 · 植物水墨装饰画](prompts/09-publishing.md#p053)** | [![街区独立刊物封面](assets/images/example-p054.png)](prompts/09-publishing.md#p054)<br>**[P054 · 街区独立刊物封面](prompts/09-publishing.md#p054)** |

**可直接复制 · P049**

输入：此默认示例无需上传参考图。

```text
交付物：果园主题书籍封面。目标比例：2:3。模式：新建。
设计原创文学书封“THE QUIET ORCHARD”，虚构作者“MIRA VALE”。单棵剪纸梨树在浅桃纸上投出巨大深绿影，上方奶油衬线标题、下方作者。平面正封、触感纸纹，不做透视样机。
约束：仅所给书名作者，不加奖章、引言、ISBN或出版社标识。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只增加标题对比，不移动树或改字体。

**检查要点：** 逐字检查书名及缩略图可读性。

[本分类完整配方与使用说明](prompts/09-publishing.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-10-production"></a>

### 系列、本地化与制作交付 · 6

| | | |
| --- | --- | --- |
| [![商品四季系列](assets/images/example-p055.png)](prompts/10-production.md#p055)<br>**[P055 · 商品四季系列](prompts/10-production.md#p055)** | [![横版广告转竖版](assets/images/example-p056.png)](prompts/10-production.md#p056)<br>**[P056 · 横版广告转竖版](prompts/10-production.md#p056)** | [![广告本地化母版](assets/images/example-p057.png)](prompts/10-production.md#p057)<br>**[P057 · 广告本地化母版](prompts/10-production.md#p057)** |
| [![三参考图商品合成](assets/images/example-p058.png)](prompts/10-production.md#p058)<br>**[P058 · 三参考图商品合成](prompts/10-production.md#p058)** | [![老照片轻度修复](assets/images/example-p059.png)](prompts/10-production.md#p059)<br>**[P059 · 老照片轻度修复](prompts/10-production.md#p059)** | [![确认分镜扩展单镜头](assets/images/example-p060.png)](prompts/10-production.md#p060)<br>**[P060 · 确认分镜扩展单镜头](prompts/10-production.md#p060)** |

**可直接复制 · P055**

参考图（按顺序上传）：[1](assets/images/tideline-lamp.png)

```text
交付物：商品四季系列。目标比例：1:1。模式：编辑。
以图1为确认台灯广告，只把背景道具换为两片干枫叶和一小块折叠毛呢，制作一张秋季版。产品、品牌、位置、镜头不变，新道具匹配原光，保留标题区。
约束：每次只做一个变体，不拼四图、不改商品颜色。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 冬季同系列只把秋季道具换象牙针织布，保留灯和裁切。

**检查要点：** 用确认稿对比各季商品轮廓。

[本分类完整配方与使用说明](prompts/10-production.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-11-multilingual"></a>

### 多语言海报 · 12

| | | |
| --- | --- | --- |
| [![English · Repair workshop flyer](assets/images/example-l001.png)](prompts/11-multilingual.md#l001)<br>**[L001 · English · Repair workshop flyer](prompts/11-multilingual.md#l001)** | [![简体中文 · 城市慢生活海报](assets/images/example-l002.png)](prompts/11-multilingual.md#l002)<br>**[L002 · 简体中文 · 城市慢生活海报](prompts/11-multilingual.md#l002)** | [![日本語 · ベーカリーポスター](assets/images/komorebi-bakery.png)](prompts/11-multilingual.md#l003)<br>**[L003 · 日本語 · ベーカリーポスター](prompts/11-multilingual.md#l003)** |
| [![한국어 · 독립 서점 포스터](assets/images/example-l004.png)](prompts/11-multilingual.md#l004)<br>**[L004 · 한국어 · 독립 서점 포스터](prompts/11-multilingual.md#l004)** | [![Español · Cartel de café](assets/images/example-l005.png)](prompts/11-multilingual.md#l005)<br>**[L005 · Español · Cartel de café](prompts/11-multilingual.md#l005)** | [![Français · Affiche de marché](assets/images/example-l006.png)](prompts/11-multilingual.md#l006)<br>**[L006 · Français · Affiche de marché](prompts/11-multilingual.md#l006)** |
| [![Deutsch · Werkstattplakat](assets/images/example-l007.png)](prompts/11-multilingual.md#l007)<br>**[L007 · Deutsch · Werkstattplakat](prompts/11-multilingual.md#l007)** | [![Português · Cartaz de padaria](assets/images/example-l008.png)](prompts/11-multilingual.md#l008)<br>**[L008 · Português · Cartaz de padaria](prompts/11-multilingual.md#l008)** | [![العربية · ملصق مقهى](assets/images/example-l009.png)](prompts/11-multilingual.md#l009)<br>**[L009 · العربية · ملصق مقهى](prompts/11-multilingual.md#l009)** |
| [![हिन्दी · पुस्तकालय पोस्टर](assets/images/example-l010-v2.png)](prompts/11-multilingual.md#l010)<br>**[L010 · हिन्दी · पुस्तकालय पोस्टर](prompts/11-multilingual.md#l010)** | [![ไทย · โปสเตอร์ร้านชา](assets/images/example-l011.png)](prompts/11-multilingual.md#l011)<br>**[L011 · ไทย · โปสเตอร์ร้านชา](prompts/11-multilingual.md#l011)** | [![Русский · Афиша мастерской](assets/images/example-l012.png)](prompts/11-multilingual.md#l012)<br>**[L012 · Русский · Афиша мастерской](prompts/11-multilingual.md#l012)** |

**可直接复制 · L002**

输入：此默认示例无需上传参考图。

```text
生成一张2:3竖版城市慢生活海报。奶油纸背景，下半部为一把钴蓝折叠椅和一株斜伸入画的橄榄枝，午后自然光形成柔和长影，呈现真实布料纹理。上方大标题严格写“把周末还给自己”，下方小字“坐一会儿，也很好”，底部仅“慢慢生活”。中文采用清楚的现代黑体，标点完整，行距宽松，不加入英文、日期、地址或品牌。保持椅子结构可信。
```

**下一轮修改：** 后续只把椅子布面改为铁锈色，文字、橄榄枝和光线保持不变。

**检查要点：** 逐字核对简体字、逗号和行距；检查折叠椅支架。

[本分类完整配方与使用说明](prompts/11-multilingual.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-12-launch-examples"></a>

### 官方发布场景原创实践 · 7

| | | |
| --- | --- | --- |
| [![梗犬披风换装](assets/images/launch-dog-edit.png)](prompts/12-launch-examples.md#p061)<br>**[P061 · 梗犬披风换装](prompts/12-launch-examples.md#p061)** | [![虚构儿童人像换装](assets/images/launch-child-edit.png)](prompts/12-launch-examples.md#p062)<br>**[P062 · 虚构儿童人像换装](prompts/12-launch-examples.md#p062)** | [![卧室被套花色替换](assets/images/launch-bed-edit.png)](prompts/12-launch-examples.md#p063)<br>**[P063 · 卧室被套花色替换](prompts/12-launch-examples.md#p063)** |
| [![纪念卡城市文字替换](assets/images/launch-ticket-edit.png)](prompts/12-launch-examples.md#p064)<br>**[P064 · 纪念卡城市文字替换](prompts/12-launch-examples.md#p064)** | [![带符号立方体旋转](assets/images/launch-cube-edit.png)](prompts/12-launch-examples.md#p065)<br>**[P065 · 带符号立方体旋转](prompts/12-launch-examples.md#p065)** | [![旅行信息图单栏修改](assets/images/launch-travel-edit.png)](prompts/12-launch-examples.md#p066)<br>**[P066 · 旅行信息图单栏修改](prompts/12-launch-examples.md#p066)** |
| [![生日蜡烛数量修改](assets/images/launch-cake-edit.png)](prompts/12-launch-examples.md#p067)<br>**[P067 · 生日蜡烛数量修改](prompts/12-launch-examples.md#p067)** |  |  |

**可直接复制 · P061**

参考图（按顺序上传）：[1](assets/images/launch-dog-input.png)

```text
交付物：梗犬披风换装。目标比例：1:1。模式：编辑。
使用附上的梗犬照片作为唯一参考，只在肩背处添加森林绿布披风，用赭黄色系带在颈部固定。头部与耳朵完全露出。保持白色卷毛、眼周焦糖色斑纹、坐姿、四只爪子、体型、桃色背景、相机位置和光线。披风要顺着身体自然垂落，不新增帽子、文字或道具。
约束：只附上方标为 input 的输入图，不要同时附前后两图。仅修改要求的区域，逐一检查应保留部分。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只把披风改为酒红色，保留赭黄色系带和狗的特征。

**检查要点：** 披风与系带已添加，眼周斑纹、耳朵和爪子仍可识别，细部毛发有变化。

[本分类完整配方与使用说明](prompts/12-launch-examples.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-13-customizable-studio"></a>

### 可微调创作配方 · 6

| | | |
| --- | --- | --- |
| [![修理工坊纪实风肖像](assets/images/studio-workshop.png)](prompts/13-customizable-studio.md#p068)<br>**[P068 · 修理工坊纪实风肖像](prompts/13-customizable-studio.md#p068)** | [![四步手冲咖啡流程海报](assets/images/studio-brew.png)](prompts/13-customizable-studio.md#p069)<br>**[P069 · 四步手冲咖啡流程海报](prompts/13-customizable-studio.md#p069)** | [![口袋电车收藏包装](assets/images/studio-tram.png)](prompts/13-customizable-studio.md#p070)<br>**[P070 · 口袋电车收藏包装](prompts/13-customizable-studio.md#p070)** |
| [![手工灯塔岛微缩场景](assets/images/studio-lighthouse-edit.png)](prompts/13-customizable-studio.md#p071)<br>**[P071 · 手工灯塔岛微缩场景](prompts/13-customizable-studio.md#p071)** | [![针织纪念物贺卡](assets/images/studio-card.png)](prompts/13-customizable-studio.md#p072)<br>**[P072 · 针织纪念物贺卡](prompts/13-customizable-studio.md#p072)** | [![陶艺工作室编辑拼贴](assets/images/studio-collage.png)](prompts/13-customizable-studio.md#p073)<br>**[P073 · 陶艺工作室编辑拼贴](prompts/13-customizable-studio.md#p073)** |

**可直接复制 · P068**

输入：此默认示例无需上传参考图。

```text
交付物：修理工坊纪实风肖像。目标比例：3:2。模式：新建。
为虚构社区修理工坊制作3:2横向编辑摄影图。一位五十多岁的成年女性，银色短卷发，穿芥末黄色帆布围裙，坐在带使用痕迹的桦木工作台前，手工缝补深蓝帆布背包开裂的接缝。相机与桌面接近同高，以四分之三角度看见双手和针线。桌上仅放奶油色线轴、圆头剪刀和一盏台灯。左侧大窗透入阴天柔光，鼠尾草绿墙壁与整齐工具板虚化在后方。保留自然皮肤、磨损布纤维和轻微胶片颗粒。人物位于右侧，左上留出后期排字空间。这是虚构摆拍，不是历史影像。
约束：保持手部接触关系与可见接缝合理，不加文字或其他人物。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只将围裙由芥末黄改为柔和梅紫，保留人物、姿势、背包、工具、光线和构图。

**检查要点：** 人物、背包接缝和窗光符合主要要求；前景工作台多出碗与布料，手指和针的接触需放大检查。

[本分类完整配方与使用说明](prompts/13-customizable-studio.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-14-sketch-to-story"></a>

### 从草图到故事：英文工作流配方 · 12

| | | |
| --- | --- | --- |
| [![One sketch, four concept directions](assets/images/example-p074.png)](prompts/14-sketch-to-story.md#p074)<br>**[P074 · One sketch, four concept directions](prompts/14-sketch-to-story.md#p074)** | [![Bedroom plan to interior concept](assets/images/example-p075.png)](prompts/14-sketch-to-story.md#p075)<br>**[P075 · Bedroom plan to interior concept](prompts/14-sketch-to-story.md#p075)** | [![Doodle character across four media](assets/images/example-p076.png)](prompts/14-sketch-to-story.md#p076)<br>**[P076 · Doodle character across four media](prompts/14-sketch-to-story.md#p076)** |
| [![English tea collection editorial sheet](assets/images/example-p077.png)](prompts/14-sketch-to-story.md#p077)<br>**[P077 · English tea collection editorial sheet](prompts/14-sketch-to-story.md#p077)** | [![Headline replacement without layout drift](assets/images/example-p078.png)](prompts/14-sketch-to-story.md#p078)<br>**[P078 · Headline replacement without layout drift](prompts/14-sketch-to-story.md#p078)** | [![Four-region portrait correction brief](assets/images/example-p079.png)](prompts/14-sketch-to-story.md#p079)<br>**[P079 · Four-region portrait correction brief](prompts/14-sketch-to-story.md#p079)** |
| [![Portrait continuity through three revisions](assets/images/example-p080.png)](prompts/14-sketch-to-story.md#p080)<br>**[P080 · Portrait continuity through three revisions](prompts/14-sketch-to-story.md#p080)** | [![Logo redesign with an explicit brand brief](assets/images/example-p081.png)](prompts/14-sketch-to-story.md#p081)<br>**[P081 · Logo redesign with an explicit brand brief](prompts/14-sketch-to-story.md#p081)** | [![Reference-led branded apparel presentation](assets/images/example-p082.png)](prompts/14-sketch-to-story.md#p082)<br>**[P082 · Reference-led branded apparel presentation](prompts/14-sketch-to-story.md#p082)** |
| [![Sixteen-pose action reference sheet](assets/images/example-p083.png)](prompts/14-sketch-to-story.md#p083)<br>**[P083 · Sixteen-pose action reference sheet](prompts/14-sketch-to-story.md#p083)** | [![Nine-shot music-video concept board](assets/images/example-p084.png)](prompts/14-sketch-to-story.md#p084)<br>**[P084 · Nine-shot music-video concept board](prompts/14-sketch-to-story.md#p084)** | [![Sixteen-shot two-character narrative board](assets/images/example-p085.png)](prompts/14-sketch-to-story.md#p085)<br>**[P085 · Sixteen-shot two-character narrative board](prompts/14-sketch-to-story.md#p085)** |

**可直接复制 · P074**

此配方提供英文提示词，可直接复制使用。

参考图（按顺序上传）：[1](assets/images/curve-input.png)

```text
Asset: One sketch, four concept directions. Target aspect ratio: 1:1. Mode: edit.
Use the attached line sketch as a silhouette and composition reference. Create one square concept board with exactly four equal panels in a 2-by-2 grid. Keep the sketch's dominant curve recognizable in every panel, including its direction, major bend and approximate position; the stroke is a shape guide, not an object to print on top. Interpret it as four distinct concepts: upper left, a bent-plywood reading bench; upper right, a ceramic pouring vessel; lower left, a folded-paper stage canopy; lower right, a luminous glass sculpture. Give each panel one primary object, a quiet environment and lighting appropriate to its material. Maintain equal gutters and similar object scale so the alternatives can be compared. Do not add captions, arrows, extra panels or unrelated decorative marks. These are four explorations, not four views of one design.
Constraints: Attach one sketch you own. Preserve its distinctive bend without forcing identical materials. Generate each selected panel separately for final production.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

**下一轮修改：** Develop only the upper-left bench concept into one landscape image. Preserve the approved bent silhouette; replace the background with a quiet library interior.

**检查要点：** Count four panels; trace the original curve in each; check that all four object categories differ.

[本分类完整配方与使用说明](prompts/14-sketch-to-story.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-15-x-community"></a>

### X 社区实用场景 · 6

| | | |
| --- | --- | --- |
| [![Ingredient-built bakery lettering](assets/images/example-p086-v2.png)](prompts/15-x-community.md#p086)<br>**[P086 · Ingredient-built bakery lettering](prompts/15-x-community.md#p086)**<br>修订后成图；完整过程见配方 | [![Six-frame fragrance launch board](assets/images/example-p087.png)](prompts/15-x-community.md#p087)<br>**[P087 · Six-frame fragrance launch board](prompts/15-x-community.md#p087)** | [![Editorial mobility concept poster](assets/images/example-p088.png)](prompts/15-x-community.md#p088)<br>**[P088 · Editorial mobility concept poster](prompts/15-x-community.md#p088)** |
| [![Paper-window weekend destination card](assets/images/example-p089.png)](prompts/15-x-community.md#p089)<br>**[P089 · Paper-window weekend destination card](prompts/15-x-community.md#p089)** | [![Sketch-to-building concept reveal](assets/images/example-p090.png)](prompts/15-x-community.md#p090)<br>**[P090 · Sketch-to-building concept reveal](prompts/15-x-community.md#p090)** | [![Community picnic announcement](assets/images/example-p091.png)](prompts/15-x-community.md#p091)<br>**[P091 · Community picnic announcement](prompts/15-x-community.md#p091)** |

**可直接复制 · P087**

此配方提供英文提示词，可直接复制使用。

输入：此默认示例无需上传参考图。

```text
Asset: Six-frame fragrance launch board. Target aspect ratio: 3:2. Mode: generate.
Create a static six-panel presentation board for a fictional cedar fragrance named NORTH ROOM. Use a precise three-column, two-row grid on warm gray paper. The product is a squat amber rectangular glass bottle with a brushed silver cylindrical cap and an ivory NORTH ROOM label. Read left to right: full bottle on slate; close-up of the cap seam; side light through amber liquid; uncapped bottle with the cap resting beside it; atomizer releasing a fine mist; final bottle beside a small cedar block. Number the frames 01 through 06 in identical outside gutters. Keep the same bottle geometry and studio surface throughout.
Constraints: A single still image, not a video or GIF. Six panels only. No floating cap, invented performance claims or additional text.
Render only explicitly requested image text. Do not add unrelated logos, signatures or captions.
```

**下一轮修改：** Correct only panel 05 so the mist originates at the atomizer; preserve all other panels and gutters.

**检查要点：** Count six frames, compare caps and labels, inspect mist origin. Animation and sound require a separate production step.

[本分类完整配方与使用说明](prompts/15-x-community.md) · [回到分类目录](#按实际工作选场景)

<a id="showcase-16-videoweb-x-creators"></a>

### VideoWeb 创作者 X 案例 · 3

| | | |
| --- | --- | --- |
| [![时装短片服装概念](assets/images/p092-videoweb.png)](prompts/16-videoweb-x-creators.md#p092)<br>**[P092 · 时装短片服装概念](prompts/16-videoweb-x-creators.md#p092)** | [![复古短片开场帧](assets/images/p093-videoweb.png)](prompts/16-videoweb-x-creators.md#p093)<br>**[P093 · 复古短片开场帧](prompts/16-videoweb-x-creators.md#p093)** | [![耳机发布主视觉](assets/images/p094-videoweb.png)](prompts/16-videoweb-x-creators.md#p094)<br>**[P094 · 耳机发布主视觉](prompts/16-videoweb-x-creators.md#p094)** |

**可直接复制 · P092**

输入：此默认示例无需上传参考图。

```text
交付物：时装短片服装概念。目标比例：3:4。模式：新建。
为虚构时装短片制作竖版3:4服装概念图。一位成年模特穿青绿色短雨衣、象牙白阔腿裤和深色短靴，完整展示全身和双脚。用清晰墨线配合克制的水彩晕染，背景为暖白纸面。人物轮廓清楚，头顶预留后期加标题的空白。人物朝左侧四分之三方向，双手放松；雨衣门襟和口袋应可辨认。这是服装设计插画，不是真人照片。
约束：不要文字、标识或其他人物；不要裁掉双脚或遮住衣服结构。
只渲染明确要求的图中文字，不添加无关标识、签名或说明。
```

**下一轮修改：** 只把雨衣改成赭黄色，保留姿势、面部、裤子、靴子、墨线风格及标题留白。

**检查要点：** 检查轮廓、人体或产品结构、标题留白及画面一致性。后续修改和视频建议尚未执行。

[本分类完整配方与使用说明](prompts/16-videoweb-x-creators.md) · [回到分类目录](#按实际工作选场景)

<!-- END GENERATED SHOWCASE -->

## VideoWeb 新增案例

| 时装短片服装概念 | 复古短片开场帧 | 耳机发布主视觉 |
| --- | --- | --- |
| [![服装概念](assets/images/p092-videoweb.png)](prompts/16-videoweb-x-creators.md#p092) | [![复古开场](assets/images/p093-videoweb.png)](prompts/16-videoweb-x-creators.md#p093) | [![耳机广告](assets/images/p094-videoweb.png)](prompts/16-videoweb-x-creators.md#p094) |

[复制3条新增双语提示词](prompts/16-videoweb-x-creators.md) · [视频演示导览](docs/video-guide.md) · [从图片到视频](docs/videoweb-workflow.md)

保留源库全部103条配方，新增3条从X案例扩展的原创简报及各自生成图。X原生页面要求登录，本次通过公开镜像核对作者、内容和素材地址，并在配方中注明。复古开场图的左墙仍有装饰物，未完全满足留白要求，已记录在图片检查说明中。

## 新增：官方发布场景原创实践

参照 [OpenAI 发布文章](https://openai.com/index/introducing-chatgpt-images-2-5/) 的实用场景，新增7条中英双语配方、14张原创图片：宠物披风、虚构儿童换装、被套花色、纪念卡文字、立方体旋转、行程单栏修改与蜡烛计数。每组附输入图、编辑图、实际提示词和检查结果；立方体存在几何偏差，已如实标明。

[查看7组前后对照](docs/launch-examples.md) · [复制P061–P067提示词](prompts/12-launch-examples.md)

## 新增：中文文章转化的英文工作流

根据文章提取并扩展P074–P085共12条英文配方，覆盖草图、复杂英文排版、局部修图、连续编辑、品牌周边和分镜。配方、图内文案与使用指南均以英文编写，使用新虚构品牌和故事；现已全部配有新生成示例，编辑类同时提供输入图和实际效果说明。

[复制12条英文提示词](prompts/14-sketch-to-story.md) · [查看来源与场景对应](docs/sketch-to-story.md)

## 新增：可微调创作配方

新增P068–P073共6条中英双语提示词，每条有3组可调整项与保留条件，覆盖工坊纪实照、手冲流程、玩具包装、灯塔微缩、纪念贺卡和陶艺拼贴。附7张新图，包括一次真实屋顶换色编辑。

[复制可微调提示词](prompts/13-customizable-studio.md) · [查看微调示例与来源说明](docs/customizable-studio.md)

## 从一张好看的图，到可以继续修改的作品

商业创作经常需要“产品不变，只换背景”“中文换成日文，版式不要乱”“同一角色继续下一镜”。因此，本库不止描述风格，还明确任务、构图、材质、图中文字、保留项、后续修改与验收标准。

当前版本包含 **106 条配方、16 个场景包**：76 条完整中英双语核心提示词、18条英文工作流配方，以及12条本地语言配方。翻译、追问和变体不重复计数。**全部106条现已配图**，共143张PNG（源库139张，本次新增4张），包含生成结果、编辑参考图、修改过程与封面。源库已为全部原始配方配图，本分支保留这些记录，并补充新增配方的使用说明。可直接浏览[完整图片画廊](docs/gallery.md)。

## 新增：玩法路线与版本对比

- [10条实用玩法路线](docs/playbook.md)：从商品母版、宠物写真到故事分镜，按素材选择并逐步执行。
- [GPT Image 2 与 Images 2.5 升级对比](docs/images-2-vs-2-5.md)：解释Flare、Sunburst的区别，以及哪些能力属于改进而非首次支持。

两份指南复用现有配方和图片，不增加配方计数，不冒充模型对比实测。

README现提供 **16个语言／地区版本**，默认英文。各语言入口包含使用指引、示例提示词和平台资源；原有76条核心配方为完整中英双语，新工作流包以英文提供。[查看语言覆盖范围](docs/localization-guide.md#readme-language-coverage)。

## 源库生成示例

| 商品广告 | 日英双语烘焙海报 |
| --- | --- |
| ![台灯产品广告：深蓝金属与珊瑚展台](assets/images/tideline-lamp.png) | ![日英双语面包店海报：焼きたての朝](assets/images/komorebi-bakery.png) |
| [P001 提示词](prompts/01-product.md#p001) | [L003 提示词](prompts/11-multilingual.md#l003) |

| 修补纸月亮故事 | 社区阅读室 |
| --- | --- |
| ![机器人修补纸月亮六格分镜](assets/images/paper-moon-story.png) | ![旧工坊改造社区阅读室概念图](assets/images/reading-room.png) |
| [P037 提示词](prompts/07-stories-games.md#p037) | [P043 提示词](prompts/08-spaces.md#p043) |

示例来自 Codex 内置生图工具，工具未返回底层模型ID，因此**不作为 Flare / Sunburst 的指定型号实测或横向评测**。六格故事第三格提前出现缝线；阅读室增加了杯子和花瓶。这些可见偏差均在[生成记录](docs/generation-log.md)中说明。

## 同一张广告：先改颜色，再改标题

| 原稿 | 第一轮：底座换绿 | 第二轮：只换标题 |
| --- | --- | --- |
| ![原始蓝色台灯](assets/images/tideline-lamp.png) | ![保留标题的绿色台灯](assets/images/tideline-lamp-jade.png) | ![保留绿色并更换标题](assets/images/tideline-lamp-copy.png) |

第二轮以第一轮绿色成图为输入，能直观看到确认稿如何继续修改。细微表面纹理仍有变化，灯杆也随底座变绿，不能理解为像素级不变。[查看完整过程与验收方法](docs/editing-case-study.md)。

## X 社区提示词与原图来源

新增 **P086–P091 共6条英文配方**，覆盖食材文字、香水分镜、交通工具海报、纸艺旅行卡、建筑草图演变与野餐邀请。每条都附 X 作者、原帖、原图预览、改写说明、微调参数和验收要点。

原图为第三方来源参考，不是改写提示词的生成结果，也不纳入本库 MIT 许可；本库改写后的6条X场景也已单独生成配图，计入143张原创图片资产。模型名称来自原帖作者说明，未经独立验证。

[查看提示词及来源图片](prompts/15-x-community.md) · [英文使用指南](docs/x-community.md)

## 免费 GPT Image 2.5 AI 工具，无需注册

想直接试用本库提示词，可以从以下在线工具开始。各页面均介绍了免费、免注册的 ChatGPT Images 2.5 文生图和单张参考图编辑：输入提示词或上传一张图片，选择比例，再根据结果继续调整。

| 工具 | 简介 | 推荐尝试 |
| --- | --- | --- |
| [VideoWeb AI free gpt image 2.5](https://videoweb.ai/free-gpt-image-2-5/) | 适合影片开场概念、转场参考帧、广告主视觉和场景氛围研究。提示词中明确机位与光线，可添加单张参考图，先确认静态画面，再用于视频前期策划。 | [故事与分镜](prompts/07-stories-games.md) |
| [Flaq.ai free gpt image 2.5](https://flaq.ai/free-chatgpt-images-2-5/) | 源库团队提供的另一个工具，可尝试产品图、海报、写实场景和单图修改。页面还连接 flaq.ai 的创作工具与模型 API，方便将确认后的创意进一步接入应用流程。 | [P001 产品广告](prompts/01-product.md#p001) |
| [UGC Maker free gpt image 2.5](https://ugcmaker.org/free-chatgpt-images-2-5/) | 面向创作者内容、UGC 广告概念、产品故事和社交媒体图片，可先探索广告主视觉或封面，再继续制作其他内容。 | [广告、社媒与创作者封面](prompts/02-social.md) |
| [Best Image AI free gpt image 2.5](https://bestimage.ai/free-chatgpt-images-2-5/) | 通用文生图与单图编辑入口，适合电商、海报和视觉概念探索，可尝试方形、竖版和横版等不同构图。 | [P070 收藏玩具包装](prompts/13-customizable-studio.md#p070) |
| [HeyDream free gpt image 2.5](https://heydream.im/free-chatgpt-images-2-5/) | 适合写实场景、照片风格调整、背景编辑与初步分镜构思；页面还提供独立图生视频工具入口，方便继续探索动态内容。 | [P071 灯塔微缩场景](prompts/13-customizable-studio.md#p071) |
| [AITryOn free gpt image 2.5](https://aitryon.art/free-chatgpt-images-2-5/) | 适合服装概念、时尚人像、配饰和商品图。生成或编辑时明确服装、材质、姿势与背景，有助于表达具体造型方向。 | [P079 人像局部修改](prompts/14-sketch-to-story.md#p079) |
| [Flyne AI free gpt image 2.5](https://flyne.ai/free-gpt-image-2-5/) | 适合产品发布概念图、醒目社交配图、插画分镜和情绪板。可从文字或单张参考图开始，通过九种画幅比例安排主体位置与标题留白。 | [产品广告](prompts/01-product.md) |
| [Sea Imagine AI free gpt image 2.5](https://seaimagine.com/free-gpt-image-2-5/) | 适合艺术构图、建筑环境、海报布局和配色探索。通过文字或单张参考图引导画面，明确留白、材质与光线，比较不同画幅中的视觉方向。 | [空间与建筑](prompts/08-spaces.md) |
| [Fylia AI free gpt image 2.5](https://fylia.ai/free-gpt-image-2-5/) | 适合插画人像、微缩绘本场景、生活方式图片及纸艺色彩实验。可输入文字或使用单张参考图，根据故事需要选择横版、方形或竖版构图。 | [人物与宠物](prompts/03-people-pets.md) |
| [SeeVido AI free gpt image 2.5](https://seevido.com/free-gpt-image-2-5/) | 适合角色场景、产品预热图、旅行插画和季节性社交配图。支持文字或单张参考图引导；修改时明确需要保留的表情、产品细节与背景元素。 | [广告与社交配图](prompts/02-social.md) |
| [VO4 AI free gpt image 2.5](https://vo4.org/free-gpt-image-2-5/) | 适合电影感场景、动作参考帧、科幻环境和镜头构图研究。先明确视点、主体和照明，再从九种画幅中选择合适比例，为镜头规划制作静态参考图。 | [草图到故事工作流](prompts/14-sketch-to-story.md) |
| [Chat 4O AI free gpt image 2.5](https://chat4o.ai/free-gpt-image-2-5/) | 适合将文字想法转成演示文稿配图、教学插画、项目情绪板和故事图片。从提示词或单张参考图开始，为幻灯片文案预留空间，并检查图像是否准确表达主题。 | [信息图与教学插图](prompts/05-information.md) |

**使用方法：**复制配方并替换虚构内容；编辑任务上传参考图，生成后检查并保存确认稿，再使用后续修改指令。需要多张参考图的配方，应选择支持相应输入数量的工具。

**可用性说明：**原有5个页面于 **2026-09-14** 核对，新增7个页面于 **2026-09-16** 核对，本次未实测生成。新增工具的页面均说明生成前需完成验证，免注册不代表无需验证。免费指所链接的工具，不代表高级功能、视频服务或 API 一并免费；当前可用性与限制以各站规则为准。

## 针对 Images 2.5 做了哪些细化？

官方模型文档将 **Flare** 定位为快速日常生图，将 **Sunburst** 用于更重视编辑精度的工作流，均接受文字和图像输入。参见 [Flare 模型页](https://developers.openai.com/api/docs/models/gpt-image-2.5-flare)及 [Sunburst 模型页](https://developers.openai.com/api/docs/models/gpt-image-2.5-sunburst)。

本库据此强化参考图分工、保留项、多轮确认稿、局部换字和系列一致性。这是提示词设计策略，不是成功率承诺；[版本说明](docs/model-notes.md)区分官方参数与尚未验证的假设。

## 从图片到视频

先生成并检查静态图，再将选定图片用于独立的视频工具。GPT Image 2.5 负责图片；分镜图本身不是视频。见[VideoWeb 创作流程](docs/videoweb-workflow.md)。

## 常见问题

### 可以免费使用吗？

仓库原创内容采用 [MIT](LICENSE) 开源许可。最终图片中的人物、品牌、输入素材及其他第三方权利仍需结合实际用途检查；虚构演示名称不等于经过商标检索。

### 106条都已经生成验证了吗？

全部106条已有对应生成示例，其中76条双语配方（源库73条、本次新增3条）、18条英文工作流配方、12条本地语言配方。配图不代表所有要求均完美达成；每张图附有实际效果说明，建议中的后续修改只有单独记录结果时才表示已执行。

### 可以直接用作商业成品吗？

可作为创作起点，但需要检查文字、人物、产品外形和用途。界面图不是可运行软件；字标不是矢量文件；数据图、施工图和长篇排版需要相应制作工具复核。

### 如何避免多轮修改越改越乱？

每次只改一个变量，重复必须保留的内容，传入最近一次确认图。如有漂移，回到确认图重新修改。不要依赖新对话记住以前的图。

### 是 OpenAI 官方项目吗？

不是。这是 **VideoWeb AI 维护的独立开源项目**，与 OpenAI 无隶属或背书关系。

## 参与贡献

欢迎提交原创场景、语言审校和带真实生成记录的图片。请阅读[贡献规范](CONTRIBUTING.md)与[原创规范](docs/originality.md)。

[发布与维护资料](docs/seo.md) · [Quality review / 质量复查](docs/quality-review.md)

## 关于 VideoWeb AI

VideoWeb AI 面向图片和视频创作者。这个分支保留源库完整配方与图片记录，并持续补充视频封面、分镜和社区案例。原始内容归属与同步方法见[源库说明](docs/upstream.md)。

## 联盟推广合作

我们支持联盟推广合作，欢迎教程作者、视频创作者和工具评测者通过 [VideoWeb AI 联盟计划](https://videoweb.ai/affiliate-program/)加入。

首笔有效付费订单佣金为20%；注册后60天内的后续有效付费订单为10%。具体资格、退款处理和结算规则以联盟页面为准。

## 许可

[MIT](LICENSE) © 2026 Flaq AI；VideoWeb AI 品牌适配与新增内容。第三方素材另行标注。
