from class_storage import *
from class_myBank import *
class Shop:
    def __init__(self):
        self.entry = Storage()
        self.bull = Bullet()
        self.account = []
        self.shopcar = []

    def buy(self):
        wishl = input('Informe o código do produto:\n')
        tryr = str(len(self.account)+1)
        for i in range(len(self.entry.productsList)):
            if wishl == self.entry.productsList[i].cod:
                much = int(input('Quantidade que deseja comprar:\n'))
                limial=self.entry.productsList[i].price*much
                self.bull(Bullet(valor=-limial))
                self.entry.productsList[i].unit = much
                print(self.bull(Bullet(valor)))
                print('_______________________________________________________________________________________________________')
            else:
                pass

    def shopping(self):
        while wilt != 'S':
            wilt = input('Informe o código do produto ou digite (S) para sair:\n')
            if wilt == self.entry.productsList[i].cod:
                much = int(input(-('Quantidade que deseja comprar:\n')))
                self.bull=(-(self.entry.productsList[i].price*much))
                print('___________________________________________________________________________________________________________')
