#通过open()打开一个文件

# f = open('test.txt', mode,encoding)


"""
演示打开文件
"""
import time

#打开文件
f =open("D:/百度网盘/Baidu_Downloads/资料/可视化案例数据/折线图数据/美国.txt","r",encoding="utf-8")

print(type(f))

#读取文件-read()
# print( f"读取文件内容：{f.read(10)}" )
# print( f"读取文件全部内容：{f.read()}" )

#读取文件的全部内容-readlines()
# #读取文件的全部内容，封装到列表中
# lines = f.readlines()
# print(f"lines对象的类型是：{type(lines)}")
# print(f"读取文件的全部内容，封装到列表中：{lines}" )


# #读取文件-readline方法
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# print(f"读取的第一行数据是：{line1}")
# print(f"读取的第二行数据是：{line2}")
# print(f"读取的第三行数据是：{line3}")


#for循环读取文件行
#
# for line in f:
#     print(line)
#
#
# #文件的关闭
#
#
# f.close()

#with open()语法操作文件
with open ("D:/百度网盘/Baidu_Downloads/资料/可视化案例数据/折线图数据/美国.txt","r",encoding="utf-8") as f :
    for line in f :
        print(line)
time.sleep(6000)
