# 1. 定义类：私有类属性，类方法获取这个私有类属性
class Dog(object):
    @staticmethod
    def info_print():
        print('这是一个静态方法')


# 2. 创建对象
wangcai = Dog()

# 3. 调用静态方法： 类 和 对象
wangcai.info_print()

Dog.info_print()
