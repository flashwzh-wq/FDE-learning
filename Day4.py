#让代码能和人对话
name = input("你叫什么名字？")
print("你好，",name)
# word_count = input("请输入日报字数：")
# word_count = int(word_count)
# if word_count >50:
#     print("✅合格，字数够了")
# else:
#     print("✖️太短，再补点内容")
#三选一
word_count = input("请输入日报字数：")
word_count = int(word_count)
if word_count <20:
    print("❌ 太短，凑不够一条微博")
elif word_count <=100:
    print("✅ 合格，长度适中")
else:
    print("⚠️ 太长，建议拆分段落")