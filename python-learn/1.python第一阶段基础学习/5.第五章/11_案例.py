money=500000
name=None

name = input("请输入你的名字")

def query(show_header):
    if show_header:
        print("-----查询余额-----")
    print(f"{name},你好，你查询的余额：{money}")

def saving(num):
    global money
    money=money+num
    print("-----存款-----")
    print(f"{name},您好余额{money}")

    query(False)


def get_money(num):
    global money
    money=money-num
    print("------取款------")
    print("f{name},您好，你的取款金额{money}")

    query(False)

def main():
    print("------主菜单-----")
    print(f"{name},您好，欢迎来到黑马银行ATM。请选择操作：")
    print("查询余额\t\t[输入1]")
    print("存款\t\t[输入2]")
    print("取款\t\t[输入3]")
    print("退出\t\t[输入4]")
    return input("请输入你的选择")

while True:
    keyboard_input = main()
    if keyboard_input == "1":
        query(True)
        continue
    elif keyboard_input == "2":
        num =int( input("您想要存多少钱"))
        saving(num)
        continue
    elif keyboard_input == "3":
        num = int (input("你想要取多少钱"))
        get_money(num)
        continue
    else:
        print("程序退出")
        break
