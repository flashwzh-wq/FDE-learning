import json
orders = [
    {"客户": "万达", "金额": 3200},
    {"客户": "天虹", "金额": 1850},
    {"客户": "永旺", "金额": 4600},
    {"客户": "华润", "金额": 2100},
]
total = 0
count = len(orders)
max_score = 0
result = []
for v in orders:
    name = v["客户"]
    score = int(v["金额"])
    total = total +score
    if score > max_score:
        max_score = score
    if score >= 3000:
        result.append(v)
average =round (total / count ,1)
with open ("big_orders.json", "w") as f:
    json.dump(result,f)
print("总金额：" + str(total))
print("平均金额：" + str(average))
print("最大金额：" +str(max_score))
