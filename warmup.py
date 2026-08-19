import requests

resp = requests.get("https://jsonplaceholder.typicode.com/posts/3")
data = resp.json()

print("标题为：" , data["title"])
print("userID为：" , data["userId"])