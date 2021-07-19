# 需求：函数3个参数 name，age，gender

def user_info(name, age, gender):
    print(f'您的姓名是{name},年龄是{age}，性别是{gender}')


user_info('python', 30, 'man')
# user_info(20)     # 个数定义和传入不一致会报错
user_info(20, 'TOM', 'man')  # 顺序也和定义必须是一致的，否则导致数据无意义
