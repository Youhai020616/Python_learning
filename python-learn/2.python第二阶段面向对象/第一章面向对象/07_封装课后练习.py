"""
封装课后练习：设计带有私有成员的手机
"""
from turtle import TurtleGraphicsError


#设计一个类，用来描述手机

class Phone:
#提供私有成员变量：__is_5g_enable
    __is_5g_enable = True  #5g状态

    #提供私有成员方法：
    def __check_5g_(self):
        if self.__is_5g_enable:
            print("5g 已开启")
        else:
            print("5g 未开启,使用4g网络")

    #提供公开成员方法；call_by_5g()
    def call_by_5g(self):
        self.__check_5g_()
        print("正在通话中")

phone =Phone()

phone.call_by_5g()











