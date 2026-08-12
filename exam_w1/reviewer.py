for i in range(5):
    word1 = input("请输入第" + str(i+1) + "条反馈")
    word2 =len(word1)
    if word2 < 5:
         print("字数" + str(word2) + "❌ 太短")
    elif word2 <= 15:
        print("字数" + str(word2) + "✅ 合格")
    else:
        print("字数" + str(word2) + "⚠️ 太长")
print("审查完成")