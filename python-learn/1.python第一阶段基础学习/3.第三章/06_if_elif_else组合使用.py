height = int (input("Enter your height in cm: "))
vip_level = int(input("Enter your vip level: "))
day = int(input("Enter your day number: "))

if height <120:
     print("身高小于120，可以免票")
elif vip_level>3:
     print("vip级别大于3，可以免票")
elif day ==1:
    print("今天是1号，可以免票")
else:
  print("买票10元")

print("祝您游玩愉快！")