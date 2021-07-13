"""
1.按经验将不同的变量储存不同类型的数据

2.验证这些数据到底是什么类型 -- 检测数据类型 -- type（数据）
"""

# int -- 整型
num1 = 1
print(type(num1))

# float -- 浮点型，就是小数
num2 = 1.1
print(type(num2))

# str -- 字符串，特点：数据都要带引号""
name = "TOM"
print(type(name))

# bool -- 布尔型，通常判断使用，布尔型有两个取值 True 和 Fales
b = True
print(type(b))

# list -- 列表
c = [1, 2, 3]
print(type(c))

# tuple -- 元组
d = (1, 2, 3)
print(type(d))

# set -- 集合
e = {1, 2, 3}
print(type(e))

# dict -- 字典 -- 键值对 K：V
f = {'name': 'TOM', 'age': 20}
print(type(f))