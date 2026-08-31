import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--keyword", type=str, default=None, help="要查关键词")
parser.add_argument("--delete", type=str, help="要删除的模板标题")
parser.add_argument("--update", type=str, help="要修改的模板标题")
parser.add_argument("--newcode", type=str, help="要更新的代码")
parser.add_argument("--add", type=str, help="要新增的模板标题")
parser.add_argument("--addcode", type=str, help="要新增的模板代码")
parser.add_argument("--addkeywords", type=str, help="要新增的模板关键词")
args = parser.parse_args()

# with 打开数据库，缩进结束自动 conn.close()，不用再手动关
with sqlite3.connect("code_dict.db") as conn:
    c = conn.cursor()

    # 建表
    c.execute("""CREATE TABLE IF NOT EXISTS templates(
         id INTEGER PRIMARY KEY,
         title TEXT,
         keywords TEXT,
         code TEXT
         )""")
    conn.commit()

    # 预置 3 条模板（带查重）
    code1 = """import requests
resp = requests.get("网址")
data = resp.json()"""

    c.execute("SELECT id FROM templates WHERE title = ?", ("requests请求",))
    if c.fetchone() is None:
        c.execute("INSERT INTO templates(title, keywords, code) VALUES(?,?,?)",
                  ("requests请求", "下载网络内容", code1))
        conn.commit()

    code2 = """items = ["a", "b", "a", "c", "b", "a"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print(counts)"""

    c.execute("SELECT id FROM templates WHERE title = ?", ("字典计数器",))
    if c.fetchone() is None:
        c.execute("INSERT INTO templates(title, keywords, code) VALUES(?,?,?)",
                  ("字典计数器", "统计 计数 出现次数", code2))
        conn.commit()

    code3 = """import sqlite3
conn = sqlite3.connect("test.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS t(id INTEGER PRIMARY KEY, name TEXT)")
c.execute("INSERT INTO t(name) VALUES(?)", ("小明",))
conn.commit()
print(c.execute("SELECT * FROM t").fetchall())
conn.close()"""

    c.execute("SELECT id FROM templates WHERE title = ?", ("SQLite标准流程",))
    if c.fetchone() is None:
        c.execute("INSERT INTO templates(title, keywords, code) VALUES(?,?,?)",
                  ("SQLite标准流程", "数据库 建表 插入 查询", code3))
        conn.commit()

    # 增（先查重 + 如实汇报）
    if args.add and args.addcode:
        c.execute("SELECT id FROM templates WHERE title = ?", (args.add,))
        if c.fetchone() is None:
            c.execute("INSERT INTO templates(title, keywords, code) VALUES(?,?,?)",
                      (args.add, args.addkeywords, args.addcode))
            conn.commit()
            print(f"已新增：{args.add}")
        else:
            print(f"已存在，跳过：{args.add}")

    # 查
    if args.keyword:
        c.execute("SELECT id, title, keywords FROM templates WHERE keywords LIKE ? OR title LIKE ?",
                  (f"%{args.keyword}%", f"%{args.keyword}%"))
        for row in c.fetchall():
            print(row[0], row[1], row[2])

    # 删（先查再删 + 如实汇报）
    if args.delete:
        c.execute("SELECT id FROM templates WHERE title = ?", (args.delete,))
        if c.fetchone() is None:
            print(f"没找到，无需删除：{args.delete}")
        else:
            c.execute("DELETE FROM templates WHERE title = ?", (args.delete,))
            conn.commit()
            print(f"已删除：{args.delete}")

    # 改（先查再改 + 如实汇报）
    if args.update and args.newcode:
        c.execute("SELECT id FROM templates WHERE title = ?", (args.update,))
        if c.fetchone() is None:
            print(f"没找到，无法修改：{args.update}")
        else:
            c.execute("UPDATE templates SET code = ? WHERE title = ?", (args.newcode, args.update))
            conn.commit()
            print(f"已更新：{args.update}")
