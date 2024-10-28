#复写：子类在继承父类的属性和成员属性后，可以进行复写

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("5g通话")

#定义字类，复写父类成员

class MyPhone(Phone):
    producer = "ITHIMA"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        print("使用5g进行通话")
        print("关闭CPU单核模式")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)

#调用父类名同名成员

print(f"父类的厂商：{Phone.producer}")
Phone.call_by_5g(self=Phone)
print("关闭CPU，确保性能")



