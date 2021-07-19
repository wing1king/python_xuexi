# 1.任意三个数之和

def sum_num(a, b, c):
    return a + b + c


result = sum_num(1, 2, 3)
print(result)


# 2.任意三个数求平均值
def avg_num(a, b, c):
    sum_result = sum_num(a, b, c)
    return sum_result / 3


avg_num_result = avg_num(1, 2, 9)
print(avg_num_result)