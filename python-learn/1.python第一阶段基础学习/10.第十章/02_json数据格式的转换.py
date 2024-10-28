# #负责不同语言之间的数据传递和交互
# "python - json - c语言接受json的数据格式并转化为c格式继续使用"
# "c格式数据 - json - python 程序接受json的数据格式并转化为python格式继续使用"

import json
#准备一个列表，转化为json
data = [{"name":"张大山","age":11},{"name":"王大锤","age":13},{"name":"赵小虎","age":16}]
josn_str=json.dumps(data,ensure_ascii=False)
print(josn_str)
print(type(josn_str))


#准备一个字典，将字典的内容转化为Json
d = {"name":"周杰伦","addr":"台北"}
josn_str=json.dumps(d,ensure_ascii=False)
print(josn_str)
print(type(josn_str))


#将json字符串转化为python 数据格式
s ='[{"name": "张大山", "age": 11}, {"name": "王大锤", "age": 13}, {"name": "赵小虎", "age": 16}]'
l = json.loads(s)
print(l)
print(type(s))
print(type(l))

#将json字符串转换为python 数据格式
s = '{"name": "周杰伦", "addr": "台北"}'
l = json.loads(s)
print(l)
print(type(s))
print(type(l))