
#对list 进行切片，从1开始，到4结束，步长为1、
my_list =[0,1,2,3,4,5,6]
my_list1=my_list[1:4:1] #步长默认为1，可以省略不写
print(f"结果1：{my_list1}")

#对tuple 进行切片，从头开始，最后结束，步长为1
my_tuple =(0,1,2,3,4,5,6)
my_tuple1=my_tuple[:] #步长默认为1，可以省略不写
print(f"结果2：{my_tuple1}")

#对str进行切片，从头开始，最后结束，步长为2
my_str ="01234567"
my_str3 =my_str[::2]
print(f"结果3：{my_str}")


#对str进行切片，从头开始，最后结束，步长为-1
my_str ="01234567"
my_str4 =my_str[::-1]
print(f"结果4：{my_str4}")


#对list 进行切片，从3开始，最后结束，步长为-1
my_list5 =[0,1,2,3,4,5,6]
result5 = my_list5[3:1:-1]
print( f"结果5：{result5}")

#对元组进行切片，从头开始，最后结束，步长为-2

my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::2]
print(
    f"结果6：{result6}"
)


