# word1 = input("请输入一个数字")
# word2 = int(word1)
# if word2 < 10:
#     print("小")
# else:
#     print("大")
# for i in range(5):
#     print("这是第",i,"次")
# #批量统计反馈数字
# for i in range(3):
#     feedback =input("请输入第" + str(i+1) + "条反馈：")
#     print("字数",len(feedback))
#while 循环：输入exit 停止
print("\n--- while 循环练习 ---")
text = ""
while text != "exit":
    text =input("输入反馈（输入 exit 退出）：")
    if text !="exit":
        print("字数", len(text))
print("循环结束")