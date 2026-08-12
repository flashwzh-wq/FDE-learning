def select_record(line):
    parts = line.split("|")
    return parts
def bijiao(score):
    return score >= 70
with open("competitors.txt", "r")as f_in: 
    all_companies = []
    high_companies = []
    for line in f_in:
        line =line.strip()
        text = select_record(line)
        all_companies.append(text[0])
        score = int(text[1])
        if bijiao(score):
            high_companies.append(text[0])
    for all_company in all_companies:
        print("全部企业：" + all_company)
    print("全部企业共" + str(len(all_companies)) + "家")
    for high_company in high_companies:
        print("高分企业：" + high_company)
    print("高分企业共" + str(len(high_companies)) + "家")