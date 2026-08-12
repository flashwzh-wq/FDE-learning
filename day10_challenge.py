import json
def classify(score):
    if score >= 80:
        return "高关注"
    elif score >= 60:
        return "中等"
    else:
        return "低关注"
with open("competitors.txt" , "r") as f_in:
    jilu = {}
    results = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        jilu[parts[0]] = int(parts[1])
        score = int(parts[1])
        level = classify(score)
        print(parts[0] + " | " + str(parts[1]) + " | " + level)
        results[parts[0]] = {"分数":score, "等级": level}
with open("report.json", "w") as f_out:
    json.dump(results,f_out)
    