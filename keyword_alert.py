import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--keyword", type=str , default="est", help="输入想要查询的关键词")
args = parser.parse_args()

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

count = 0
for v in data:
    if args.keyword in v["title"]:
        count = count + 1
if count > 0:
    print("找到" , count , "篇包含关键词“", args.keyword , "“的文章")
else:
    resp_out = requests.post("https://jsonplaceholder.typicode.com/posts" , json={"body":f"未找到包含{args.keyword}的文章"})
    data_out = resp_out.json()
    print("回执 ID 为：" , data_out["id"])
    print(resp_out.status_code)

