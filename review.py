word1 = input("请输入日报标题：")
word2 = input("请输入日报正文：")
print(len(word1),len(word2))
len1 = len(word1)
len2 = len(word2)
chazhi = len2 - len1
print("字数差",chazhi)
if len2 < 30:
    print("❌ 不及格，内容太少")
elif len2 <= 80:
    print("✅ 合格")
else:
    print("⚠️ 超标，建议精简")