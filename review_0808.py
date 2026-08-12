def is_vip(score):
   return score >= 80 
count_vip = 0
while True:
    word = input("请输入分数(输入“q“退出)：")
    if word == "q":
        print ("已退出")
        break
    else:
        score = int(word)
        result = is_vip(score)
        if result:
            count_vip = count_vip + 1
            print("vip")
        else:
            print("普通")
print("共" + str(count_vip) + "位VIP")

