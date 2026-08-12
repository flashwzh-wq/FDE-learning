def get_rating(score):
    if score < 60:
        return "待跟进" + "(" + str(score) + ")分" 
    elif score < 85:
        return "合格" + "(" + str(score) + ")分"
    else:
        return "优秀" + "(" + str(score) + ")分"

for i in range(3):
    record = input("请按照“拜访公司|目标企业|评分|产品需求“的格式填写反馈")
    parts = record.split("|")
    score =int(parts[2])
    print("拜访日期：" + parts[0] + "  公司：" + parts[1] + "  评级：" + get_rating(score) + "  备注：" + parts[3])
