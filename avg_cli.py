import sys

s1 = int(sys.argv[1])
s2 = int(sys.argv[2])
s3 = int(sys.argv[3])

average = round(((s1 + s2 + s3  ) / 3) , 1)

print("平均分：" + str(average))
