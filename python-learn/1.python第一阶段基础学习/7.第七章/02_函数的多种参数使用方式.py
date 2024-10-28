"""
演示多种传参形式

"""
def user_info(name, age,gender):
    print(f"名字是:{name},年龄是:{age},性别是:{gender}")

#位置参数-默认传参形式
user_info("周杰伦",18,"男")


#关键字参数
user_info(age=18,gender="男",name="周杰伦")


#缺省参数
def user_info(name,age,gender="男"): #默认参数必须写到最后
    print(f"名字是:{name},年龄是:{age},性别是:{gender}")
user_info("周杰伦",18)

#不定长-位置不定长参数
def user_info(*args):
        print(args)

user_info("周杰伦",18,"男")


#不定长-关键字不定长参数
def user_info(**kwargs):
        print(kwargs)
        print(f"名字是:{kwargs['name']},年龄是:{kwargs['age']},性别是:{kwargs['gender']}")
user_info(name="周杰伦",age=18,gender="男")
