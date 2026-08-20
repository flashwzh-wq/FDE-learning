# FDE 学习项目

这是我为零基础转行「腾讯云智慧零售 FDE 售前顾问」而搭建的学习仓库，
记录从 Python 入门到 AI 应用落地的完整过程。

## 学什么

- **Python 基础**：变量、列表、字典、循环、函数
- **文件与数据**：读写文件、JSON 数据处理
- **版本管理**：Git + GitHub 协作
- **进阶方向**：CLI 工具、API 调用、数据库、Web 框架、AI 应用

## 项目作品

| 项目 | 说明 |
|---|---|
| `alert_push.py` | 数据异常监控：抓文章 → 筛超长标题 → 推送告警（首个可下载作品） |
| `competitor_report.py` | 竞品数据分级 → 双报告输出 |
| `day10_final.py` | 嵌套字典 → JSON 导出 + 极值分析 |
| `day11_final.py` | 客户拜访满意度分析器 |
| `review_weekly.py` | 综合：函数 + 字典 + 擂台法 + 分类 + JSON |

## 首个完整作品：alert_push.py

数据异常监控小工具——抓取文章列表，找出标题超过 `--limit` 字的异常文章，统计数量并自动推送一条告警。

**怎么装**（只需一次）：

```bash
pip install -r requirements.txt
```

**怎么跑**：

```bash
# 默认阈值 70 字
python alert_push.py

# 自定义阈值，比如标题超过 75 字才算异常
python alert_push.py --limit 75
```

## 学习日志

每日学习记录见 `.workbuddy/memory/`，错题复盘见 `错题本.md`。
