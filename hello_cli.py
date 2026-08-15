import argparse

parser = argparse.ArgumentParser()
parser.add_argument("名字")
args = parser.parse_args()

print("你好，" , args.名字)

