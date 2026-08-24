# ============================================================
#  代码模板库（泽华的活笔记本 · 静态版）
# ------------------------------------------------------------
#  用法：这个文件不是拿来「运行」的，是拿来「查」和「抄」的。
#  要用哪段，选中复制到你的新文件里，再把表名/字段/URL 换成你的。
#
#  ⚠️ 不要整文件运行 —— 很多段需要真实数据，一运行就会报错。
#  正确姿势：打开 → 找到对应模板 → 复制 → 粘贴到新文件 → 改。
# ============================================================


# ══════════════════════════════════════════════════════════
# 模板 1 ｜ SQLite 完整流程（建表 → 插入 → 更新 → 删除 → 查询）
# 场景：想把数据存到本地数据库，增删改查都要用
# 记忆点：连接 → 游标 → 执行 → 提交 → 关闭；增删改必须 commit
# ══════════════════════════════════════════════════════════
import sqlite3
from datetime import date

conn = sqlite3.connect("你的库名.db")   # 连接（没有这个文件就自动建）
c = conn.cursor()                        # 游标，靠它发命令

# 1) 建表（IF NOT EXISTS = 表已存在就不重建，重复跑不报错）
c.execute("""CREATE TABLE IF NOT EXISTS 表名(
    id INTEGER PRIMARY KEY,
    字段1 TEXT,
    字段2 TEXT
)""")

# 2) 插入（? 占位符 + 元组打包，元组一个值时记得加逗号）
c.execute("INSERT INTO 表名(字段1, 字段2) VALUES(?, ?)", ("值1", "值2"))
conn.commit()          # ← 增删改完必须 commit，否则没真正写进去

# 3) 更新
c.execute("UPDATE 表名 SET 字段2 = ? WHERE 字段1 = ?", ("新值", "旧值"))
conn.commit()

# 4) 删除
c.execute("DELETE FROM 表名 WHERE 字段1 = ?", ("值",))
conn.commit()

# 5) 查询全部
c.execute("SELECT * FROM 表名")
rows = c.fetchall()          # fetchall = 全部抓出来（注意括号 + 拼写）
for row in rows:
    print(row)

conn.close()


# ══════════════════════════════════════════════════════════
# 模板 2 ｜ requests GET + JSON 解析 + 遍历统计
# 场景：从接口拉一批数据，逐个检查、数数
# 记忆点：get → .json() → for 遍历 → if 条件筛选
# ══════════════════════════════════════════════════════════
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()          # 把返回内容转成 Python 能用的字典/列表

count = 0
for v in data:              # v 是一条数据（一个字典）
    if len(v["title"]) > 70:   # 按某个字段做条件
        count = count + 1
print("发现异常：", count, "篇")


# ══════════════════════════════════════════════════════════
# 模板 3 ｜ requests POST 推送 + 取回执
# 场景：把结果「推」到某个接口（比如告警通知）
# 记忆点：post 用 json= 传数据，回执看 .json() 和 .status_code
# ══════════════════════════════════════════════════════════
import requests

resp_out = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"title": "标题", "body": "正文内容", "userId": 7}
)
data_out = resp_out.json()            # 服务器给的回执
print("回执 ID：", data_out["id"])
print("状态码：", resp_out.status_code)


# ══════════════════════════════════════════════════════════
# 模板 4 ｜ argparse 四步骨架
# 场景：让脚本能接收命令行参数（python xx.py --关键词 值）
# 记忆点：建 parser → 加参数 → 解析 → 取 args.名（把 -- 去掉）
# ══════════════════════════════════════════════════════════
import argparse

parser = argparse.ArgumentParser()                       # A、P 大写
parser.add_argument("--name", type=str, default="泽华", help="姓名")
args = parser.parse_args()                               # parse_args 带 s

print(f"你好，{args.name}")     # 取值用 args.name（没有 --）


# ══════════════════════════════════════════════════════════
# 模板 5 ｜ argparse + requests 组合（含 if/else 告警）
# 场景：命令行传关键词 → 拉数据 → 命中/未命中走不同分支
# 记忆点：这是周五小考的完整套路，两个模块缝一起
# ══════════════════════════════════════════════════════════
import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--keyword", type=str, default="est", help="关键词")
args = parser.parse_args()

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

count = 0
for v in data:
    if args.keyword in v["title"]:   # in 判断：关键词在不在标题里
        count = count + 1

if count > 0:
    print("找到", count, "篇包含关键词的文章")
else:
    resp_out = requests.post("https://jsonplaceholder.typicode.com/posts",
                             json={"body": f"未找到包含{args.keyword}的文章"})
    print("回执 ID：", resp_out.json()["id"])


# ══════════════════════════════════════════════════════════
# 模板 6 ｜ 字典计数器（数每个 key 出现几次）
# 场景：统计「每个作者发了多少篇」「每个词出现几次」
# 记忆点：在字典里 → 加 1；不在 → 设为 1（千万别写成 counts["uid"]）
# ══════════════════════════════════════════════════════════
counts = {}
for v in data:               # data 是你上面拉到的列表
    uid = v["userId"]
    if uid in counts:
        counts[uid] = counts[uid] + 1   # 变量 uid，不加引号
    else:
        counts[uid] = 1

for k, val in counts.items():          # .items() 拆出 键 和 值
    print("作者：", k, "，篇数：", val)


# ══════════════════════════════════════════════════════════
# 模板 7 ｜ 字典累加 + 擂台法找最大
# 场景：统计「每个作者总字数」，再找出第一名
# 记忆点：累加用 total[uid] = total[uid] + 值；找最大用擂台法
# ══════════════════════════════════════════════════════════
total = {}
for v in data:
    uid = v["userId"]
    if uid in total:
        total[uid] = total[uid] + len(v["body"])   # 累加
    else:
        total[uid] = len(v["body"])

max_long = 0        # 擂台：先立一个 0 分的人
max_name = ""
for a, b in total.items():
    if b > max_long:        # 谁更大，谁上台
        max_long = b
        max_name = a
print("作者", max_name, "写了", max_long, "字，最多")


# ══════════════════════════════════════════════════════════
# 模板 8 ｜ 读文件 with open（逐行读）
# 场景：读一个本地文本文件，一行一行处理
# 记忆点：with open 会自动关文件；strip() 去掉每行末尾换行
# ══════════════════════════════════════════════════════════
with open("文件名.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())   # strip 去掉换行符


# ══════════════════════════════════════════════════════════
# 模板 9 ｜ JSON 写入 + 读取
# 场景：把 Python 数据存成文件，下次再读回来
# 记忆点：写用 dump，读用 load；"w" 写、"r" 读
# ══════════════════════════════════════════════════════════
import json

# —— 写入 ——
data = {"name": "泽华", "score": 90}
with open("数据.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)  # 中文不乱码 + 缩进好看

# —— 读取 ——
with open("数据.json", "r", encoding="utf-8") as f:
    data = json.load(f)
print(data)


# ══════════════════════════════════════════════════════════
# 模板 10 ｜ 函数 def（把一段逻辑打包，重复调用）
# 场景：同一段逻辑要用很多次，写成函数，一次定义到处调用
# 记忆点：def 定义 → 参数收进来 → return 交出去
# ══════════════════════════════════════════════════════════
def 求和(a, b):
    """两个数相加，返回结果（这行是说明）"""
    结果 = a + b
    return 结果

答案 = 求和(3, 5)     # 调用，3 传给 a，5 传给 b
print(答案)           # 8
