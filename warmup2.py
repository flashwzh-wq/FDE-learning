import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

count = 0
for v in data:
    title = v["title"]
    if len(title) > 70:
        count =count + 1

print("共返回" , len(data) , "条数据")
print("标题超过 70 字的共有" , str(count) , "篇")

