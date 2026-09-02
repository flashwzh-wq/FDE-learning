def 转向量(文字):
    列表 = []
    for 字符 in 文字:
        编号 = ord(字符)
        列表.append(编号)
    return 列表

def 算距离(向量a, 向量b):
    距离 = 0
    for i in range(min(len(向量a), len(向量b))):
        差值 = 向量a[i] - 向量b[i]
        距离 = 距离 + abs(差值)
    return 距离

def 找最像(目标句 ,候选句们 ):
    最小距离 = 9999
    最像的句子 = ""
    for 候选句 in 候选句们:
        距离 = 算距离(转向量(目标句), 转向量(候选句))
        if 距离 < 最小距离:
            最小距离 = 距离
            最像的句子 = 候选句
    return 最像的句子