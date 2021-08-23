#While

i = 0
while i < 5: #mientras que i sea menor a 5:
    print(i) #imprime el valor actual de i
    i += 1   #incrementa en 1 el valor de i gracias al +=

print('\n********\n')

x = 0
while x < 5:
    if x == 3: #si x llega a valer 3, entonces cortamos el script aca y todo lo que haya debajo no se ejecuta
        break
    print(x)
    x += 1

print('\n********\n')

y = 0
while y < 5:        #es mayor a 5? 
    y += 1          #si no lo es entonces incrementamos el valor de Y en 1
    if y == 3:      #y tiene valor 3?
        continue    #entonces salteamos todo lo que venga abajo y vovlemos a empezar el while pero no imprimimos el valor de 3
    print(y)        #porque nos saltamos esta operacion de print

print('\n********\n')


#For
 
#se utilizan generalmente cuando queremos iterar datos (podemos hacer uso de los break y continue del While)

#imprimiendo todos los datos de una lista:
usuarios = ['apple', 'xiaomi', 'huawei', 'realme']

for usuario in usuarios:
    print(usuario)

print('\n********\n')

#imprimiendo cada caracter de un array:
nombre = 'Nicolas'
for c in nombre: #la c representa la palabra caracter, pero podemos elegir cualquier palabra o letra que querramos poner en esta instancia
    print(c)     #siempre hay que poner dentro de los () a la hora de imprimir lo que estemos buscando con el For, en este caso 'c'

print('\n********\n')

for x in range(1, 6): #los parametros dentro del (): 1 hace referencia al numero donde comienza y el 6 donde termina, siempre llega hasta un numero antes
    print(x) 

print('\n********\n')

#si nosotros quisieramos ir incrementando mas de 1 a la vez, se pasa un 3er parametro dentro del () y ese va a determinar de cuanto va a ir subiendo
for num in range (1, 20, 2):
    print(num)
else: #el else se pone en los For loops cuando hayamos terminado de iterar
    print('hemos terminado!')

print('\n********\n')

#for dentro de otro for
ninjas = ['naruto', 'sasuke', 'sakura']
edades = [15, 16, 16]

for ninja in ninjas:
    for edad in edades:
        print(ninja, edad)   #va a imprimir cada ninja con cada edad posible antes de volver a imprimir al siguiente ninja
    
    
    
    
    

    
    