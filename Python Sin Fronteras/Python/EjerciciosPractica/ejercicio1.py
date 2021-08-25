#multiplicar dos numeros sin usar el signo de multiplicacion
from os import name


num1 = 2
num2 = 4
res = 0

for x in range(num2):
    res = res + num1

print(res)



#ingresar nombre y apellido e imprimirlo al revez
nombre = input('Ingrese nombre: '); apellido = input('\nIngrese apellido: ')
concatenacion = nombre + ' ' + apellido
print(concatenacion[::-1]) 



#escribir una funcion que encuentre el elemento menor de una lista
listaNumeros = [5, 2, 4, 1, 3]
listaNumeros.sort()
def numeroMenor():
    print(listaNumeros[0])
numeroMenor()



#escribir una funcion que indique si un usuario  mayor de edad o no
def esMayorDeEdad():
    edad = int(input('Indique su edad: '))
    if edad >= 18:
        return('Es mayor de edad')
    else:
        return('No es mayor de edad')

resultadoFinal = esMayorDeEdad()
print(resultadoFinal)            



#indique si un numero es par o impar
numero_a_ingresar = int(input('Ingrese numero: '))
if numero_a_ingresar % 2 == 0:
    print('Se trata de un numero par')
else:
    print('Se trata de un numero impar')    



#escribir un script que reciba una cantidad de numeros infinita hasta decir basta. Luego sumar esos numeros
numerosInfinitos = []
print('Por favor ingrese numeros y cuando quiera salir ingrese "basta"')
while True:
    enterNumbers = input('Ingrese numero: ')
    if enterNumbers == 'basta' or enterNumbers == 'Basta':
        break
    else:
        try:
            enterNumbers = int(enterNumbers)
            numerosInfinitos.append(enterNumbers)
        except:
            print('Dato invalido')
            exit()

resultado = 0

for x in numerosInfinitos:
    resultado += x

print(resultado)



#escribir una funcion que reciba nombre y apellido y los vaya agregando a un archivo
def recibiendoNombreApellido():
   enterName = input('Ingrese su nombre: ')
   enterLastName = input('Ingrese su apellido: ')

   archivoTxt = open('archivoEjercicio1.txt', 'a')
   archivoTxt.write('nombre: ' + enterName + '\n'); archivoTxt.write('apellido: ' + enterLastName + '\n')
   archivoTxt.close()

recibiendoNombreApellido()    