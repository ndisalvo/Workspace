def miFuncion():
    print('mi primera funcion')

#miFuncion()

def funcionConParametros(nombre, apellido):
    print('el nombre completo es:', nombre, apellido)

funcionConParametros('Nicolas', 'Di Salvo') #pasamos manualmente la cantidad de parametros que hayamos puesto dentro de los () de la funcion


def funcionConMultiplesParametros(*nombres): #el * hace referencia a que va a recibir mas de un solo argumento 
    print('Argumentos:', nombres)

funcionConMultiplesParametros('A', 'E', 'I', 'O', 'U')  #Esto lo va a imprimir en forma de una tupla 


#como podemos hacer que una funcion corra sin que le tengamos que pasar parametros? se los pasamos al momento de definirla:
def miFuncion2(nombre = 'Nicolas'):
    print(nombre)

miFuncion2()

#imprimiendo una lista con for dentro de una funcion
def imprimiendoUnaLista(lista):
    for el in lista: #el -> elemento
        print(el)

imprimiendoUnaLista(['Hola', 'Mundo'])

#concatenando nombres:
def concatenandoNombres(listaNombres):
    i = ''
    for el in listaNombres:
        i = i + el + ' '
    return i #cuando hacemos un return, hay que almacenar el nombre de dicha funcion dentro de una variable y despues imprimirla

nombres_a_imprimir = concatenandoNombres(['Mimo', 'Kira'])
print(nombres_a_imprimir)
