class Washer(object):
    def wash(self):
        print('洗衣服')

    # 获取实例属性
    def print_info(self):
        # self.属性名
        print(f'洗衣机的宽度是{haier.width}')
        print(f'洗衣机的高度是{haier.height}')


haier = Washer()

# 添加属性
haier.width = 400
haier.height = 800

# 对象调用实力方法
haier.print_info()