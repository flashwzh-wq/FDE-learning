import requests

def title_line(v):
    return len(v["title"])

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()
line_for3 = sorted(data,key=title_line, reverse = True)[:3]

for v in line_for3:
    title = v["title"]
    body = v["body"]
    print("正文长度" , len(body) , "标题" , title)

