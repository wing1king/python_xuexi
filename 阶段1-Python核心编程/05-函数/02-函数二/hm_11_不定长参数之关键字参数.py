# 收集所有关键字参数，返回一个字典
def user_info(**kwargs):
    print(kwargs)


user_info()
user_info(name='rose')
user_info(name='tom', age=18)