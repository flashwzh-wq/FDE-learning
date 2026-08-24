import argparse
import requests
import sqlite3

parser = argparse.ArgumentParser()
parser.add_argument("--keyword", default="est", help="请输入关键词")
args = parser.parse_args()
keyword = args.keyword

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

goodword = {}
for v in data:
    uid = v["id"]
    title = v["title"]
    if keyword in title:
        goodword[uid] = title
count = len(goodword)
print ("共找到" , count , f"篇包含关键词{keyword}的文章")

conn = sqlite3.connect("post_search.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS results(
        id INTEGER,
        title TEXT
)""")

c.execute("DELETE FROM results")
for a,b in goodword.items():
    c.execute("INSERT INTO results(id,title) VALUES(?,?)",(a,b))
conn.commit()
conn.close()