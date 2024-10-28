#字典的定义
#同样和集合一样使用{}来定义字典
#通过：键值对，来定义一个字典

dict = {'key1':'value1','key2':'value2'}

my_dict1 = {"王力宏":99,"周杰伦":88,"林俊杰":100}

#定义空字典

my_dict2 = {}  # 方法1：使用空的花括号定义一个空字典
my_dict3 = dict  # 方法2：使用dict()函数创建一个空字典
print(f"my_dict1的内容是：{my_dict1},类型是：{type(my_dict1)}")
print(f"my_dict2的内容是：{my_dict2},类型是：{type(my_dict2)}")
print(f"my_dict3的内容是：{my_dict3},类型是：{type(my_dict3)}")


#定义字典的重复，新的字典会把重复的老的字典进行覆盖

#从字典中获取value
my_dict1 = {"王力宏":99,"周杰伦":88,"林俊杰":100}
score = my_dict1["王力宏"]
print(f"王力宏的成绩是：{score}")
score = my_dict1["周杰伦"]
print(f"周杰伦的成绩是：{score}")

#定义嵌套字典
stu_score_dict ={
    "王力宏":{"语文":99,"数学":88,"英语":100},
    "周杰伦":{"语文":88,"数学":100,"英语":99},
    "林俊杰":{"语文":100,"数学":99,"英语":88}
}
print(f"stu_score_dict的内容是：{stu_score_dict}")


#从嵌套字典中获取数据
score= stu_score_dict["周杰伦"]["语文"]
print(f"周杰伦的语文成绩是：{score}")
score1 = stu_score_dict["林俊杰"]["英语"]
print(f"林俊杰的英语成绩是：{score1}")