"""
演示异常，模块，包的综合案例
"""

#创建my_utils 包 在包内创建str_util.py 和file_util.py

import my_utils.str_util as su
import my_utils.file_util as fu

print(su.str_reverse("黑马程序员"))
print(su.substr("itheima", 0, 4))

print(fu.append_to_file("D:/test.txt","itheima"))
print(fu.print_file_info("D:/test.txt"))
