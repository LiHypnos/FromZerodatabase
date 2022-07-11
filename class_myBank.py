import datetime


class Bullet:
    def __init__(self, valor=1000.0, payto=0.0):
        self.valor = valor
        self.payto = payto
        self.extract = []
        now = datetime.time
        day = datetime.datetime

    def printr(self):
        print('R$',self.valor)

    def add(self, din):
        self.valor = din
        print('Um valor de R$',din,'foi adicionado a sua conta!')
        print('Seu saldo atual é de R$',self.valor)
        self.extract.append('Um valor de: R$',din,'Foi adicionado na sua conta',now,day)

    def extract_l(self):
        for i in len(range(self.extract)):
            print(self.extract)

