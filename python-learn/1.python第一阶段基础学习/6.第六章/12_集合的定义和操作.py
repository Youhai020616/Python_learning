#基本语法
#{元素，元素...}

#集合的定义
my_set={"传智教育","黑马程序员","传智播客"}
my_set_empty= set()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")
print(f"my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}")


#添加新元素
my_set.add("python")
my_set.add("传智教育")
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")

#移除元素
my_set.remove("黑马程序员")
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")

#从集合中随机取出一个元素
my_set = {"传智教育", "黑马程序员", "黑马程序员"}
element = my_set.pop()
print(f"从集合中随机取出的元素是：{element}")

#清空集合
my_set.clear()
print(f"my_set的内容是：{my_set}，类型是：{type(my_set)}")

#取两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}

set3 = set1.difference(set2)
print(f"set3的内容是：{set3}，类型是：{type(set3)}")
print(f"set1的内容是：{set1}，类型是：{type(set1)}")
print(f"set2的内容是：{set2}，类型是：{type(set2)}")


#消除两个集合的差集
set1 = {1,2,3}
set2 = {1,5,6}
set1.difference_update(set2)

print(f"set1的内容是：{set1}，类型是：{type(set1)}")
print(f"set2的内容是：{set2}，类型是：{type(set2)}")


#2个集合合并
set1 = {1,2,3}
set2 = {1,5,6}
set3 = set1.union(set2)
print(f"set3的内容是：{set3}，类型是：{type(set3)}")

#统计集合元素的数量len()
set1 = (1,2,3,4,5,1,2,3,5,6)
num = len(set1)
print(f"set1的元素个数是：{num}")

#集合的遍历
#集合不支持下标索引，不支持for循环
set1 = {1,2,3,4,5,1,2,3,5,6}
for element in set1:
    print(f"集合的元素有：{element}")




