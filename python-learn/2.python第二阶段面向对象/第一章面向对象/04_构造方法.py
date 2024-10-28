"""
构造方法： __int__()
可以实现的功能:
1,在创建类对象时，会自动执行
2.在创建类对象是，将传入的参数自动传给__int__()方法使用

例；
class student()

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
"""

"""
演示构造方法
"""
#构造方法的名称：__init__

class Student:

    def __init__(self,name,age,tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("student类创建了一个类对象")


stu = Student("张三", 18, "123456")

print(stu.name)
print(stu.age)
print(stu.tel)

"""
名称：__init__
作用：在创建类对象时，会自动执行
构造成员变量是会传参给构造方法，借此可以直接给成员变量进行赋值

"""