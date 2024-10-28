#语法
from itertools import count
#
# name = "itheima "
# for x in name:
#     print(x)

name = "itheima is a brand of itcast"

count = 0

for x in name:
    if x == "a":
        count += 1
        
print(f"被统计的字符串有{count}个a")