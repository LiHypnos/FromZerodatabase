from class_storage import *
from class_myBank import *
from class_move import *
class Shop:
    def __init__(self):
        self.entry = Storage()
        self.bull = Bullet()
        self.account = []
        self.shopcar = []
        self.history = Move()

    def buy(self):
        wishl = input('Informe o código do produto:\n')
        tryr = str(len(self.account)+1)
        for i in range(len(self.entry.productsList)):
            if wishl == self.entry.productsList[i].cod:
                much = int(input('Quantidade que deseja comprar:\n'))
                limial=self.entry.productsList[i].price*much
                self.bull.valor-=limial
                self.entry.productsList[i].unit -= much
                print('O valor total da compra foi de: R$',limial)
                print('Seu saldo é de: R$',self.bull.valor)
                self.history.buys.append(Move(f'Compra no valor de: R$',limial,'do item:',self.entry.productsList[i].description,'!'))
                self.history.sells.append(Move(f'Venda no valor de: R$',limial,'do item:',self.entry.productsList[i].description,'!'))
                print('_______________________________________________________________________________________________________')
            else:
                pass

    def shopping(self):
        wilt = str
        while wilt != 'S':
            wilt = input('Informe o código do produto ou digite (S) para sair ou (C) para confirmar as compras:\n')
            for a in range(len(self.entry.productsList[a].cod)):
                if wilt == self.entry.productsList[a].cod:
                    much = int(input('Quantidade que deseja comprar:\n'))
                    self.history.sells.append(Move(f'A quantidade de',much,'do produto',self.entry.productsList[a].cod,'foi selecionada em um carrinho de compras!'))
                    aslut += much
                    limial += self.entry.productsList[a].price*much
                    self.entry.productsList[a].unit -= much
                    print('Preço atual das compras: R$',limial)
                    print('_______________________________________________________________________________________________________')
                    self.history.buys.append(Move(f'O item', self.entry.productsList[a].description,' Foi adicionado no carrinho com sucesso!'))
                    self.history.sells.append(Move(f'Item reservado no carrinho no valor de: R$', limial, 'do item:',self.entry.productsList[i].description, '!'))
                    if wilt == 'C':
                        self.bull.valor -= limial
                        print('Preço total das compras: R$', limial)
                        print('Seu saldo é de: R$', self.bull.valor)
                        print('___________________________________________________________________________________________________________')
                        self.history.buys.append(Move(f'"SHOPPING", compra realizada no valor de: R$',limial,'de um total de ',aslut,'itens!'))
                        self.history.sells.append(Move(f'"SHOPPING" no valor de: R$', limial, 'do item:',self.entry.productsList[i].description, '!'))
            else:
                pass
                print('___________________________________________________________________________________________________________')


