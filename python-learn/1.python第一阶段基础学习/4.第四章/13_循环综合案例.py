#定义账余额
money = 10000

#对员工21位进行发工资
for i in range(1,21):
    import  random
    score = random.randint(1,10)

    if score > 5:
        print(f"员工{i}绩效分{score},不满足条件，下一位")
        continue


    #判断余额
    if money >= 1000:
        money -= 1000
        print(f"员工{i},满足条件，发工资1000元，公司账户剩余：{money}")
    else:
        print(f"余额不足，当前余额：{money}元，不发工资了，下个月再来")
        break
