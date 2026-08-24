import sqlite3

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



c.execute("INSERT INTO templates(title , keywords , code) VALUES(? , ? , ?)" , 
("requests请求 " , "下载网络内容" , code1))
conn.commit()

c.execute("SELECT id ,title , keywords FROM templates")
rows = c.fetchall()
for row in rows:
    print(row[0] , row[1] , row[2])