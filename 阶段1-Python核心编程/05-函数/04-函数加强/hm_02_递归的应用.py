# 需求： 3以内的数字累加和 3+2+1 = 6
# 6 = 3+2以内数字累加和
# 2以内数字累加和 = 2 + 1以内数字累加和
# 1以内数字累加和 = 1 # 出口


# 递归特点：函数内容自己调用自己，必须有出口，否则死循环


def sum_numbears(num):
    # 2. 出口
    if num == 1:
        return 1
    # 1. 当前数字 + 当前数字-1的累加和
    return num + sum_numbears(num - 1)


result = sum_numbears(3)
print(result)

# 如果没有出口，报错：超出最大递归深度
