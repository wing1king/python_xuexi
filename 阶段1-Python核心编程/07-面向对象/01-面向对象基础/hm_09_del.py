class Washer(object):
    def __init__(self):
        self.width = 300

    def __del__(self):
        print('对象已删除')


haier = Washer()
