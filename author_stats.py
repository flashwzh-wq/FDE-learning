import requests
import sqlite3

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

counts={}
for v in data:
    uid = v["userId"]
    if uid not in counts:
        counts[uid] = 1
    else:
        counts[uid] = counts[uid] + 1

conn = sqlite3.connect("author_stats.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS author_stats(
            id INTEGER PRIMARY KEY ,
            user_id INTEGER, 
            count INTEGER
            )""")

for a, b in counts.items():
    c.execute("INSERT INTO author_stats(user_id , count) VALUES(?,?)", (a,b))
conn.commit()

c.execute("SELECT * FROM author_stats")
rows = c.fetchall()
for row in rows:
    print(row)
