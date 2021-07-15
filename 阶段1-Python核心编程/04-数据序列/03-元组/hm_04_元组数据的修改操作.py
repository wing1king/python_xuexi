t1 = ('aa', 'bb', 'cc')

# t1[0] = 'aaa'   # 报错，元组不支持修改

t2 = ('aa', 'bb', ['cc', 'dd'])
print(t2[2])
print(t2[2][0])
t2[2][0] = 'ccc'
print(t2)
