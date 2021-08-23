#calculadora

print('Calculadora\n')

primerNumero = input('Ingrese un numero: ')
try:
    primerNumero = int(primerNumero)
except:
    primerNumero = str
    print('Prueba utilizando unicamente numeros')
    exit()    

segundoNumero = input('Ingrese un numero: ')
try:
    segundoNumero = int(segundoNumero)
except:
    segundoNumero = str    
    print('Prueba utilizando unicamente numeros')
    exit()

operadores = ['+', '-', '*', '/']
operacionElegida = input('Seleccione un operador que desea utilizar: \n a)+\n b)-\n c)*\n d)/\n operador elegido: ')

if operacionElegida == operadores[0]:
    print('Suma:', primerNumero + segundoNumero)
elif operacionElegida == operadores[1]:
    print('Resta:', primerNumero - segundoNumero)
elif operacionElegida == operadores[2]:
    print('Multiplicación:', primerNumero * segundoNumero)
elif operacionElegida == operadores[3]:
    print('Multiplicación:', primerNumero / segundoNumero) 
else:
    print('El valor ingresado no existe')
    exit()       