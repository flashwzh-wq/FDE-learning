import json
def rank(score):
    if score >= 80:
        return "优势"
    elif score >= 60:
        return "持平"
    else:
        return "劣势"
def analyze(record):
    point = len(record)
    highest_score = 0
    hightest_name = ""
    lowest_score = 1000
    lowest_name = ""
    total = 0
    for name,score in record.items():
        total = total + score
        if score > highest_score:
            highest_score = score
            hightest_name = name
        if score < lowest_score:
            lowest_score = score
            lowest_name = name
    avarage = total/point
    return (hightest_name,highest_score, lowest_name,lowest_score, avarage)
with open("competitors.txt", "r") as f_in:
    record = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[0]] =int(parts[1])
        print(parts[0] + " | " + parts[1] + " | " + rank(int(parts[1])))
    higtest_name,highest_score, lowest_name,lowest_score, avarage = analyze(record)
    print("最高分：" + higtest_name + "（" + str(highest_score) + "分） ｜ " + "最低分：" + lowest_name + "（" + str(lowest_score) + "分） ｜ " +  "均分：" + str(avarage))
record["汇总"] = {"最高": higtest_name,
                   "最高分": highest_score,
                   "最低": lowest_name,
                   "最低分": lowest_score,
                   "均分": avarage}
with open("analysis.json", "w") as f_out:
    json.dump(record, f_out)



