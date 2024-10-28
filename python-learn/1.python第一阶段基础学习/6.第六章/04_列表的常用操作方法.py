"""
#列表的查询功能（方法）

#查询某元素的下标

my_list =["itcast","itheima","python"]

index = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是：{index}")

# index = my_list.index("hello")
# print(f"itheima在列表中的下标索引值是：{index}")

#1修改列表

my_list[0] = "传智教育"
print(f"列表被修改后，结果是：{my_list}")


#2插入元素

my_list.insert(1,"best")
print(my_list)


# 3追加元素

my_list.append("黑马程序员")
print(f"列表追加后的结果是：{my_list}")


#4追加一个新的列表
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(f"在列表后追加一个新的列表,结果是：{my_list}")


#删除某个列表的元素
del my_list[2]
print(f"删除后的结果是：{my_list}")


#取出列表的某个元素
element = my_list.pop(2)
print(f"通过pop取出元素后的列表内容是{my_list},取出的内容是：{element}")


#移除列表中的某个元素
my_list = ["itcast","itheima","python","itheima","itcast"]
my_list.remove("itheima")
print(my_list)

#清空列表
# my_list.clear()
# print(my_list)


#列表中某个元素的数量
my_list = ["itcast","itheima","python","itheima","itcast"]
count = my_list.count("itheima")
print(f"列表中itheima 的数量是{count}")

#
#列表中的元素的总数
my_list = ["itcast","itheima","python","itheima","itcast"]
count = len(my_list)
print(f"列表中的元素数量一共有:{count}个")
"""






my_list = [21,25,21,23,22,20]


my_list.append(31)

my_list.extend([29,33,30])

num1 = my_list[0]
print(f"第一个元素{num1}")

num2 = my_list[-1]
print(f"最后一个元素是{num2}")


index = my_list.index("31")
print(f"31在列表中的位置是：{index}")
print(f"列表的最后内容是：{my_list}")







