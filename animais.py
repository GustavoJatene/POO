class Animais:

    def __init__(self, nome, idade, peso, corOlhos, comendo=False, dormindo=False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.corOlhos = corOlhos
        self.comendo = comendo
        self.dormindo = dormindo

    def dormir(self):
        if self.comendo:
            print(f'{self.nome} não pode dormir enquanto está comendo.')
            return
        if self.dormindo:
            print(f'{self.nome} já está dormindo.')
            return
        print(f'{self.nome} foi dormir.')
        self.dormindo = True

    def acordar(self):
        if not self.dormindo:
            print(f'{self.nome} já está acordado.')
            return
        print(f'{self.nome} acabou de cordar.')
        self.dormindo = False

    def comer(self, alimento):
        if self.dormindo:
            print(f'{self.nome} não pode dormir enquanto come.')
            return
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo = True


    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} continua sem comer.')
            return
        print(f'{self.nome} parou de comer.')
        self.comendo = False

