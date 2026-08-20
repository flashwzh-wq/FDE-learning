import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts")
data = resp.json()

print(len(data))
print(data[0])

counts ={}
for v in data:
    uid = v["userId"]
    if uid in counts:
        counts[uid] = counts[uid] + 1
    else:
        counts[uid] = 1
print(counts)

for k,v in counts.items():
    print("作者名：" , k , "，发布篇数："  , v)
    


