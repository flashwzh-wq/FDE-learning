total = 0
for i in range(3):
    word1 = input("请输入第：" + str(i+1) + "条用户反馈")
    word2 = len(word1)
    if word2 < 10:
        print("太短")
    else:
        print("合格")
        total = total+1

print("共" + str(total) + "条合格")
