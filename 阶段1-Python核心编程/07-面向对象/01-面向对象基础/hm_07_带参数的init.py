# 定义类： 带参数的init： 宽度和高度 实例方法： 调用实例属性


class Washer(object):
    def __init__(self, width, height):
        # 添加实例属性
        self.width = width
        self.height = height

    def print_info(self):
        print(f'洗衣机的宽度是{self.width}')
        print(f'洗衣机的高度是{self.height}')


haier = Washer(100, 200)
haier.print_info()

haier1 = Washer(800, 1600)
haier1.print_info()