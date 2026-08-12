def check_alert(score):
    return score >= 70
count = input("今天要提供几条动态？")
n = int(count)
alert_count = 0
for in range(n):
    name = input("请输入第" + str(n+1) + "条动态的产品名")
    score_str = input("请输入第" + str(n+1) + "条动态的评分")
    score = int(score_str)
    if check_alert:
        print(name + " " + score_str + "分 🔴警惕")
        alert_count = alert_count + 1
    else:
        print(name + " " + score_str + "分 ✅安全"))
print("共" + count + "条，其中" + str(alert_count) + "条需要警惕")