counts = {'MBP': 268, 'HP': 125, 'DELL': 201, 'LENOVO': 199, 'ACER': 99}

# 需求：提取电脑台数大于等于200
# 获取所有键值对数据，判断v值大于200 返回 字典
# print(counts.items())

dict1 = {key: value for key, value in counts.items() if value >= 200}
print(dict1)