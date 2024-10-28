#元组定义：使用小括号，逗号隔开
from operator import index

#定义元组
t1 = (1,"hello",True)

t2 = ()

t3 = tuple()
print(f"t1的类型是：{type(t1)}")
print(f"t2的类型是：{type(t2)}")
print(f"t3的类型是：{type(t3)}")

t4 =("Hello"),
print(type(t4))


t5 = ((1,2,3),(4,5,6))
print(type(t5))

num = t5[1][2]
print(f"从嵌套元组中取出的元素是：{num}")

#index 查找方法
t6  = ("传智教育","黑马程序员","python")
index = t6.index("黑马程序员")
print(f"在元组中查询黑马程序员，下标是：{index}")

#count 统计方法
t7  = ("传智教育","黑马程序员","python","黑马程序员","黑马程序员")
num = t7.count("黑马程序员")
print(f"黑马程序员的元素数量是：{num}")


#len函数统计元组的元素数量
t8  = ("传智教育","黑马程序员","python","黑马程序员","黑马程序员")
num = len(t8)
print(f"num中元素的数量有：{num}")



#while 循环进行遍历
index = 0
while index < len(t8):
    print(t8[index])
    index += 1


#for循环

for elem in t8:
    print(f"元组中的elem有:{elem}")


#定义一个元组
t9 = (1,2,["itheima","itcast"])
print(f"t9的内容是：{t9}")
t9[2][0] = "黑马程序员"
t9[2][1]= "传智教育"
print(f"t9的内容是：{t9}")

