import argparse
import requests

parser = argparse.ArgumentParser()
parser.add_argument("--id",type = int,help="请填写帖子编号")
args = parser.parse_args()

resp = requests.get(f"https://jsonplaceholder.typicode.com/posts/{args.id}")
data = resp.json()

print("文章标题：", data["title"])
print("作者 ID：", data["userId"])