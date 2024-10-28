import random
num = random.randint(1,10)

guess_num = int (input("输入你要猜测的数字:"))

if guess_num == num:
    print("猜中了")
else:
    if guess_num > num:
        print("你输入的数字太大了")
    else:
        print("你输入的数字小了")
    guess_num = int (input("再次输入你要猜的数字："))
    if guess_num == num:
        print("恭喜你，猜中了")
    else:
        if guess_num > num:
            print("你猜的数字太大了")
        else:
            print("你猜的数字太小了")
        guess_num = int(input("请输入你第三次要猜测的数字"))
        if guess_num == num:
            print("恭喜你，猜中了")
        else:
            print("三次机会用完了，没有猜中")
