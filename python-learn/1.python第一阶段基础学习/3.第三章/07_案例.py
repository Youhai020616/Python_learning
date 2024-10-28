num = 5

#通过键盘输入的猜想的数字

if  int(input("猜想一个数字")) ==num:
    print("猜对了")
elif int(input("猜错了，再猜一次")) == num:
    print("猜对了")
elif int(input("猜错了。再猜一次"))==num:
    print("最后一次机会，猜对了")
else:
    print("soory")