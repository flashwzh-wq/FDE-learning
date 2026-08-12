def is_qualified(text):
    if text < 10:
        return "太短"
    else:
        return "合格"
for i in range(3):
    text1 = input("请输入第" + str(i+1) + "条反馈")
    text = len(text1)
    score = is_qualified(text)
    print("第" + str(i+1) + score)