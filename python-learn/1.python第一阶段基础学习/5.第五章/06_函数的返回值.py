# #函数的返回值，函数在完成之后，返回给调用者的结果
#
# def add(a,b):
#     result = a+b
#     return res
#
#
#
# #函数的返回值可以通过变量去接受
#
# r = add(5,6)
# print(r)


# None类型

def say_hello():
    print('Hello World!')

result = say_hello()
print(f"无返回值函数，返回的内容是{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")


def say_hello2():
    print('Hello World!')
    return None

result = say_hello2()
print(f"无返回值函数，返回的内容是：{result}")
print(f"无返回值函数，返回的内容类型是：{type(result)}")


#在if判断上，None 等同于 false

def check_age(age):
    if age >18:
        return "success"
    else:
        return None

result = check_age(16)
if not result:
    print("未成年，不可进入")

name = None
#声明无初始值的变量的定义
