import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--keyword",type= str , default= "est" , help="要查关键词")
parser.add_argument("--delete", type= str ,help="要删除的模板标题")
parser.add_argument("--update", type= str ,help="要修改的模板标题")
parser.add_argument("--newcode", type= str , help="要更新的代码")
parser.add_argument("--add", type= str , help="要新增的模板标题")
parser.add_argument("--addcode", type= str , help="要新增的模板代码")
args = parser.parse_args()

conn = sqlite3.connect("code_dict.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS templates(
     id INTEGER PRIMARY KEY , 
     title TEXT , 
     keywords TEXT , 
     code TEXT
     )""")

code1 = """import requests
resp = requests.get("网址")
data = resp.json()"""

c.execute("SELECT id FROM templates WHERE title = ?", ("requests请求",))
if c.fetchone() is None:
     c.execute("INSERT INTO templates(title , keywords , code) VALUES(? , ? , ?)" , 
          ("requests请求" , "下载网络内容" , code1))
     conn.commit()

code2 = """items = ["a", "b", "a", "c", "b", "a"]
counts = {}
for item in items:
    counts[item] = counts.get(item, 0) + 1
print(counts)"""

c.execute("SELECT id FROM templates WHERE title = ?", ("字典计数器",))
if c.fetchone() is None:
    c.execute("INSERT INTO templates(title , keywords , code) VALUES(? , ? , ?)" ,
         ("字典计数器" , "统计 计数 出现次数" , code2))
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
    c.execute("INSERT INTO templates(title , keywords , code) VALUES(? , ? , ?)" ,
         ("SQLite标准流程" , "数据库 建表 插入 查询" , code3))
    conn.commit()

if args.add and args.addcode:
     c.execute("SELECT id FROM templates WHERE title = ?",(args.add,))
     if c.fetchone() is None:
          c.execute("INSERT INTO templates(title, keywords,code) VALUES(?,?,?)",
                    (args.add , "手动添加" , args.addcode))
          conn.commit()

c.execute("SELECT id ,title , keywords FROM templates WHERE keywords LIKE ? OR title LIKE ?",(f"%{args.keyword}%",f"%{args.keyword}%"))
rows = c.fetchall()
for row in rows:
    print(row[0] , row[1] , row[2])

if args.delete:          
     c.execute("DELETE FROM templates WHERE title = ?", (args.delete,))
     conn.commit()

if args.update:
     if args.newcode:
          c.execute("UPDATE templates SET code = ? WHERE title = ?",(args.newcode,args.update))
conn.commit()
conn.close()

