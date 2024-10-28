# """
# 演示自定义模块
# """
# # # import my_module1
# # from my_module1 import test
# # test(1,3)
#
# #导入不同模块的同名功能
# from my_module1 import test
# from my_module2 import test
# test(1,3)


#__all__变量
from my_module1 import *
test_a(1,3)



