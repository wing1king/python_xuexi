def user_info(name, age, gender):
    print(f'您的姓名是{name}，年龄是{age}，性别是{gender}')


# 调用函数传参
user_info('rose', '18', '女')
user_info('tom', gender='男', age=19)  # 关键字参数之间不分先后顺序
# 位置参数必须写在关键字参数的前面
# user_info(age=20, gender='男', 'tome')
