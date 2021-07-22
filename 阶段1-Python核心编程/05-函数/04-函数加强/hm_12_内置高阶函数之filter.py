# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2. 定义功能函数：过滤序列中的偶数
def func(x):
    return x % 2 == 0


# 3. 调用filter
result = filter(func, list1)
print(result)   # 打印内存地址
print(list(result))
