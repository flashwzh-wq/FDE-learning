import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--city", default="深圳", help="请填写城市名,默认为深圳")
args = parser.parse_args()

print("城市" , args.city)