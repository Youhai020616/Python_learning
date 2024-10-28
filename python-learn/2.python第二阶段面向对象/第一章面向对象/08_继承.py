"""
演示面向对象，继承的基础语法
"""

#演示继承

class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_4g(self):
        print("4g通话")

class Phone2022(Phone):
    face_id = "10010"

    def call_by_5g(self):
        print("2022年新功能，5g通话")

phone = Phone2022()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()



#演示多继承

class NFCReader:
    nfc_type = "第五代"
    producer = "HM"

    def read_nfc(self):
        print("NFC读卡")
    def write_card(self):
        print("NFC写卡")
class RemoteControl:
    rc_type = "红外遥感"

    def control(self):
        print("红外遥控")

class MyPhone (Phone,NFCReader,RemoteControl):
    pass

phone = MyPhone()
phone.call_by_4g()
phone.read_nfc()
phone.control()
phone.write_card()

print(phone.producer)

#多继承中，对于同名成员，如果父类有同名方法或者属性，按照先继承的优先级高于后继承的优先级

#pass关键字的作用：保证方法或者类的定义的完整性