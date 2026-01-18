# 1 Skeleton-First Design
## 1.1 Description
> Design:（Priority / Category / Domain / Template）
> 本文档定义了 python_tools 的**根本架构思想**。  
> 它不是“目录说明”，而是一套**代码坐标系统**。  
> python_tools 中的每一行代码，都必须能映射到这套坐标中。

---

## 1.2 核心思想（第一性原则）

python_tools **不是**围绕：

- 功能
- 第三方库
- 文件或模块

来组织的。

而是围绕一个**四维骨架坐标系**：

```
<priority>/<category>/<domain>/<pattern> [+ context]

priority ∈ { core, framework, modules }
category ∈ { audio, video, math, signal, time , web ...}		
domain	 ∈ { fastapi, ffmpeg, std ... }
pattern  ∈ { backend, model, service, repository, mapper ...}
```



# 2 四个维度的定义
## 2.1 《priority》
\<priority\> —— 依赖优先级（纵向维度，最重要）

决定「谁可以依赖谁」
```txt
priority ∈ { core, framework, modules }
```
| priority  | 含义       | 依赖规则                |
| --------- | -------- | ------------------- |
| modules   | 能力 / 系统层 | 依赖 core + framework |
| framework | 逻辑 / 算法层 | 只能依赖 core           |
| core      | 语言 / 语义层 | 不依赖任何层              |

铁律：
- 依赖只能 向下
- 不允许环形依赖
- modules --(使用)-→ frame / core ✅
- core → modules ❌


-----
**维度骨架映射**
> 可以剪枝实现特定含义，但不能

| priority   | 维度骨架 |
| ---------- | --------------- |
| modules    |  \<priority>/\<category>/\<domain>/\<pattern> |
| framework  | \<priority>/\<category>/\<pattern> |
| core       |  \<priority>/\<category>/\<pattern> |



## 2.2 《category》
回答问题：这是哪一类能力？
```
category ∈ {	
	audio,	console,	data,		filesystem,		
	video,	math,		signal,		string,		time, 
	text,	network,	process ...
}
```

## 2.3 《domain》
<\domain\> —— 技术域 / 世界边界 / 来源
```
domain ∈ { sdl, ffmpeg, stl, std, chrono, posix, win32, custom, none }
```

规则：
- core 通常 没有 domain
- framework 只做抽象层面的 domain 投射
- modules 必须绑定 具体 domain

## 2.4 《pattern》
\<pattern\> —— 组织 / 执行模板

回答问题：代码按什么结构和模式存在？
代码应当按什么结构和模式存在？

pattern 描述的是可复用的结构协议（structural protocol），
它定义代码如何被组织、约束与协作，而不承载任何业务语义。

pattern ≠ business

pattern = structure + rule + responsibility

### 2.4.0 pattern 总集合

```
pattern ∈ {
  // ───────── core : 原生物（What exists）
  primitive,
  base,
  types,
  memory,
  utility,
  meta,
  error,
  concurrency,
  config,

  // ───────── framework : 原生行为（How to think）
  model,
  algorithm,
  api,
  service,
  policy,
  pipeline,

  // ───────── modules : 外生世界（Where reality happens）
  backend,
  mapper,
  adapter,
  driver,
  device,
  platform,
  detail,
  benchmark,
  tuning
}

```

| 标记 | 含义             |
| -- | -------------- |
| ✅  | 允许，且是推荐用法      |
| ⚠️ | 有条件允许（需严格遵守定义） |
| ❌  | 明确禁止           |


pattern × priority 是一个受限矩阵

⚠️ 不是每个 priority 都能使用所有 pattern

-----

**Core（原生物）**
| pattern     | core | framework | modules | 说明                 |
| ----------- | :--: | :-------: | :-----: | ------------------ |
| primitive   |   ✅  |     ❌    |    ❌    | 语义原子（不可再分）|
| base        |   ✅  |     ❌    |    ❌    | 语言级基础              |
| types       |   ✅  |     ⚠️    |    ❌    | framework 仅使用      |
| memory      |   ✅  |     ⚠️    |    ❌    | RAII / ownership   |
| utility     |   ✅  |     ⚠️    |    ⚠️    | modules 仅内部 helper |
| meta        |   ✅  |     ⚠️    |    ❌    | traits / constexpr |
| error       |   ✅  |     ⚠️    |    ⚠️    | modules 仅错误映射      |
| concurrency |   ✅  |     ⚠️    |    ❌    | 无 OS / 设备          |
| config      |   ✅  |     ⚠️    |    ⚠️    | modules 只读         |

**Framework（原生行为）**
| pattern   | core | framework | modules | 说明               |
| --------- | :--: | :-------: | :-----: | ---------------- |
| model     |   ❌  |     ✅     |    ⚠️   | modules 仅 shadow |
| algorithm |   ❌  |     ✅     |    ❌    | 世界无关             |
| api       |   ❌  |     ✅     |    ⚠️   | modules 仅薄入口     |
| service   |   ❌  |     ✅     |    ❌    | 不触碰世界            |
| policy    |   ❌  |     ✅     |    ❌    | 编译期策略            |
| pipeline  |   ❌  |     ✅     |    ⚠️   | modules 仅 glue   |

**Modules（外生世界）**

| pattern   | core | framework | modules | 说明            |
| --------- | :--: | :-------: | :-----: | ------------- |
| backend   |   ❌  |     ❌     |    ✅    | 世界执行体         |
| mapper    |   ❌  |     ❌     |    ✅    | 世界 ↔ 抽象翻译     |
| adapter   |   ❌  |     ❌     |    ✅    | 第三方接口适配       |
| driver    |   ❌  |     ❌     |    ✅    | OS / 硬件       |
| device    |   ❌  |     ❌     |    ✅    | 设备实例          |
| platform  |   ❌  |     ❌     |    ✅    | win32 / posix |
| detail    |   ❌  |     ❌     |    ✅    | 私有实现          |
| benchmark |   ❌  |     ⚠️     |    ✅    | 性能评估          |
| tuning    |   ❌  |     ⚠️     |    ✅    | 性能 / 参数       |



## 2.5 [+ content]
content = 内部细分结构