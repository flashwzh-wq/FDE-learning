import streamlit as st
import requests

st.title("企业知识库问答")


def 真转向量(文字):
    resp_out = requests.post("http://127.0.0.1:11434/api/embed",json={"model": "bge-m3", "input": 文字})
    data_out = resp_out.json()
    向量= data_out["embeddings"][0]
    return 向量

def 建向量库(片段们):
    库 = {}
    for 片段 in 片段们:
        库[片段] = 真转向量(片段)
    return 库

with open("资料.txt",encoding="utf-8" ) as 文件:
    资料片段们 = 文件.readlines()
资料片段们 = [资料.strip() for 资料 in 资料片段们]


库 = 建向量库(资料片段们)
st.caption(f"当前知识库共收录 {len(资料片段们)} 条资料")


def 算距离(向量a, 向量b):
    距离 = 0
    for i in range(min(len(向量a), len(向量b))):
        差值 = 向量a[i] - 向量b[i]
        距离 = 距离 + abs(差值)
    return 距离

def 搜库(问题,库):
    问题向量 = 真转向量(问题)
    最小距离 = 99999
    最像片段 = ""
    for 片段 in 库:
        片段向量 = 库[片段]
        距离 = 算距离(问题向量, 片段向量)
        if 距离 < 最小距离:
            最小距离 = 距离
            最像片段 = 片段
    return 最像片段



def 生成回答(问题, 最像片段):
    提示词 = f"根据下面这份资料回答用户问题，如果资料里没有答案，就说不知道。 \n\n资料: {最像片段}\n\n问题:{问题}"
    resp = requests.post("http://127.0.0.1:11434/api/generate",
                         json={"model":"qwen2.5:3b", "prompt": 提示词, "stream" : False})
    return resp.json()["response"]

问题 = st.text_input("请输入你的问题")

if st.button("提问"):
    if not 问题.strip():
        st.warning("请输入问题后再提问")
    else:
        with st.spinner("正在检索资料并生成回答..."):
            最像片段 = 搜库(问题, 库)
            回答 = 生成回答(问题, 最像片段)

        st.write(回答)
        st.write("命中的资料：", 最像片段)
