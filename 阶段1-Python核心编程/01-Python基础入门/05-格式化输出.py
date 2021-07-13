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
print("我的体重是%.1f公斤" % weight)   # .1：表示保留一位小数
