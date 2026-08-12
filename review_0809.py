def get_company(line):
    parts = line.split("|")
    return parts[1]
with open("visits.txt","r") as f:
    for lines in f:
        line = lines.strip()
        print(get_company(line))
        