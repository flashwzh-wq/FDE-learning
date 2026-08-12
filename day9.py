companies = ["钉钉", "飞书", "字节", "阿里"]
score = [85, 45, 92, 67]
print(companies[0])
print(companies[2])
print(len(companies))
for company in companies:
    print("竞品：" + company)
# 读取 visits.txt，把所有公司名收集到一个列表里
companise_list = [] #这是个空列表
with open("visits.txt","r") as f:
    for line in f:
        line =line.strip()
        parts = line.split("|")
        companise_list.append(parts[1])
print("所有公司：")
print(companise_list)
print("共" + str(len(companise_list)) + "家公司")
