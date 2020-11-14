class Animais:

    def __init__(self, nome, idade, peso, corOlhos):
        self.__nome = nome
        self.__idade = idade
        self.__peso = peso
        self.__corOlhos = corOlhos

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def idade(self):
        return self.__idade
    @idade.setter
    def idade(self, valor):
        self.__idade = valor

    @property
    def peso(self):
        return self.__peso
    @peso.setter
    def peso(self, valor):
        self.__peso = valor

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
