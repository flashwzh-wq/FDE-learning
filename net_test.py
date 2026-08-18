import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/2")
print(resp)
print(resp.status_code)

date = resp.json()
print(date)

print("标题是：", date["title"])
print("作者 ID 是", date["userId"])