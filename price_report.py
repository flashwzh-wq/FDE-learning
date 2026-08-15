import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--product", help="请填产品名称")
args = parser.parse_args()

with open ("price.txt" ,"r") as f:
    price_group ={}
    for line in f:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        price = float(parts[2])
        if name not in price_group:
            price_group[name] = []
        price_group[name].append(price)

name_final = args.product
if name_final in price_group:
    text = price_group[name_final]
    count = len(text)
    average = round(sum(text) / count, 1)
    max_score = max(text)
    min_score = min(text)
    print("产品：", name_final)
    print("门店数：", count)
    print("平均价：", average)
    print("最高价：", max_score)
    print("最低价：", min_score)
else:
    print("暂未查询到该产品信息")

