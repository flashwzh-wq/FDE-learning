import json
with open ("competitors.txt" , "r") as f_in:
    record = {}
    for line in f_in:
        line = line.strip()
        parts = line.split("|")
        record[parts[0]] = parts[1]
        score = int(parts[1])
        if score >70:
            print(parts[0])
with open ("exercise.json" , "w") as f_out:
    json.dump(record,f_out)



