import json
with open("analysis.json", "r") as f:
    data = json.load(f)
    record = {}
    for k,v in data.items():
        if k != "汇总":
            print(k + "(" + str(v) + ")分")
            if v < 60:
                record[k]=v

with open("low_score.json", "w") as f_out:
    json.dump(record,f_out)