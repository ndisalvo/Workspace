c = open('archivoEjemplo.txt', 'a') #de esta forma abrimos el archivo ***
#print(c.read()) #de esta forma leemos el archivo .txt entero
#print(c.readline()) #esto nos permite leer linea a linea el archivo. Recomendado si el archivo es grande


'''

*** en el metodo open('nombreDelArchivo') nosotros podemos pasar mas argumentos dentro del () a modo de permisos como por ej:
open('nombreDelArchivo', 'r') -> la 'r' hace referencia al 'read', lo podemos poner para ser mas explicitos
open('nombreDelArchivo', 'a') -> la 'a' hace referencia al 'append', lo podemos para tener permisos de añadir al final de todo en este caso, texto
open('nombreDelArchivo', 'w') -> la 'w'  hace referencia al 'write', nos permite modificar todo el archivo entero. En caso de que el archivo no exista, con este metodo Python crea el archivo solicitado
open('nombreDelArchivo', 'x') -> la 'x' nos permite crear un archivo con el nombre que hayamos asignado


#como interpretar las lineas del texto de manera independiente:
for x in c:
    print(x)

'''

#agregando cosas al archivo .txt: agregamos 'a' como permiso al metodo de open()
c.write('\nagregando linea al archivo con Python') #al añadir cosas nos va a tirar error si queremos leer el archivo


#al finalizar de leer y/o modificar un archivo la buena costumbre es cerrarlo, como? de la siguiente manera:
c.close()    