import json
def judge(score):
    if score >= 85:
        return "优秀"
    elif score >= 70:
        return "良好"
    else:
        return "需跟进"
with open("visits.txt", "r") as f_in:
    record ={}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[0]] = {"次数":parts[1], "分数":parts[2]}
        text = parts[0] + " | 拜访" + parts[1] + "次 ｜ " + parts[2] + " | " + judge(int(parts[2]))
        print(text)
with open("visit_report.json", "w") as f_out:
    json.dump(record,f_out)
