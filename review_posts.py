import argparse
import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()


count = len(data)
max_titleline = 0
total_bodyline = 0
max_name = ""
name_group ={}
for v in data:
    name = v["userId"] 
    title_line = len(v["title"])
    body_line = len(v["body"]) 
    total_bodyline = total_bodyline + body_line
    if title_line >max_titleline:
        max_titleline = title_line
        max_name = v["title"]
    if name not in name_group:
         name_group[name] = []
    name_group[name].append(title_line)

for a,b in name_group.items():
    name_final = a
    count_final = len(b)
    print("作者：" , a , "共发布" , str(count_final) , "篇")

print("标题最长的文章是：" , max_name , "(" , str(max_titleline) , "字）")
average_line = round(total_bodyline / count , 1)
print("所有文章平均长度：" , float(average_line))



