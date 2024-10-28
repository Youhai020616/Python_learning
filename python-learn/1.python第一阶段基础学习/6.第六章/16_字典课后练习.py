"""
演示字典的课后练习，升职加薪，对所有级别为1的员工，级别上升1级，薪水增加1000元

"""

#组织字典记录数据

info_dict = {
    "王力宏":{"部门":"科技部","工资":3000,"级别":1},
    "周杰伦":{"部门":"市场部","工资":5000,"级别":2},
    "林俊杰":{"部门":"市场部","工资":7000,"级别":3},
    "张学友":{"部门":"科技部","工资":4000,"级别":1},
    "刘德华":{"部门":"市场部","工资":6000,"级别":2}
}
print(f"升级前的员工信息是：{info_dict}")
#for循环进行遍历字典
for name in info_dict:
    #if 条件判断员工的级别
    if info_dict[name]["级别"] == 1:
        #升职加薪操作
        #获取员工的信息字典
        employee_info_dict = info_dict[name]
        #修改员工信息字典
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] = employee_info_dict["工资"] + 1000

        #将员工的信息更新回info_dict
        info_dict[name] = employee_info_dict

#打印升级后的员工信息
print(f"升级后的员工信息是：{info_dict[name]}")
