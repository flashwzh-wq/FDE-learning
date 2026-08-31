from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import sqlite3

class TemplateIn(BaseModel):
    title: str
    keywords: str
    code: str
    
app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(
        {"message": "你好，这是我的第一个网页程序"},
        media_type="application/json; charset=utf-8",
    )

@app.get("/about")
def zehua():
    return JSONResponse(
        {"message": "我是泽华，正在学习python"},
        media_type="application/json; charset=utf-8",
    )

@app.get("/hello/{name}")
def greet (name: str):
    return JSONResponse(
        {"message":f"你好，{name}"},
        media_type="application/json; charset=utf-8",
    )

@app.get("/search/{keyword}")
def search(keyword:str):
    conn = sqlite3.connect("code_dict.db")
    c = conn.cursor()
    
    c.execute("SELECT id, title, keywords FROM templates WHERE keywords LIKE ? OR title LIKE ?", (f"%{keyword}%", f"%{keyword}%"))
    rows = c.fetchall()
    conn.close()
    return JSONResponse(
        {"keyword": keyword, "results":rows},
         media_type="application/json; charset=utf-8",
    )

@app.post("/add")
def add_template(item:TemplateIn):
    title = item.title
    keywords = item.keywords
    code = item.code
    conn = sqlite3.connect("code_dict.db")
    c = conn.cursor()

    c.execute("SELECT * FROM templates WHERE title like ?",(title,))
    if c.fetchone() is None:
        c.execute("INSERT INTO templates (title, keywords, code) VALUES(?, ?, ?)",
                  (title, keywords, code))
        conn.commit()
        conn.close()
        return JSONResponse(
                {"OK": True, "title":title},
                 media_type="application/json; charset=utf-8",
         )
    else:
        conn.close()
        return JSONResponse(
            {"OK": False, "message": "已存在相同 title"},
            media_type="application/json; charset=utf-8",
        )

@app.delete("/delete/{template_id}")
def delete_template(template_id:int):
    conn = sqlite3.connect("code_dict.db")
    c = conn.cursor()

    c.execute("SELECT id FROM templates WHERE id = ?",(template_id,))
    if c.fetchone():
        c.execute("DELETE FROM templates WHERE id = ?",(template_id,))
        conn.commit()
        conn.close()
        return JSONResponse(
            {"OK":True, "deleted_id":template_id},
            media_type="application/json; charset=utf-8",
         )
    else:
        conn.close()
        return JSONResponse(
            {"OK":False,"message":"没有找到需要删除的内容"},
            media_type="application/json; charset=utf-8",
        )

@app.put("/update/{template_id}")
def update_template(template_id: int, item:TemplateIn):
    conn = sqlite3.connect("code_dict.db")
    c = conn.cursor()

    c.execute("SELECT id FROM templates WHERE id = ?",(template_id,))
    if c.fetchone():
        c.execute("UPDATE templates SET title=?, keywords=?, code=? WHERE id = ?",
        (item.title, 
         item.keywords, 
         item.code, 
         template_id)
         )
        conn.commit()
        conn.close()

        return JSONResponse(
            {"OK":True, "message":f"已修改编号为{template_id}的记录"},
            media_type="application/json; charset=utf-8",
        )
    else:
         conn.close()
         return JSONResponse(
            {"OK":False, "message":f"未找到编号为{template_id}的记录"},
            media_type="application/json; charset=utf-8",
        )