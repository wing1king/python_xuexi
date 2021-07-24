class Master(object):
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


class School(Master):
    def __init__(self):
        self.kongfu = '[黑马煎饼果子配方]'

    def make_cake(self):
        print(f'运用{self.kongfu}制作的煎饼果子')


class Prentice(School):
    def __init__(self):
        self.kongfu = '[独创的煎饼果子技术]'
        # self.money = 20000
        self.__money = 20000

    def __info_print(self):
        print('这是私有方法')

    def make_cake(self):
        self.__init__()
        print(f'运用{self.kongfu}制作的煎饼果子')

    def make_master_cake(self):
        Master.__init__(self)
        Master.make_cake(self)

    def make_school_cake(self):
        School.__init__(self)
        School.make_cake(self)


class Tusun(Prentice):
    pass


xiaoqiu = Tusun()
print(xiaoqiu.mooney)
print(xiaoqiu.__money)

# xiaoqiu.__info_print()