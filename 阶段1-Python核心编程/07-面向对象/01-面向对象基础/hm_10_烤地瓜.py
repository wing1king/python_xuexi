# 1.定义类： 初始化属性、被烤和添加调料的方法、显示对象信息的str

class SweetPotato(object):
    def __init__(self):
        # 被烤的时间
        self.cook_time = 0
        # 烤的状态
        self.cook_state = '生的'
        # 调料列表
        self.condiments = []

    def cook(self, time):
        """烤地瓜的方法"""
        # 1. 先计算地瓜整体考过的时间
        self.cook_time += time
        # 2. 用整体考过的时间再判断地瓜的状态
        if 0 <= self.cook_time < 3:
            # 生的
            self.cook_state = '生的'
        elif 3 <= self.cook_time < 5:
            # 半生不熟
            self.cook_state = '半生不熟'
        elif 5 <= self.cook_time < 8:
            # 熟了
            self.cook_state = '熟了'
        elif self.cook_time >= 8:
            # 糊了
            self.cook_state = '烤糊了'

    def add_condiments(self, condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f'这个地瓜被烤过的时间是--{self.cook_time}分钟, 生熟状态是--{self.cook_state}, 加的调料有--{self.condiments}'


# 2. 创建对象并调用对应的实例方法

digua1 = SweetPotato()
# print(digua1)

digua1.cook(1)
digua1.add_condiments('蜂蜜')
print(digua1)

digua1.cook(5)
digua1.add_condiments('白砂糖')
print(digua1)