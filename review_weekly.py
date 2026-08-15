import json
record =[
    {"店名": "万达", "拜访": [88, 92, 85]},
    {"店名": "天虹", "拜访": [76, 81, 79]},
    {"店名": "永旺", "拜访": [91, 95, 89]},
]

def word(scores_group):
    count = len(scores_group)
    total = 0
    for score in scores_group:
        scores_r = int(score)
        total = total + scores_r
    average =round(total / count, 1)
    return average

average_group = {}
for v in record:
    name = v["店名"]
    scores_group = v["拜访"]
    average = word(scores_group)
    average_group[name] = average

classic = {}
max_average = 0
max_average_name = ""
for k,v in average_group.items():
    average_score = v
    if average_score > max_average:
        max_average = average_score
        max_average_name = k
    if average_score > 85:
        word = "优秀"
    else:
        word = "待提升"
    classic[k] = word
print("平均分最高的门店：" + max_average_name + "(" + str(max_average) + "分)")

report = {"平均分":average_group,"分类":classic}
with open("report.json", "w") as f:
    json.dump(report,f)