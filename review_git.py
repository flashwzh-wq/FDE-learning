import json
record = {
    "万达店": {"拜访次数": 4, "满意度分": [88, 92, 85, 90]},
    "天虹店": {"拜访次数": 3, "满意度分": [76, 81, 79]},
    "永旺店": {"拜访次数": 5, "满意度分": [91, 95, 89, 93, 90]},
}
result = {}
for k,v in record.items():
    text = v["满意度分"]
    total_score = 0
    total = len(text) 
    for score in text:
        total_score= total_score + score
    average = total_score / total
    final_average = round(average,1)
    result[k] = final_average
with open ("review_output.json" , "w") as f_in:
    json.dump(result, f_in)
