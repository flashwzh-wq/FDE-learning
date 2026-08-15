import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", help="请填写城市名")
parser.add_argument("--min_score", type=int, default=0, help="请填写最低分，默认为 0 分")
args = parser.parse_args()

print("城市：", args.city)
print("最低评分：", args.min_score)