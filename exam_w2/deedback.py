def rate(text):
    if text >= 30:
        return "详细" 
    elif text >= 10:
        return "合格"
    else:
        return "敷衍"
total = 0
good = 0
fine = 0
under = 0
while True:
    word = input("请输入用户反馈(退出请输入exit):")
    text = len(word)
    if word == "exit":
        print("记录结束")
        break
    else:
        result =rate(text)
        print(result)
        total = total + 1
        if result == "详细":
            good = good + 1
        elif result == "合格":
            fine = fine + 1
        else:
            under = under + 1
print("汇总：")
print("共" + str(total) + "条记录")
print("详细" + str(good) + "条")
print("合格" + str(fine) + "条")
print("敷衍" + str(under) + "条")
