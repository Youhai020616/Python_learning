"""

演示函数作为参数进行传递
"""

#定义一个函数，接受另一个函数传入参数

def test_func(computer):
    result = computer(1,2)#确定computer是一个函数
    print(f"computer的参数的参数类型是{type(computer)}")
    print(f"计算结果是{result}")


#定义一个函数准备作为参数传入另一个函数

def computer (x,y):
    return x+y


#调用，并传入函数
test_func(computer)