# 1.定义2个函数
# 2.函数1有返回值50，函数2把返回值50作为参数传入（定义函数2要有形参）


def test1():
    return 50


def test2(num):
    print(num)


# 先得到函数1的返回值，再把这个返回值传入到函数2
result = test1()
test2(result)

test2(test1())