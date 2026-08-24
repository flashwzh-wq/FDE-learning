import sqlite3
from datetime import date

conn = sqlite3.connect("books.db")
c = conn.cursor()

#1.建表
c.execute("""CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY , title TEXT, borrower TEXT , date TEXT)""")

#2.算日子是今天
today = str(date.today())

#3.塞一条数据
c.execute("INSERT INTO books(title , borrower , date) VALUES(? , ? , ?)",("《三体》" , "张三" , today))
conn.commit()

#4.查阅这条记录，打印
c.execute("SELECT*FROM books")
rows = c.fetchall()
print(rows)

#5.改变借阅人
c.execute("UPDATE books SET borrower = ? WHERE borrower = ?" ,("李四" , "张三") )
conn.commit()
c.execute("SELECT*FROM books")
rows1 = c.fetchall()
print(rows1)

#删除这条记录
c.execute("DELETE FROM books WHERE borrower = ?",("李四"))
conn.commit()

#确认表为空
c.execute("SELECT*FROM books")
rows2 = c.fetchall()
print(rows2)