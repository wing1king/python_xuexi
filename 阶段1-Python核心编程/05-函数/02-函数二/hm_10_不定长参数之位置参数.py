# 接收所有位置参数，返回一个元组
def user_info(*args):
    print(args)


user_info('tom')
user_info('tom', 20)
user_info('tom', 20, 'man')
user_info()
