# [(1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# 数据1： 1和2 range（1， 3）
# 数据2： 0 1 2 range（3）

list1 = []
for i in range(1, 3):
    for j in range(3):
        list1.append((i, j))

print(list1)

# 多个for实现列表推导式

list2 = [(i, j) for i in range(1, 3) for j in range(3)]
print(list2)

# 多for的列表推导式等同于for循环嵌套
