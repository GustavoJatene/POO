from animais import Animais
from mamiferos import Mamiferos

a1 = Animais('JACARE', 11, 235, '')
a2 = Mamiferos('JACARE2', 11, 235, '', '', 0)

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
a2.sentar()