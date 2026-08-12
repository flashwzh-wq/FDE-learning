word_count1 = input("请输入数字A:")
word_count1 = int(word_count1)
word_count2 = input("请输入数字B:")
word_count2 = int(word_count2)
word_count3 = input("请输入数字C:")
word_count3 = int(word_count3)
total = word_count1 + word_count2 + word_count3
avg = total / 3
if avg < 15:
    print("太短")
elif avg <= 30:
    print("合适")
else:
    print("太长")