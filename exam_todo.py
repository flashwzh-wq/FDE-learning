import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--user",type = int,help="请填写作者编号", default=1)
args = parser.parse_args()

resp = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={args.user}")
data = resp.json()
count = len(data)

total = 0
done = 0
for v in data:
    todo = v["completed"]
    total = total + 1
    if todo:
        done = done + 1
rate = round(done /total*100,1) 

if count == 0:
    print("未检索到作者" , args.user , "的作品")
else:
    print("作者 ID：",args.user )
    print("总待办数量：", str(count))
    print("已完成待办数量：", str(done))
    print("完成率：",float(rate),"%")