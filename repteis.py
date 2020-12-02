from animais import Animais
class Repteis(Animais):
    def __init__(self, nome, idade, peso, corOlhos, tipoEscamas, comprimentoCalda, rastejando = False):
        Animais.__init__(self, nome, idade, peso, corOlhos)
        self.tipoEscamas = tipoEscamas
        self.comprimentoCalda = comprimentoCalda
        self.rastejand = rastejando

    def rastejar(self):
        pass