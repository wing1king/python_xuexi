# 类：洗衣服 功能 洗衣服

class Washer(object):
    def wash(self):
        print('洗衣服')
        print(self)


haier = Washer()
print(haier)
haier.wash()

# 由于打印对象和打印self得到的内存地址相同，所以self指的是调用该函数的对象
