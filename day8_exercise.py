def get_rating(score):
    if score >= 85:
        return (str(score) + "分 （优秀）", "good")
    elif score >= 60:
        return (str(score) + "分 （合格）", "fine")
    else:
        return (str(score) + "分 （待改进）", "under")
def parse_record(record):
    parts =record.split("|")
    score = int(parts[2])
    result, level = get_rating(score)
    text = parts[1] + "-" + result + "| 备注：" + parts[3]
    return (score, text)
with open("visits.txt", "r") as f_in:
    with open("high_score.txt", "w") as f_out:
        f_out.write("客户拜访记录报告\n")
        f_out.write("=" * 20 +"\n")
        for line in f_in:
            line = line.strip()
            score, text = parse_record(line) 
            if score >= 80:
                f_out.write(text + "\n")
        f_out.write("=" * 20 + "\n")
        f_out.write("报告生成完毕\n")

