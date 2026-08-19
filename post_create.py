import requests

resp = requests.post("https://jsonplaceholder.typicode.com/posts" , json = {"title": "测试标题" , "body":"测试正文" , "userId": 7})
data = resp.json()

print("回执 ID：" , data["id"] , "文章标题："  , data["title"])
print(resp.status_code)
