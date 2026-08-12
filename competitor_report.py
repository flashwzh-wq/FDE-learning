# Input:  competitors.txt（每行：公司|分数）
# Process: 读文件 → 解析每行 → 按分数评级 → 写两个报告
# Output: alert_report.txt（高优）+ full_report.txt（全量+汇总）
def get_rating(score):
    if score >= 85:
        return ("🔴高优先", "3")
    elif score >=60:
        return ("🟡跟进", "2")
    else:
        return ("🟢低关注", "1")
def parse_record(record):
    parts = record.split("|")
    score1 = parts[1]
    score = int(score1)
    pingjia, defen = get_rating(score)
    return (parts[0], str(score), pingjia, defen)
with open("competitors.txt","r") as f_in:
    with open("alert_report.txt","w") as f_outhigh:
        with open("full_report.txt","w") as f_outfull:
            total = 0
            total_score = 0
            proint1 = 0
            proint2 = 0
            proint3 = 0
            for line in f_in:
                line = line.strip()
                a,b,c,d = parse_record(line)
                text =a + " " + b + "分 " + c
                if d == "3":
                    total = total + 1
                    total_score = total_score +int(b)
                    proint3 =  proint3 + 1
                    f_outhigh.write(text + "\n")
                    f_outfull.write(text + "\n")
                if d == "2":
                    total = total + 1
                    total_score = total_score +int(b)
                    proint2 =  proint2 + 1
                    f_outfull.write(text + "\n")
                if d == "1":
                    total = total + 1
                    total_score = total_score +int(b)
                    proint1 =  proint1 + 1
                    f_outfull.write(text+ "\n")
            average = int(total_score) / int(total)
            f_outfull.write("共" + str(total) + "条\n")
            f_outfull.write("平均分：" + str(average) + "分\n")
            f_outfull.write("3级共" + str(proint3) + "条\n")
            f_outfull.write("2级共" + str(proint2) + "条\n")
            f_outfull.write("1级共" + str(proint1) + "条\n")