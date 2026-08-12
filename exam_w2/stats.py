#IPO拆解
#输入这里先用 input 确定数值N，然后用 lnt 数字化，变为 range的值
#然后需要两个函数：1、评分函数 2、切分+输出函数
#循环里需要记录总分和优秀、合格、待跟进数
#评分函数
good = 0
fine = 0
under = 0
total = 0
def get_rating(score):
    if score < 60:
        return (str(score) + "分（待跟进)", "under")
    elif score < 85:
        return (str(score) + "分（合格)", "fine")
    else:
        return (str(score) + "分（优秀)", "good")
def parse_record(record):
    parts = record.split("|")
    score = int(parts[1])
    result, level = get_rating(score)
    return parts[0] + " - " + result + " | " + "备注：" + parts[2]
time = input("请输入今天要填写的拜访记录数量：")
time1 = int(time)
for i in range(time1):
    record = input("请按照“公司名|分数|备注“的格式输入第" +  str(i+1) + "条拜访记录：")
    parts = record.split("|")
    score = int(parts[1])
    line = parse_record(record)
    _,level =get_rating(score)
    print(line)
    if level == "good":
        good = good + 1
    elif level == "fine":
        fine = fine + 1
    else:
        under = under + 1
    total = total +score
average = total / time1
print("汇总如下：")
print("平均分：" + str(average) + "分")
print("共" + time + "条记录")
print("优秀：" + str(good) +"条（≥85）")
print("合格：" + str(fine) +"条（60～84）")
print("待跟进：" + str(under) +"条（<60）")
