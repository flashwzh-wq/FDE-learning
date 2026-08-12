with open("competitors.txt" , "r") as f:
    score = {}
    for line in f:
        parts = line.split("|")
        score[parts[0]] = int(parts[1])
        score_a = int(parts[1])
        if score_a >= 80:
            print(parts[0], parts[1], "分")
    if "阿里" in score:
            print("有阿里的数据")
    else:
            print("“阿里“不在字典里")
    print(score.values()) 
import json
text = json.dumps({"飞书": 85, "钉钉": 72})
print(text)
print(type(text))
