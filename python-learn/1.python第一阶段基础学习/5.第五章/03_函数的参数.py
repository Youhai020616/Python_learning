# #传入参数，在函数计算的时候，能够传入参数
# def add(x,y):
#     result=x+y
#     print(f"{x}+{y}的计算结果是：{result}")
#
# #调用结果
# add(5,6)
#


#案例
def check(num):
    print("欢迎来到黑马程序员！请出示您的健康吗以及72小时核酸证明")
    if num <=37.5:
        print(f"体温测量中，您的体温是{num}度，体温正常请进")
    else:
        print(f"体温检测中，您的体温是{num}度，需要隔离")

check(67)