import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--name", help="随便填",type = str ,default= "泽华" )
args = parser.parse_args()

print(f"你好，{args.name}")
