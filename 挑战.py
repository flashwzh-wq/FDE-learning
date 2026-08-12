word1 = input("今天收到几条动态？")
word2 = int(word1)
total = 0
max_score = 0
max_name = ""
min_score = 100
min_name = ""
for a in range(word2):
    ads1 = input("请输入第" + str(a+1) + "条反馈的产品名")
    ads2 = input("请输入第" + str(a+1) + "条反馈的热度分")
    ads3 = int(ads2)
    if ads3 < 30:
        print(ads1 + ads2 + "🟢 低关注")
    elif ads3 <= 70:
        print(ads1 + ads2 + "🟡 需跟进")
    else:
        print("ads1" + "ads2" + "🔴 高优先级")  
    score = ads3
    total = total + score
    if score > max_score:
        max_score = score
        max_name = ads1
    if score < min_score:
        min_score = score
        min_name = ads1
print("---")
print("共处理" + str(word2) + "条")
print("平均热度：" + str(total / word2) + "分")
print("🔥最热动态：" + max_name + "(" + str(max_score) + ")分")
print("🧊最冷动态：" + min_name + "(" + str(min_score) + ")分")



