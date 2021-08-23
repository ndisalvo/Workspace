class Usuario:
    def __init__(self, nombre='Mimo', apellido='El Michi') -> str:
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print('Hola, soy', self.nombre, self.apellido)

usuario = Usuario()
usuario.saludo()  #de esta manera accedemos a la funcion de saludo

#si nosotros quisieramos modificar el valor del nombre o del apellido bastaria con hacer:
usuario.nombre, usuario.apellido = 'Kira', 'The Cat' #asignamos nuevos valores a los nombres y apellidos
usuario.saludo()

#como podemos eliminar propiedades a las clases:
#del usuario.nombre  -> usamos la palabra reservada de 'del'
#usuario.saludo() -> arrojaria un error ya que no se encuentra mas el atributo de 'nombre'

#como podemos eliminar una clase entera:
#del usuario -> elimina toda la clase que fue guardada dentro de la variable de usuario