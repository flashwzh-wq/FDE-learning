import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--brand", help="竞品品牌名，比如瑞幸")
parser.add_argument("--limit", type=int, default=10, help="最多显示几条，默认10条")
args = parser.parse_args()

print("查询品牌：", args.brand)
print("显示条数：", args.limit)