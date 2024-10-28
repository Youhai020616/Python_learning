#通过占位形式，完成拼接
from turtledemo.clock import setup

name ="黑马程序员"
message = "学IT来黑马：%s" %name
print(message)

#通过占位的形式，完成数字和字符串的拼接
class_num= 57
avg_salary =16781
message = "python 大数据学课，北京%s期，毕业工资：%s" %(class_num,avg_salary)
print(message)


#注：%：表示我要占位
# s :将变量转换成字符串的形式放在需要占位的地方



"""
%s : 将内容转成字符串的形式，放入占位位置
%d : 转换成整数的形式，放在占位位置
%f : 转换成浮点型，放在占位位置
"""

name = "传智播客"
setup_year =2006
stock_price = 19.19
message = "%s,成立于:%d,今天的股价是:%f" %(name,setup_year,stock_price)
print(message)


num1 = 11
num2 = 11.345
print("数字11宽度限制为5，结果是：%5d"%num1)
print ("数字11宽度限制为1，结果为：%1d"%num1)
print ("数字11.345宽度限制为7，小数精度2，结果为：%7.2f"%num2)
print ("数字11.345宽度不限制，小数精度为2，结果是：%.2f"%num2)



name ="传智播客"
setup_year =2006
stock_price = 19.19
#f:format
print(f"我是{name},我成立于{setup_year}，今天的股票市价是{stock_price}")

#字符串格式化——表达式格式化

print("1*1的结果是：%d"%(1*1))
print(f"1*2的结果是：{1*2}")
print("字符串在python中的类型名是：%s" %type ("字符串"))


#temple

name = "传智播客"
stock_code =" 003032"
stock_price = 19.19
stock_price_daily_growth_factor =1.2
growth_days = 7
finally_stock_price = stock_price * stock_price_daily_growth_factor**growth_days
print(f"公司{name},股票代码：{stock_code},当前股价：{stock_price}")
print ("每日增长系数：%s, 经过%d天的增长，股价达到了：%.2f"%(stock_price_daily_growth_factor,growth_days,finally_stock_price))



name = input("请输入你的名字:")
print("我知道了,你是：%s"%name)

#输入数字类型
num = input("请输入你是银行卡密码:")

num = int(num)
print("你的银行卡密码的类型是：",type(num))




