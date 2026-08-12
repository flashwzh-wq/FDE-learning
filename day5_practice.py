for i in range(4):
    word1 = input("请输入第" + str(i+1) + "条反馈")
    word2 = len(word1)
    if word2 < 5:
        print("太短")
    else:
        print("合格")
print("统计完成")