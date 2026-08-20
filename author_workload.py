import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()
print("共拉取" , len(data) , "组数据")
print("数据格式为：" , data[0])

total = {}
for v in data:
    uid = v["userId"]
    if uid in total:
        total[uid] = total[uid] + len(v["body"])
    else:
        total[uid] =  len(v["body"])
print(total)

max_long = 0
max_name = ""
for a,b in total.items():
    if b > max_long:
        max_long = b
        max_name = a
print("作者", max_name , "写了" , max_long , "字，最多")

