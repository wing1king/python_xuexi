# 1. 拆包元组数据
# def return_num():
#     return 100, 200
#
#
# result = return_num()
# print(result)
# num1, num2 = return_num()
# print(num1)
# print(num2)


# 2.字典数据拆包：变量存储的数据是key值
# 先准备字典，然后拆包
dict1 = {'name': 'rose', 'age': 18}
# dict1中有2个键值对，拆包的时候用两个变量接收数据
a, b = dict1
print(a)
print(b)

# vlue值
print(dict1[a])
print(dict1[b])