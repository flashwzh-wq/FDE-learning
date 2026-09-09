# 从零基础到 FDE 售前：我的 12 周转型实战仓库

> 腾讯在职 · 企业微信品牌经理 · 零基础自学 Python，目标 2026 年 11 月拿下腾讯云认证。

## 我在做什么

- **身份**：腾讯在职，企业微信品牌经理出身，正在转型技术售前
- **学习方向**：云技术售前 / FDE 方案（技术 × 行业场景）
- **方式**：零基础自学 Python，工作日每天 1 小时，已连续推进 5 周
- **方法论**：每学一个模块，产出一个能跑、能写进简历的作品——不注水、不赶工

## 学习路线（12 周 · 8 条简历行）

| 周 | 模块 | 产出 | 状态 |
|---|---|---|---|
| W1-W4 | Python 基础 · 字典/JSON | 竞品分级报告、客户拜访分析器 | 完成 |
| W5 | Git + GitHub | 本仓库（完整提交历史） | 完成 |
| W6 | CLI 工具 argparse | 竞品数据处理命令行工具 | 完成 |
| W7 | API 调用 requests | 企业微信数据异常自动推送 | 完成 |
| W8 | SQLite 数据库 | 代码字典、客户台账 | 完成 |
| W9 | Web 框架 FastAPI | 代码字典 Web API（查询 + 新增 + 删除 + 更新） | 完成 |
| W10-11 | RAG 应用 | 企业知识库问答 Web Demo | 进行中（核心链路已跑通） |
| W12-13 | Agent + Streamlit | 会议纪要自动生成工具 | 计划中 |
| W14 | 云部署 Docker | 应用容器化上腾讯云 | 计划中 |
| W15-16 | 简历 + 面试 | 简历重写 + 模拟面试 | 计划中 |

## 项目作品

每个项目对应一句「做了什么 + 解决什么问题 + 输出什么」。

### 代码字典 v2（`code_dict.py`）· W8

用 Python + SQLite 开发的代码模板速查工具，支持关键词检索、增删改查、防重复插入。

```bash
python code_dict.py --keyword 数据库              # 按关键词查模板
python code_dict.py --add 新模板 --addcode "..."   # 手动新增模板
```

### 客户台账（`customer_book.py`）· W8

用 Python + SQLite 搭建的客户台账，支持新增、删除、列表、按行业统计客户分布。

```bash
python customer_book.py --stats                  # 按行业统计，如 {'餐饮': 2, '零售': 1}
```

### 企业知识库问答（`app.py` + `资料.txt`）· W10

用 Python + Streamlit + Ollama 搭建的本地企业知识库问答 Demo。资料维护在独立的 `资料.txt`：程序读取资料后，用 `bge-m3` 完成向量检索，再由 `qwen2.5:3b` 根据命中资料生成回答。

- 支持语义检索、回答生成和命中资料展示；
- 支持空问题提示，知识库无相关资料时明确说不知道；
- 新增资料只需编辑 `资料.txt`，无需修改 Python 代码；
- 当前内置 6 条企业微信操作资料。

```bash
streamlit run app.py
```

浏览器打开 `http://localhost:8501` 后即可提问。

### 数据异常监控（`alert_push.py`）· W7

调用企业微信 API，抓取文章列表、筛出超长标题、自动推送告警。

### 竞品数据分级（`competitor_report.py`）· W6

读竞品数据 → 按规则分级 → 输出双报告。

## 怎么跑

基础依赖：

```bash
pip install -r requirements.txt
```

运行企业知识库问答 Demo 前，还需要安装并启动 Ollama，并下载两个本地模型：

```bash
ollama pull bge-m3
ollama pull qwen2.5:3b
streamlit run app.py
```

然后在浏览器打开 `http://localhost:8501`。运行期间需要保持 Streamlit 和 Ollama 服务可用。

## 认证与下一步

- 腾讯云从业者认证：备考中（线上随时考，60 题 / 90 分钟 / 70 分过）
- 每日学习记录见 `.workbuddy/memory/`，错题复盘见 `错题本.md`
