"""
1.准备数据
2.格式化符号输出数据
"""

age = 20
name = "TOM"
weight = 75.5
stu_id = 1
stu_id2 = 100

# 1.今年我的年龄是X岁 -- 整数 %d
print("今年我的年龄是%d岁" % age)

# 2.我的名字是X -- 字符串 %s
print("我的名字是%s" % name)

# 3.我的体重是X公斤 -- 浮点数 %f
print("我的体重是%f公斤" % weight)
print("我的体重是%.1f公斤" % weight)  # .1：表示保留一位小数

# 4.我的学号是X -- %d
print("我的学号是%d" % stu_id)

# 4.1 我的学号是001 -- %d
print("我的学号是%03d" % stu_id)  # 03:表示3位数，前面增加2个0
print("我的学号是%03d" % stu_id2)  # 03:表示3位数，前面增加2个0,如果以满足3位则数据不变

# 5.我的名字是X，今年X岁了
print("我的名字是%s，今年%d岁了" % (name, age))

# 5.1我的名字是X，明年X岁了
print("我的名字是%s，明年%d岁了" % (name, age + 1))

# 6.我的名字是X,今年X岁了，体重X公斤，学号是X
print("我的名字是%s,今年%d岁了，体重%.2f公斤，学号是%06d" % (name, age, weight, stu_id))