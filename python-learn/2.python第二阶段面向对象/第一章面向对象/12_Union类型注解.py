"""
演示Union 类型注解

"""

#使用Union
from typing import Union

my_list : list[Union[int,str]] = [1,2,3,"itheima"]

def func(data:Union[int,str])  -> Union[int,str]:
    pass
func("itheima")