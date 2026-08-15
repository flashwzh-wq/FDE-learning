import argparse

parser = argparse.ArgumentParser()
parser.add_argument("a")
parser.add_argument("b")
parser.add_argument("c")
args = parser.parse_args()


a = int(args.a)
b = int(args.b)
c = int(args.c)

average = round((a + b + c)/3, 1)


print("平均数，" , str(average))