mystr = "hello world and itcast and itheima and python"

# 1.find()
print(mystr.find('and'))  # 12
print(mystr.find('and'), 15, 30)  # 指定范围查找 15 开始 30结束
print(mystr.find('ands'))  # -1, ands子串不存在

# 2.index()
# print(mystr.index('and'))   # 12
# print(mystr.index('and'), 15, 30)  # 指定范围查找 15 开始 30结束
# print(mystr.index('ands'))  # 如果index查找的子串不存在，则报错

# 3.count()
# print(mystr.count('and'), 15, 30)  # 指定范围查找 15 开始 30结束
# print(mystr.count('and'))  # 3
# print(mystr.count('ands'))  # 0

# 4.rfind()
# print(mystr.rfind('and'))   # 35
# print(mystr.rfind('ands'))  # -1

# 5.rindex()
# print(mystr.rindex('and'))  # 35
# print(mystr.rindex('ands'))  # 如果index查找的子串不存在，则报错
