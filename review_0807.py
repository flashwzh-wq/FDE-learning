def get_level(score):
    if score < 60:
        return "不及格"
    elif score < 85:
        return "合格"
    else:
        return "优秀"
for i in range(3):
    score1 = input("请输入第" + str(i+1) + "条分数")
    score = int(score1)
    print(get_level(score))
