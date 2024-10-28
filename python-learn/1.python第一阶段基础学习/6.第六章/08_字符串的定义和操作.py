from itertools import count
from operator import index

#下标索引
my_str = "itheima and itcast"

value1 = my_str[2]
value2 = my_str[-9]

print(f"{value1} and {value2}")

#index方法

value = my_str.index("and")
print(f"查找在{my_str}中查找and 起始下标是：{value}")

#replace 方法
new_my_str =my_str.replace("it","程序")
print(f"替换成新的字符串：{new_my_str}")


#spile 方法

my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行切分的结果是：{my_str_list}，类型是：{type(my_str_list)}")


#strip
my_str = "     itheima and itcast "
new_my_str = my_str.strip()#不传入参数，默认去除前后空格
print(f"字符串{my_str},被strip后的结果是：{new_my_str}")

my_str = "12itheima and itcast21"
new_my_str = my_str.strip("12")
print(f"字符串{my_str}被strip后得到的结果是：{new_my_str}")

#count
my_str ="itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it的数量有：{count}个")

#len
num =len(my_str)
print(f"字符串my_str的长度是：{num}")




