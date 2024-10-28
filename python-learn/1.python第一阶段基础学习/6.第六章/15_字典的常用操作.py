"""
演示字典的常用操作
"""
my_dict = {"周杰伦":88,"王力宏":99,"林俊杰":100}

#新增元素
my_dict["刘德华"] = 100
print(f"字典经过新增元素后的结果是：{my_dict}")

#更新元素
my_dict["周杰伦"] = 99
print(f"字典经过更新元素后的结果是：{my_dict}")


#删除元素
score = my_dict.pop("周杰伦")
print(f"字典经过移除元素后的结果是：{my_dict}，周杰伦的考试分数是：{score}")

#清空元素
my_dict.clear()
print(f"字典经过清空元素后的结果是：{my_dict}")

#获取全部key 的相关操作
my_dict = {"周杰伦":88,"王力宏":99,"林俊杰":100}
keys = my_dict.keys()
print(f"获取key的结果是：{keys}")

#遍历字典
#方式1：通过获取全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的key对应的value是：{my_dict[key]}")


#方式2：直接对字典进行for循环，每一次循环都是直接得到key
for key in my_dict:
    print(f"字典的key是：{key}")
    print(f"字典的key对应的value是：{my_dict[key]}")

#统计字典内的元素数量
num = len(my_dict)
print(f"字典的元素个数是：{num}")