# if int(input("你的身高是多少"))>120:
#     print("身高超出120，不可以免费")
#     print("但是，如果VIP级别大于3,可以免费")
#
#     if int (input("你的VIP级别是")) > 3:
#         print("可以免票")
#     else:print("SOORY 你需要买票")
# else:
#     print("欢迎你")


age = int (input("请输入你的年龄"))
year = int (input("请输入你入职的时间"))
level = int (input("请输入你的等级"))
if age >=18:
    print("你是成年人")
    if age > 30:
        print("你的年龄达标")
        if year > 2:
            print("都达标了，可以领取礼物")
        elif level>3:
            print("可以领取礼物")
        else:
            print("不好意思，尽管年龄达标，但是入职时间不达标")
    else:
        print("不好意思年龄太大了")
else:
    print("不好意思，小朋友不可以领取")