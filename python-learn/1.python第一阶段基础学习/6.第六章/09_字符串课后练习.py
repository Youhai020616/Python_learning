my_str = "itheima itcast boxuegu"

num = my_str.count("it")
print(f"字符串中it 的数量是:{num}")

new_my_str = my_str.replace(" ","|")
print(f"{my_str},被替换的结果是：{new_my_str}")

my_str_list = new_my_str.split("|")
print(f"被分割后的结果是：{my_str_list}")