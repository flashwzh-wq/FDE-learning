import glob

files = glob.glob("data/*.txt")
count =len(files)
print("扫到了", count, "个文件")