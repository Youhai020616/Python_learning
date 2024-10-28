#多态：完成莫格行为时，使用不同的对象会得到不同的状态

"""
演示面向对象的多态性以及抽象类接口的使用
"""



class Animal :
    def speak(self) :
        pass
#抽象类：含有抽象方法的类
#抽象方法：方法体时空实现（pass）称之为抽象方法
#抽象类不能被实例化
#这样的抽象类又称之为接口


class Dog(Animal) :

    def speak(self) :
        print('汪汪')

class Cat(Animal) :

    def speak(self):
        print("喵喵喵")

def make_noise (animal:Animal):
    """制造点噪音，需要传入Animal对象"""

    animal.speak()

dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)

#抽象类(接口):用来做顶层设计
class AC:

    def cool_wind(self):
        pass

    def hot_wind(self):
        pass

    def swing_wind(self):
        pass

class Midea_AC(AC):
    def cool_wind(self):
        print('美的空调制冷')
    def hot_wind(self):
        print("美的空调制热")
    def swing_wind(self):
        print("美的空调摇摆")

class GREE_AC(AC):
    def cool_wind(self):
        print('TCL空调制冷')
    def hot_wind(self):
        print("TCL空调制热")
    def swing_wind(self):
        print("格力空调摇摆")

def make_cool(ac:AC):
    ac.cool_wind()


midea_ac = Midea_AC()
gree_ac = GREE_AC()

make_cool(gree_ac)
make_cool(midea_ac)