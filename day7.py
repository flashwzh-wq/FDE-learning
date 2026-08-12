# def rate_visit(company,score):
#     if score >=70:
#         return company + "🔴 需要跟进"
#     else:
#         return company + "✅ 正常"
# print(rate_visit("钉钉", 85))
# print(rate_visit("飞书", 45))

#搭积木
def is_high(score):
    return score >= 70
def summary(company,score):
    if is_high(score):
        return company + "🔴"
    else:
        return company + "✅"
print(summary("字节", 88))