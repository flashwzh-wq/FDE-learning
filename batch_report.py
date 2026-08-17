import glob

files = glob.glob("data/*.txt")
score_group = {}
for file in files:
    with open(file , "r") as f_in:
        for line in f_in:
            line = line.strip()
            parts = line.split(",")
            name = parts[0]
            score = float(parts[2])
            if name not in score_group:
                score_group[name] = []
            score_group[name].append(score)

for k,v in score_group.items():
    name_final = k
    score_group_final = v
    count = len(v)
    average = round(sum(v) / count , 1)
    print("品牌：" + k + ", 门店数：" + str(count) + ", 平均分：" + str(average))

