import sqlite3
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--add",type=str, help="请填写新增客户名称")
parser.add_argument("——industry",type=str, help="请填写新增客户行业")
parser.add_argument("——list", action="store_true", help="列出所有客户")
parser.add_argument("——delete",type=str, help="请填写需要删掉的客户名称")
parser.add_argument("——stats",action="store_true", help="统计每个行业的客户数量")
args = parser.parse_args()

conn = sqlite3.connect("customer.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS customers(
    id INTEGER PRIMARY KEY,
    name TEXT,
    industry TEXT
)""")

if args.add and args.industry:
    c.execute("SELECT id FROM customers WHERE name = ?",(args.add,))
    if c.fetchone() is None:
        c.execute("INSERT INTO customers(name , industry)VALUES(? , ?)",
        (args.add , args.industry))
        conn.commit()

if args.list:
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    for row in rows:
        print(row)

if args.delete:
    c.execute("DELETE FROM customers WHERE name = ?",(args.delete,))
    conn.commit()

if args.stats:
    c.execute("SELECT * FROM customers")
    rows = c.fetchall()
    counts = {}
    for row in rows:
        name_out = row[1]
        industry_out = row[2]
        if industry_out in counts:
            counts[industry_out] = counts[industry_out] + 1
        else:
            counts[industry_out] = 1
    print(counts)

conn.close