with open("competitors.txt" , "r") as f:
    score = {}
    for line in f:
        parts = line.split("|")
        score[parts[0]] = parts[1]
    import json
    text = json.dumps(score)
    print(text)
with open("scores.json","w") as f_out:
    json.dump(score,f_out)
