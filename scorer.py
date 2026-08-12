word1 = input("今天要评估几条反馈")
word2 = int(word1)
for a in range(word2):
    ADC1 = input("请填写第" + str(a+1) + "条反馈")
    ADC2 = len(ADC1)
    if ADC2 < 10:
        print("字数：" + str(ADC2) + "❌ 敷衍")
    elif ADC2 <= 30:
        print("字数：" + str(ADC2) + "✅ 合格")
    else:
        print("字数：" + str(ADC2) + "🌟 详细")
print("评估完成，共处理" + word1 + "条反馈")
