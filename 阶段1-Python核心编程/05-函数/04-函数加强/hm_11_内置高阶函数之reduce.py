# 1. 准备列表数据
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 2. 导入模块
import functools


# 3. 定义功能函数
def func(a, b):
    return a + b


# 4. 调用reduce，作用：功能函数计算的结果和序列的下一个数据做累计计算
result = functools.reduce(func, list1)
print(result)