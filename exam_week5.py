import json
shop = [
    {"店名": "万象城", "季度销售": [120, 135, 110, 150]},
    {"店名": "海岸城", "季度销售": [95, 88, 102, 90]},
    {"店名": "壹方城", "季度销售": [130, 128, 140, 136]},
]
def calc (text):
    total_score = 0
    count = len(text)
    for score in text:
        total_score = total_score + int(score)
    average = round(total_score / count ,1)
    return average , total_score

def level(score):
    if score >= 125:
        return "A 级"
    elif score >= 100:
        return "B 级"
    else:
        return "C 级"

aver = {}
total_sale ={}
pj = {}
max_sale = 0
max_name =""
for v in shop:
    name = v["店名"]
    score_group = v["季度销售"]
    average , total_score = calc(score_group)
    aver[name] = average
    total_sale[name] = total_score
    if average > max_sale:
        max_sale = average
        max_name = name
    pingji = level(average)
    pj[name] = pingji
print("平均分高的店：" + max_name + "(" + str(max_sale) + "分）")

huizong = {}
huizong["平均"] = aver
huizong["总销售"] = total_sale
huizong["评级"] = pj

with open ("exam_report.json", "w") as f:
    json.dump(huizong, f)







    
