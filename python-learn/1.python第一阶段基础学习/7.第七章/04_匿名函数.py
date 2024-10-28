#匿名函数lambda
#只能临时调用一次
#具体语法
#lambda 传入参数：函数体


def test_func (computer):
    result = computer(1, 2)
    print(f"结果是：{result}")


def add(x, y):
    return x + y
print(add(1, 2))


# test_func(lambda x, y: x + y)#通过lambda 匿名函数的形式，将匿名函数作为参数传入







