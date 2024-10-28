# """
# 演示文件的追加 a模式，原有内容不变，写入新的内容
#
# """
#
# #打开文件
# f = open("D:/test.txt","a")
# #写入内容
# f.write("hello world")
# #关闭文件
# f.close()

#打开一个存在的文件
f = open("D:/test.txt","a",encoding="utf-8")
#写入内容
f.write("\n月薪过万")
#关闭文件
f.close()