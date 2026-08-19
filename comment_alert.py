import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--limit", type=int , default=180, help="正文超过多少字算异常")
args = parser.parse_args()

resp = requests.get("https://jsonplaceholder.typicode.com/comments")
data = resp.json()

count_long = 0
for v in data:
    body = v["body"]
    if len(body) > args.limit:
        count_long = count_long + 1

resp_out = requests.post("https://jsonplaceholder.typicode.com/comments" , json={"title":"异常警告：评论过长可能是刷屏垃圾、也可能是情绪激烈的长文" , "body": f"共发现{count_long}条评论字数大于{args.limit}字", "userId":7 })
data_out = resp_out.json()

print("告警回执：" , data_out["id"])
print("发现异常：", count_long, "条")  
print(resp_out.status_code)

