import sqlite3
from datetime import date

conn = sqlite3.connect("stock.db")
c = conn.cursor()

#1.建表 
c.execute("""CREATE TABLE IF NOT EXISTS stock(id INTEGER PRIMARY KEY , name TEXT , qty INTEGER , date TEXT)""")

#2.算日子
today = str(date.today())

#3.塞数据
c.execute("INSERT INTO stock(name , qty , date) VALUES(? , ? , ?)" , ("手机" , 10 , today))
c.execute("INSERT INTO stock(name , qty , date) VALUES(? , ? , ?)" , ("耳机" , 20 , today))
conn.commit()

#4.查数据
c.execute("SELECT*FROM stock ")
rows = c.fetchall()
print(rows)

#5.改数据
c.execute("UPDATE stock SET qty = ? WHERE name = ?" ,(30 , "耳机"))
conn.commit()

#6.删数据
c.execute("DELETE FROM stock WHERE name = ?" ,("手机",))
conn.commit()

#在查数据
c.execute("SELECT*FROM stock ")
rows = c.fetchall()
print(rows)