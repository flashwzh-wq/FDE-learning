record = [12, 8, 15, 6, 9, 11]
count = len(record)
total = 0
max_score = 0
for r in record:
    score = int(r)
    total = total +score
    if score > max_score:
        max_score = score
average = total / count
print("总和：" + str(total))
print("平均数：" + str(average))
print("最大值：" + str(max_score))

