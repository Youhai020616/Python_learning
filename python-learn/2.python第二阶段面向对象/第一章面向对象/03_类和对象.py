#现实世界的事物：属性和对象
#类和对象

#类是程序内的“设计图纸”。需要基于图纸生产实体（对象），才能工作

"""
演示类和对象的关系，即面向对象的编程套路（思想）
"""

#设计一个闹钟类
class Clock:
    id  = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

#构建2个闹钟让其工作
clock1 = Clock()
clock1.id = "10086"
clock1.price = 19.19
print(f"闹钟1的id是：{clock1.id}, 价格是：{clock1.price}")
clock1.ring()


clock2 = Clock( )
clock2.id = "9000"
clock2.price = 99.99
print(f"闹钟2的id是：{clock2.id}, 价格是：{clock2.price}")
clock2.ring()


