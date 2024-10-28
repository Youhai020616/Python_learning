# print ("hello world",end='')
# print("world",end='')


# print("hello\tworld")
# print("itheima\tbest")

#九九乘法表
#控制行的循环（i<=9)，控制每一行输出的循环(j<=i)

#定义外层循环的控制变量
i = 1
while i <=9:

    #定义内层循环的控制变量
    j = 1
    while j <= i:
        print(f"{j}*{i}={j*i}\t",end='')
        j += 1

    i += 1
    print()