#de esta forma no importamos el modulo entero ya que a veces no vamos a necesitar TODO el modulo sino que una o un par de funciones
from modulos2 import holaMundo

#podemos importar varias cosas desde variables hasta funciones
from modulos import saludo, nombres 

holaMundo('Python'); saludo(); print(nombres) #con el ; podemos ejecutar varios comandos simples en una linea. Podemos hacer esto con los import tambien pero no creo que sea recomendable a menos que sean MUY pocos 