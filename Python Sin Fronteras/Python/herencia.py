class Usuario:
    def __init__(self, nombre = 'Madara', apellido = 'Uchiha') -> str:
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola! Me llamo', self.nombre, self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print('Hola! Soy el admin y me llamo', self.nombre)

usuario = Usuario()
admin = Admin()

usuario.saludo()
admin.superSaludo()                   