import json
with open ("visits.txt", "r") as f_in:
    record = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[1]] = {"分数":parts[2], "备注":parts[3]}
with open("practice.json", "w") as f_out:
    json.dump(record, f_out)
with open("practice.json", "r") as f_in2:
    text = json.load(f_in2)
    highest_name = ""
    highest_score = 0
    for k,v in text.items():
        score = int(v["分数"])
        if score > highest_score:
            highest_name = k
            highest_score = score
print("最高分客户：" + highest_name + "(" + str(highest_score) + "分）")


