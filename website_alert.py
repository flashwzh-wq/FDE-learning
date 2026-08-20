import requests

resp = requests.get("https://jsonplaceholder.typicode.com/users")
data = resp.json()

count = 0
for v in data:
    web = v["website"]
    if ".com" not in web:
        count = count + 1
print("异常用户数：", count)

resp_out = requests.post("https://jsonplaceholder.typicode.com/users", json={"body":f"发现{count}个官网异常用户"})
data_out =resp_out.json()

print("回执 ID 为" , data_out["id"])
print("状态码：" , resp_out.status_code)

