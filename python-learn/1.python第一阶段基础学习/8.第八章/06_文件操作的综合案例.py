"""
文件操作综合案例：文件备份
"""

#打开文件得到文件对象
fr= open("D:/bill.txt","r",encoding="utf-8")
#准备写入
fw = open("D:/bill_copy.txt","w",encoding="utf-8")



#for 循环读取文件
for line in fr:
    line = line.strip()
    if line.strip(",")[4] == "测试":
        continue

    fw.write(line)
    fw.write("\n")
