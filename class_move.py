from class_product import *
class Move:
    def __init__(self, msg='******: ', mug='>>>>>:'):
        self.under = []
        self.sober = []
        self.msg = msg
        self.mug = mug

    def sells(self):
        self.msg = '*******: '
        for i in self.under:
            self.msg += '\n - ' + i

    def buys(self):
        self.mug = '>>>>>>>: '
        for i in self.sober:
            self.mug += '\n - ' + i

    def showsells(self):
        print(self.under)

    def showbuys(self):
        print(self.sober)

