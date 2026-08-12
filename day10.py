score = {"飞书": 85,"钉钉": 72, "字节": 92}
print(score["飞书"])
score["阿里"] = 78
print(score["阿里"])
for name in score:
    print(name,":",score[name])
print(score.keys())
print(score.values())
if "飞书" in score:
    print("有飞书的数据")
else:
    print("没有找到飞书")
