import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--brand", help="请填品牌")
args = parser.parse_args()

with open ("stores.txt", "r") as f:
    score_group ={}
    for line in f:
        line = line.strip()
        parts = line.split(",")
        name = parts[0]
        shop = parts[1]
        score = float(parts[2])
        if name not in score_group:
            score_group[name] = []
        score_group[name].append(score)

name_final = args.brand
if name_final in score_group:
    text_final = score_group[name_final]
    count = len(text_final)
    average =round(sum(text_final)/count , 1)
    max_score = max(text_final)
    min_score = min(text_final)
    print("品牌名：", name_final)
    print("门店数：", count)
    print("平均分", average)
    print("最高分", max_score)   
    print("最低分", min_score) 
else:
    print("没有对应品牌数据")


