import json
record = {"飞书":77, "钉钉":89, "企微":87}
for k, v in record.items():
    print(k + ": " + str(v) + "分")
if "飞书" in record:
    print("飞书在字典里")
else:
    print("飞书不在字典里")
text = json.dumps(record)
print(text)
with open("review.json", "w") as f:
    json.dump(record, f)