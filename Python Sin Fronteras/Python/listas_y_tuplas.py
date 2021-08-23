#Listas

lista = [1, 3, 2]
lista2 = lista.copy() #.copy() sirve para copiar los elementos de una lista y almacenarlos en otra
lista.append(4) #.append() agrega el item que introduzcamos dentro de los () a la lista en ultimo lugar
lista.pop() #.pop() sirve para eliminar el ultimo elemento de una lista
lista.remove(1) #.remove() elimina el item que introduzcamos dentro de los ()
lista.reverse() #.reverse() hace que la lista se invierta, es decir, el ultimo elemento pasara a ser el primero y asi sucesivamente
#lista.clear() #.clear() elimina todos los elementos de la lista

listaEjemplo = lista.copy()
listaEjemplo.append(4)
listaEjemplo.sort() #.sort() nos permite ordenar los elementos de una lista en orden numerico o alfabetico (UNICAMENTE SIRVE SI EN LA LISTA LOS ELEMENTOS SON TODOS IGUALES, NO PUEDEN HABER STR Y INT)


print(lista[0]) #para acceder a un item en especifico basta con poner entre [] el numero de indice que tenga ese item
print(lista2, lista2.count(2)) # .count() sirve para ver cuantas veces se repite el item que introduzcamos dentro de los ()
print(len(lista2)) #len() sirve para calcular el largo o la cantidad de items que tiene una lista


#Para calcular el largo de una lista de una forma mas directa podemos hacer:
largoLista1 = len(lista)
largoLista2 = len(lista2)
print(largoLista1, largoLista2)


#o tambien, en un solo renglon:
largoListaUno, largoListaDos = len(lista), len(lista2)
print(largoListaUno, largoListaDos)


#Pequeño Ejercicio:
lista_Uchihas = ['Madara', 'Itachi', 'Sasuke']
lista_Uzumakis = ['Mito', 'Naruto']

lista_Uchihas.append('Shisui')

largoListaUchihas, largoListaUzumakis = len(lista_Uchihas), len(lista_Uzumakis)
print('La lista de los Uchihas tiene:', largoListaUchihas, 'integrantes')
print('La lista de los Uzumakis tiene:', largoListaUzumakis, 'integrantes y Naruto aparece', lista_Uzumakis.count('Naruto'), 'vez')


#Tuplas:
#A diferencia de las Listas, estas no se pueden modificar

mi_tupla = ('Hola', 'mundo', 'desde', 'Python')
print(mi_tupla.count('Hola')) #.count() sirve para lo mismo que en las listas
print(mi_tupla.index('mundo')) #.index() sirve para saber en que posicion se encuentra un elemento en particular

#Para modificar una tupla hace falta que la pasemos primero a una lista:
listaDeTupla = list(mi_tupla)
listaDeTupla.append('3.9')
print(listaDeTupla) 