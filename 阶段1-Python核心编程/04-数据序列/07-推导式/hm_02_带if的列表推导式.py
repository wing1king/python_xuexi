# 需求：0-10偶数数据的列表
# 1.简单列表推导式 range步长
list1 = [i for i in range(0, 10, 2)]
print(list1)

# for循环加if 创建有规律的列表
list2 = []
for i in range(10):
    if i % 2 == 0:
        list2.append(i)

print(list2)

# 把for循环配合if代码 改写 带if的列表推导式
list3 = [i for i in range(10) if i % 2 == 0]
print(list3)