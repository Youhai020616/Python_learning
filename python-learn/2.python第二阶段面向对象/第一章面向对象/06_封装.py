#面向对象：基于模板（类），去创建实体（对象），使用对象完成功能开发
"""
面向对象的三大特性：
封装：将现实世界的事物的属性和行为封装到类中描述为成员变量和成员方法
继承：
多态：
"""
#类提供了私有成员来支持：私有成员变量，私有成员方法
"""
#定义私有成员变量
class Person:
    name = None
    age = None
    #定义私有成员变量
    __weight = 65
    
        #定义私有成员方法
    def __init__(self, name, age):
        self.name = name
        self.__age = age
"""


#演示面向对象封装思想中私有成员的使用
#定义一个类，内含私有成员变量和私有成员方法


class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("让cpu以单核模式运行")

    def call_by_5g(self):
        if self.__current_voltage >=1:
            print("5g模式")
        else:
            self.__keep_single_core()
            print("电量不足，无法使用5g,并设置为单核模式运行")

phone =Phone()
phone.call_by_5g()

#封装：就是将现实中的事物描述为属性和方法
#类对象无法访问私有成员
#类中的其它成员可以进行访问

#私有成员的实际意义：在类中提供仅供内部使用的属性和方法而不对外开放











