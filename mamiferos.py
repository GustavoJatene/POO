from animais import Animais
class Mamiferos(Animais):
    def __init__(self, nome, idade, peso, corOlhos, corPelos, comprimentoPelos, sentado = False, amamentar = False):
        Animais.__init__(self, nome, idade, peso, corOlhos)
        self.corPelos = corPelos
        self.comprimentoPelos = comprimentoPelos
        self.sentado = sentado
        self.amamentar = amamentar

    def sentar(self):
        if self.sentado:
            print(f'{self.nome} Já está sentado')
            return
        print(f'{self.nome} Sentou')
        self.sentado = True

    def amamentando(self):
        pass