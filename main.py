from animais import Animais
from mamiferos import Mamiferos
from aves import Aves
from repteis import Repteis

a1 = Animais('JACARE', 11, 235, '')
a2 = Mamiferos('Lemori', 11, 235, '', '',0)
a3 = Aves('Pato', 2, 55, '', '', 0)
a4 = Repteis('Lagarto', 5, 10, '', '', '', 20)

a1.comer('peixe')
a1.comer('frango')
a1.parar_comer()
a1.parar_comer()
a1.comer('arroz')
a1.dormir()
a1.comer('Maçã')
a1.parar_comer()
a1.dormir()
a1.dormir()
a1.comer('pinha')
a2.comer('peixe')
a2.dormir()
a2.parar_comer()
a2.dormir()
a3.dormir()
a4.comer('Mosca')