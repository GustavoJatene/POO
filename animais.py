class Animais:

    def __init__(self, nome, idade, peso, corOlhos, comendo=False, dormindo=False):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.corOlhos = corOlhos
        self.comendo = comendo
        self.dormindo = dormindo


    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return
        print(f'O {self.nome} está comendo {alimento}.')
        self.comendo = True

    def p_comer(self):
        if not self.comendo:
            print(f'O {self.nome} continua sem comer.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def dormir(self):
        pass
