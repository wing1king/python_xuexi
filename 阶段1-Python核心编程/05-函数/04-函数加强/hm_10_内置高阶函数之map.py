# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5]


# 2. 准备2次方计算的函数
def func(x):
    return x ** 2


# 3. 调用map
result = map(func, list1)

# 4. 验收结果
print(result)   # 打印内存地址
print(list(result))