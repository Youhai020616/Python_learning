 #例如__init__构造方法，是python类内置方法之一
 #魔术方法：内置的类方法

#字符串方法__str__
class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age


#__str__魔术方法
    def __str__(self):
        return "姓名:%s 年龄:%d"%(self.name,self.age)


#__lt__小于符号比较方法
    def __lt__(self,other):
        return self.age < other.age

#__le__用于小于等于或者大于等于的比较逻辑
    def __le__(self,other):
        return self.age <= other.age

#__eq__用于等于或者不等于的比较逻辑
    def __eq__(self,other):
        return self.age == other.age


stu1 = Student("周杰伦",31)
stu2 = Student("林俊杰",31)
print(stu1==stu2)
print(stu1>stu2)




