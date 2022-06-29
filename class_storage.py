from class_product import *

cont = 0
lont = 0
class Storage:
    def __init__(self):
        self.productsList= []

    def save_products(self):
        codE = str(len(self.productsList)+1)
        descryptionE = input('Informe  o nome:\n')
        factoryE = input('Informe o fabricante:\n')
        unitE = input('Informe a quantia do produto:\n')
        priceE = float(input('Valor do produto:\n'))
        self.productsList.append(Product(cod=codE, description=descryptionE, factory=factoryE, unit=unitE,price=priceE))
        print('O código do produto é:',codE,'*')
        print('Produto Adicionado!')
        print('_______________________________________________________________________________________________________')

    def list(self):
        choose = input('Desejo listar todos (A)\nDesejo listar um produto esppecifico (B)\n')
        if choose == 'A' or 'a':
            for i in range(len(self.productsList)):
                print('Código:',self.productsList[i].cod,'/',
                    'Descrição:',self.productsList[i].description,'/',
                    'Fabricante:',self.productsList[i].factory,'/',
                    'Unidades:',self.productsList[i].unit,'/',
                    'Preço: R$',self.productsList[i].price)
                print('___________________________________________________________________________________________________')
        elif choose == 'B' or 'b':
            entry = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if entry == self.productsList[i].cod:
                    print(self.productsList[i])
                else:
                    limo += 1
                if limo == len(self.productsList):
                    print('Código não existente')

    def change_product(self):
        wish = input ('Deseja mudar todos os dados do produto ou um dado em específico?\nSe todos digite (A)\nSe específico digite (E)')
        if wish == 'A' or 'a':
            wishl = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if wishl == self.productsList[i].cod:
                    self.productsList[i].descryption = input('Nova descrição:\n')
                    print('_______________________________________________________________________________________________________')
                    self.productsList[i].factory = input('Novo nome de fabricante:\n')
                    print('_______________________________________________________________________________________________________')
                else:
                    cont += 1
                if cont == len(self.productsList):
                    print('Código não existente')
                print('_______________________________________________________________________________________________________')
        elif wish == 'E' or 'e':
            wishl = input('Informe o código do produto:\n')
            for i in range(len(self.productsList)):
                if wishl == self.productsList[i].cod:
                    will = input ('Deseja mudar a descrição ou o nome de fabricante do produto?\nSe descrição, digite (D)\nSe fabricante, digite (F)\n')
                    if will == 'D':
                        self.listaContatos[i].descryption = input('Nova descrição:\n')
                        print('_______________________________________________________________________________________________________')
                    elif will == 'F':
                        self.listaContatos[i].factory = input('Novo nome de fabricante:\n')
                        print('_______________________________________________________________________________________________________')
                else:
                    lont += 1
                if lont == len(self.productsList):
                    print('Código não existente')
                print('_______________________________________________________________________________________________________')
    def add_product(self):
        lup = input('Digite o código do produto que você deseja adicionar mais unidades')
        for i in range(len(self.productsList)):
            if lup == self.productsList[i].cod:
                luple = int(input('Quantidade que deseja adicionar\n'))
                self.productsList[i].unit = luple
                print('Quantidade de',luple,'Adicionado ao estoque do produto com sucesso!!')

