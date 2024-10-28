# """
# 演示文件的写入操作
# """
#
# # 1. 打开文件
# import  time
# f = open("D:/text.txt", "w",encoding="utf-8")
#
# # 2. 写入数据
# f.write ("hello word")
#
# # #flush 刷新
# # f.flush()
# time.sleep(6000)
#
# # 3. 关闭文件 close文件内置flush功能
# f.close()
#
# # 3. 关闭文件

#文件存在的时候，会把文件的内容进行清空原有内容，再重新写入新内容
import  time
f = open ("D:/text.txt", "w",encoding="utf-8")
f.write("黑马程序员")
f.close()
