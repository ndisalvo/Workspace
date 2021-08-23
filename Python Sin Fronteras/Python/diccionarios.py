#Diccionarios

diccionario = {
    'nombre' : 'Mimo',
    'animal' : 'gato',
    'edad' : '5 meses ',
    'ronronea' : 'si'
}


diccionario['nombre'] = 'Abemus Mimus' #para reemplazar el valor de un item de un diccionario
diccionario['color'] = 'Naranja y Blanco' #para agregar un item al diccionario
#diccionario.pop('color') #para eliminar un item del diccionario usamos .pop() y especificamos dentro de los () el nombre del item
#del diccionario['color'] #elimina el item introducido dentro de los (), igual que el .pop()
diccionario.popitem() #el metodo .popItem() elimina el ultimo valor agregado al diccionario, si no se agrego nada entonces no se elimina nada
#diccionario.clear() #elimina todo el contenido de un diccionario

print(diccionario)
print(diccionario['nombre']) #para acceder a un item del diccionario tenemos que usar la misma sintaxis de las listas
print(diccionario.get('edad')) #con el .get() hacemos lo mismo que arriba solo que de forma mas explicita
print(len(diccionario)) #para calcular la cantidad de items que hay dentro del diccionario

#Para copiar un diccionario hacemos igual que con las listas o usamos el metodo dict:
copiaDiccionario = diccionario.copy()
print(copiaDiccionario)

copiaDiccionario2 = dict(diccionario)
print(diccionario)


#Diccionarios Anidados

#forma1:

Jedis = {
    'Anakin' : {
        'nombre' : 'Anakin Skywalker',
        'nivel' : 'Caballero jedi'
    },

    'Obi-Wan': {
        'nombre' : 'Obi-Wan Kenobi',
        'nivel' : 'Maestri Jedi'
    }
}


#forma2:

Palpatine = {
    'nombre': 'Sheeve Palpatin',
    'nivel' : 'Emperador'
}

Dooku = {
    'nombre' : 'Conde Dooku',
    'nivel' : 'Señor Oscuro'
}

Sith = {
    'Palpatine' : Palpatine,
    'Dooku' : Dooku
}

print(Sith)


#forma3:

perros = dict(nombre = 'Lars', edad = 13, raza = 'Labrador')
print(perros)