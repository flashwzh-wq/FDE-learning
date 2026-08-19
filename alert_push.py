import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int , default=70, help="标题超过多少字算异常")
args = parser.parse_args()

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

count = 0
for v in data:
    if len(v["title"]) > args.limit:
        count = count + 1
print("发现异常：", count, "篇")

resp_out = requests.post("https://jsonplaceholder.typicode.com/posts" , json={"title": "异常警告：标题超长" , "body": f"共发现{count}篇标题超过{args.limit}字的文章", "userId":7})
data_out = resp_out.json()

print("回执 ID：" , data_out["id"])
print("状态码：" , resp_out.status_code)