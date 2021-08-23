class Animal:
    def __init__(self, nombre, sonido) -> str:
        self.nombre = nombre
        self.sonido = sonido

    def saludo(self):
        print('Hola, me llamo', self.nombre, 'y soy un', self.tipo + '. Mi sonido es el:', self.sonido)


class Gato(Animal):
    tipo = 'gato'

class Perro(Animal):
    tipo = 'perro'


gato = Gato('Mimo', 'maullido')
perro = Perro('Lena', 'ladrido')

gato.saludo()
perro.saludo()