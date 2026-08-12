def is_active(days):
    return days <= 7
count_str = input("请输入今天需要登记几条客户记录")
count = int(count_str)
chenmo = 0
for i in range(count):
    name = input("请输入第" + str(i+1) + "条记录的客户名称")
    days_str = input("请输入第" + str(i+1) + "条记录距上传互动天数")
    days = int(days_str)
    if is_active(days):
        print("已" + days_str + "天未联系 🔥 活跃")
        chenmo = chenmo + 1
    else:
        print("已" + days_str + "天未联系 💤 沉默")
print("共" + count_str + "位客户，" + str(chenmo) + "位活跃" )
