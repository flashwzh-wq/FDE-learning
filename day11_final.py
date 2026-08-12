import json
def level(score):
    if score >= 85:
        return "满意"
    elif score  >= 60:
        return "一般"
    else:
        return "不满"
with open("visits.txt", "r") as f_in:
    record = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[1]] = {"分数":parts[2], 
                             "备注":parts[3]}
        print(parts[1] + "(" + parts[2] + "分，" + level(int(parts[2])) + ") —— 备注：" + parts[3])
with open("visit_data.json","w") as f_out:
    json.dump(record, f_out)
with open("visit_data.json","r") as f_in2:
    text = json.load(f_in2)
    highest_score = 0
    highest_name = ""
    lowest_score = 100
    lowest_name = ""
    for k,v in text.items():
        score = int(v["分数"])
        if score > highest_score:
            highest_score = score
            highest_name = k
        if score < lowest_score:
            lowest_score = score
            lowest_name = k
    print("汇总：最高分" + highest_name + "(" + str(highest_score) + ") " + lowest_name + "(" + str(lowest_score) + ")")


