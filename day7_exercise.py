def get_rating(score):
    if score < 60:
        return "(" + str(score) + "分 待跟进）"  
    elif score < 85:
        return "(" + str(score) + "分 合格）"  
    else:
        return "(" + str(score) + "分 优秀）"  
def parse_alert(record):
    parts = record.split("|")
    score = int(parts[1])
    return parts[0] + " " + get_rating(score) + " - " + "事由：" + parts[2]
for i in range(3):
    record = input("请按照“拜访公司|评分|事由“的格式填写反馈")
    print(parse_alert(record))
    