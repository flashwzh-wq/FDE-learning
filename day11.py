import json
# #1. 把 JSON 文件读回来
# with open("review.json", "r") as f:
#     data = json.load(f)
#     print(data)
#     print(type(data))

# print(data["飞书"])
# print("钉钉" in data)
with open("analysis.json", "r") as f:
    data = json.load(f)
    print("最高分" + data["汇总"]["最高"] + "（" +  str(data["汇总"]["最高分"]) + "分）")
# 今日已学 Git 第一次存档