import os

a = os.listdir("17_FILES\dir")
print(a)

print(os.getcwd())
print(os.path.exists("rayan"))
os.remove("sample1.txt")
os.rmdir("dir") 