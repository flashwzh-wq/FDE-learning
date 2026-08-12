import json
with open("visits.txt", "r") as f_in:
    record = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[1]] = {"分数":parts[2],"备注":parts[3]}
        print(parts[1] + " -- " + parts[2] + "分（备注：" + parts[3] + ")")
with open("review_out.json", "w") as f_out:
    json.dump(record,f_out)
with open("review_out.json", "r") as f_in2:
    text = json.load(f_in2)
    lowest_name = ""
    lowest_score = 100
    for k,v in text.items():
        score = int(v["分数"])
        if score <lowest_score:
            lowest_score = score
            lowest_name = k
print("汇总：最低分客户名：" + lowest_name + "(得分：" + str(lowest_score) + ")")