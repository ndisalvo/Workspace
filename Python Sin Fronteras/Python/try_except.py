#calculadora

primero = input('Ingrese un numero: ')
try:
    primero = int(primero) #tratamos de convertir el valor que ingresamos por teclado en un entero
except:
    primero = str #en caso de el valor ingresado no sea un entero lo transformamos a un str


#validando si el valor ingresado es un entero justo despues de haberlo ingresado para no esperar que ingrese el segundo
if primero == str:
    print('Ingresaste mal un dato, por favor ingresa unicamente numeros')
    exit()


segundo = input('Ingrese un numero: ')
try:
    segundo = int(segundo) 
except:
    segundo = str

if segundo == str:
    print('INgresaste mal un dato, por favor ingresa unicamente numeros')
    exit()

print(primero + segundo)    