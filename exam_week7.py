import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--user",type = int,help="请填写作者编号", default=1)
args = parser.parse_args()

resp = requests.get(f"https://jsonplaceholder.typicode.com/posts?userId={args.user}")
data = resp.json()

count = len(data)
title_group = {}
for v in data:
    name = v["userId"]
    title = v["title"]
    title_line = len(title)
    if name not in title_group:
         title_group[name] = []
    title_group[name].append(title_line)

for a,b in title_group.items():
    total = sum(b)
    count_b = len(b)
    average = round(total / count_b , 1)

if count == 0:
    print("未查询到作者",args.user ,"发布的作品")
else:
    print("作者 ID：" , args.user)
    print("发帖数量：" , str(count) )
    print("平均标题长度："  , float(average))
