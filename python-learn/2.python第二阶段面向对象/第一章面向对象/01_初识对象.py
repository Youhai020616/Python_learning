#使用对象组织数据
"""

1.设计类
class = Student:
    name = None

2.创建对象
stu1 = Student()
stu2 = Student()

3.给对象赋值
stu1.name = "周杰伦"
stu2.name = "林俊杰

"""

#1.设计一个类（类比生活中：设计一张登记表）
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

#2,创建一个对象(打印一张登记表）
stu1 = Student()

#3.给对象的属性赋值（填写表单)
stu1.name = "周杰伦"
stu1.gender = "男"
stu1.nationality = "中国"
stu1.native_place = "北京"
stu1.age = "31"

#4.打印表单
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)

