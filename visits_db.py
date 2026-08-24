import sqlite3
from datetime import date

conn =sqlite3.connect("visits.db")
c = conn.cursor()

#1.先建表，如果表有了就不管了
c.execute("""CREATE TABLE IF NOT EXISTS visits(id INTEGER PRIMARY KEY,customer TEXT, date TEXT , note text) """)

#2.算好日子
today = str(date.today())

#3.在清场：把旧数据删掉
c.execute("DELETE FROM visits WHERE date = ?",(today,))
conn.commit()

#4.第三步，塞一条数据，提示塞好了
c.execute("INSERT INTO visits(customer , date , note) VALUES(?, ?, ?)",("星巴克" , today, "聊了会员体系"))
conn.commit()
print("塞好了")

#5.更新：把今天的备注改一下
c.execute("UPDATE visits SET note = ? WHERE date = ?" ,( "聊了会员体系，约了下周复访" , today))
conn.commit()

#6.最后查
c.execute("SELECT*FROM visits")
rows = c.fetchall()
print(rows)


