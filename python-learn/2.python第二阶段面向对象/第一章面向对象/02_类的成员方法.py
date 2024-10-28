#函数：写在类的外部。方法：写在类，内部的函数
#在成员方法的内部，必须使用self作为第一个参数

"""
演示面向对象类的成员方法的定义和使用
"""
#定义一个带有成员方法的类
class Student:                                    #类名

    name = None                                   #类的属性   name 是类的成员变量，

                                                 #类的行为，成员方法
                                                 #注意函数是写在类外的，定义在类的内部，我们都称之为方法
    def say_hi (self):
        print(f"hi, my name is:{self.name} ")

    def say2_hi(self,msg):  #say_hi2：作为成员方法
        print(f"hi, my name is:{self.name} , {msg} ")
#想要访问成员属性必须使用self关键字

stu = Student()
stu.name = "周杰伦"
stu.say2_hi("哎呦，不错呦")


stu2= Student()
stu2.name = "林俊杰"
stu2.say2_hi("小伙子，我看好你")


"""
总结：
1.类的组成：
    类的属性，称之为：成员变量
    类的行为，称之为，成员方法

2.类和成员方法的定义语法
class 类名称：
    成员变量
    
    def 成员方法（self,参数列表）：
        成员方法体
        
对象名 = 类名称


3.self 的作用
    表示类对象本身的意思
    只有通过self，成员方法才能访问类的成员变量
    
"""

