from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import JSONResponse
import sqlite3

class TemplateIn(BaseModel):
    title: str
    keywords: str
    code: str

def 执行sql(sql, 参数=(), 要写=False):
    conn = sqlite3.connect("code_dict.db")
    c = conn.cursor()
    c.execute(sql, 参数)
    if 要写:
        conn.commit()
    结果 = c.fetchall()
    conn.close()
    return 结果

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
    rows = 执行sql(
        "SELECT id, title,keywords FROM templates WHERE keywords LIKE ? OR title LIKE ?",
        (f"%{keyword}%",f"%{keyword}%"),
    )
    results = []
    for row in rows:
        result = {}
        result["id"] = row[0]
        result["title"] = row[1]
        result["keywords"] = row[2]
        results.append(result)

  
    return JSONResponse(
        {"keyword": keyword, "results":results},
         media_type="application/json; charset=utf-8",
    )

@app.post("/add")
def add_template(item:TemplateIn):
    title = item.title
    keywords = item.keywords
    code = item.code

    if 执行sql("SELECT * FROM templates WHERE title like ?", (title,)):
        return JSONResponse(
                {"OK": False, "message": "已存在相同 title"},
                 media_type="application/json; charset=utf-8")
    else:
        执行sql("INSERT INTO templates(title, keywords, code)VALUES(? ,? ,? )",
              (title,keywords,code), 要写=True )
        return JSONResponse(
            {"OK": True, "title": title},
            media_type="application/json; charset=utf-8",
        )

@app.delete("/delete/{template_id}")
def delete_template(template_id:int):
    if 执行sql("SELECT id FROM templates WHERE id = ?",(template_id,)):
        执行sql("DELETE FROM templates WHERE id = ?", (template_id,), 要写=True)
        return JSONResponse(
            {"OK":True, "deleted_id": template_id },
            media_type="application/json; charset=utf-8",
        )
    else:
        return JSONResponse(
            {"OK": False, "message":"没有找到需要删除的内容"},
             media_type="application/json; charset=utf-8",
        )


@app.put("/update/{template_id}")
def update_template(template_id: int, item:TemplateIn):
    if 执行sql("SELECT id FROM templates WHERE id = ?",(template_id,)):
        执行sql("UPDATE templates SET title=?, keywords=?, code=? WHERE id = ?",
              (item.title, item.keywords, item.code, template_id), 要写=True)
        return JSONResponse(
            {"OK": True, "message": f"已修改编号为{template_id}的记录"},
             media_type="application/json; charset=utf-8",
        )  
    else:
        return JSONResponse(
            {"OK": False, "message":f"未找到编号为{template_id}的记录"},
             media_type="application/json; charset=utf-8",
        ) 

