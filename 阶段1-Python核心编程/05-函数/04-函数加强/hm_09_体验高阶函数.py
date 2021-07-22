# 需求：任意两个数字，先进行数字处理（绝对值或四舍五入）在求和计算


# 1. 写法一
# def add_num(a, b):
#     return abs(a) + abs(b)
#
#
# result = add_num(-1.1, 1.9)
# print(result)


# 2. 写法二
def sum_num(a, b, f):
    return f(a) + f(b)


result = sum_num(-1, 5, abs)
print(result)

result1 = sum_num(1.6, 2.2, round)
print(result1)