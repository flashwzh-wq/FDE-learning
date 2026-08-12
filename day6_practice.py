def rate_competitor(score):
    if score < 30:
        return "🟢 低关注"
    elif score <= 70:
        return "🟡 需跟进"
    else:
        return "🔴 高优先级"   
while True:
    user_input = input("请输入分数（输入 exit退出）：")
    if user_input == "exit":
        break
    score = int(user_input)
    result = rate_competitor(score)
    print(result)