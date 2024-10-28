from itertools import count

str1 = "itheima"
str2 = "itcast"
str3 ="python"


count = 0
for i in str1:
    count = count + 1
print(f"字符串{str1}的长度是：{count}")



#可以使用函数来优化一下功能
def my_len(data):
    count = 0
    for i in data:
        count = count + 1
    print(f"字符串{data},的长度是：{count}")

my_len(str1)
my_len(str2)
my_len(str3)
