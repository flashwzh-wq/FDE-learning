import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()
count = len(data)

name_list = list(data[0].keys())

max_title = 0
min_title = 100
total_body = 0
for v in data:
    title = v["title"]
    body = v["body"]
    total_body = total_body + len(body)
    if len(title) > max_title:
        max_title = len(title)
    if len(title) < min_title:
        min_title = len(title)
average = round(total_body / count , 1)

print("总量：" , str(count))
print("字段清单：" , name_list)
print("最短标题：" , str(min_title) , "字; 最长标题：" , str(max_title) , "字")
print("平均值：" , float(average))



