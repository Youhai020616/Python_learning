"""
演示读取文件，以读取的模式打开
"""
from itertools import count

#打开文件
f = open("D:/word.txt", "r",encoding="utf-8")

# #方式1：读取全部内容、通过字符串count方法统计itheima的数量
# content = f.read()
# count = content.count("itheima")
# print(f"itheima的数量是：{count}")


#方式2 一行一行进行读取,统计itheima出现的次数
count = 0
for line in f :
    line = line.strip()
    words = line.split(" ")
    for word in words:
        if word == "itheima":
            count = count + 1
print(f"itheima的数量是：{count}")

