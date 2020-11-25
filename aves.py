from animais import Animais
class Aves(Animais):
    def __init__(self, nome, idade, peso, corOlhos, corDasPenas, tamanhoDasPenas, botandoOvos=False):
        Animais.__init__(self, nome, idade, peso, corOlhos)
        self.corDasPenas = corDasPenas
        self.tamanhoDasPenas = tamanhoDasPenas
        self.botandoOvos = botandoOvos

    def botarOvos(self):
        pass