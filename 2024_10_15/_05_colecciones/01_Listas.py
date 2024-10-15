# Ejemplos de listas en Python

# Algunas propiedades de las listas:

# Son ordenadas, mantienen el orden en el que han sido definidas
# Los elementos pueden ser formados por tipos arbitrarios
# Se pueden acceder a los elementos por medio de un índice.
# Se pueden anidar, es decir, meter una dentro de la otra.
# Son mutables, ya que sus elementos pueden ser modificados.
# Son dinámicas, ya que se pueden añadir o eliminar elementos.

vacia = []
vacia_dos = list()


# Creación de listas
numeros_lista = [2,3,4,5,6]
numeros_edades = [34, 45, 20, 19, 19, 54, 43, 26, 28]
vacia = []

# Crear una lista por medio de la función 'list'
vocales = list('aeiou')
print("Lista vocales =>", vocales)
numeros = list('1234')
print("Lista numeros =>", numeros)

print('-' * 80)

# ---------------- Agregar elementos a la lista --------------

# Agregar elementos por medio de la función 'append'
# La función 'append' agrega elementos al final de la lista
lista = []
lista.append(56)
lista.append(4)
lista.append(4)
lista.append(4)
lista.append(19)
lista.append("Xoan")

print("(append) Valor de lista =>", lista)

lista_diferente = [False, 7.8, 6.7-7.0J, "Mar", [4, 5], 67, None]
lista_1 = [2,3,4]
lista_2 = [-3,5,8,9]
lista_3 = lista_1
listas1 = lista_1 + lista_2
print("(concatenar) listas1 =>", listas1)
listas2 = lista_2 + lista_1
print("(concatenar) listas2 =>", listas2)

print('-' * 80)

# Agregar elementos por medio de la función 'extend'
# La función 'extend' agrega elementos al final de la lista
lista.extend([12, 34])
print("(extend) Valor de lista =>", lista)

numeros_lista.extend(numeros_edades)
print("(extend) Valor de numeros_lista =>", numeros_lista)

print('-' * 80)

# Agregar elementos por medio de la función 'insert'
# La función 'insert' agrega un elemento dentro de la lista
# en una posición indicada

print(lista)
# Número de la posición en positivo
lista.insert(0, 13)
print("(insert) Valor de lista =>", lista)

# Número de la posición en negativo
print("(insert) Valor de lista =>", lista)
lista.insert(-4, 133)
print("(insert) Valor de lista =>", lista)


# Cuando la posición (en positivo) es mayor que la longitud
# de la lista el elemento se inserta al final de la lista
lista.insert(12, 999)
print("(insert positivo) Valor de lista =>", lista)

# Cuando la posición (en negativo) es mayor que la longitud
# de la lista el elemento se inserta al principio de la lista
lista.insert(-20, 888)
print("(insert negativo) Valor de lista =>", lista)

print('-' * 80)

# Concatenar varias listas en una sola lista
nueva_lista = lista + numeros_lista + numeros_edades
print("(concatenar) Valor de nueva_lista =>", nueva_lista)

print('-' * 80)

# ---------------- Eliminar elementos de la lista --------------

# Eliminar un elemento por medio de la función 'pop'
# La función 'pop' elimina el último elemento de una lista
# y devuelve dicho elemento
print("(pop) Valores de la lista =>", lista)
ultimo = lista.pop()
print("(pop) Último elemento de la lista =>", ultimo)
print("(pop) Valores de la lista =>", lista)

print('-' * 80)


# La función 'pop(posición_del_elemento)' elimina el elemento
# en la posición indicada de la lista y devuelve el elemento
# Si la posición del elemento (positivo o negativo) sea mayor
# que el número de elementos de la lista, lanza una excepción

# Número de la posición en positivo
valor = lista.pop(1)
print("(pop positivo) Elemento de la lista =>", valor)
print("(pop positivo) Valores de la lista =>", lista)

# Número de la posición en negativo
valor = lista.pop(-1)
print("(pop negativo) Elemento de la lista =>", valor)
print("(pop negativo) Valores de la lista =>", lista)

print('-' * 80)

# Eliminar un elemento por medio de la función 'remove'
# La función remove elimina el primer elemento que encuentre
# de la lista, en caso de que haya elementos repetidos.
# En caso de que no encuentre el elemento lanza una excepción
print("(remove) Valores de la lista =>", lista)
lista.remove(4)
print("(remove) Valores de la lista =>", lista)

print('-' * 80)

# Eliminar todos los elementos de lista por medio de la
# función 'clear'
#lista.clear()
#print("(clear) Valores de la lista =>", lista)

print('-' * 80)

# ---------------- Obtener elementos de la lista --------------
# Obtener un elemento de la lista según su posición
# en positivo o negativo

print(lista)
# Número de la posición en positivo
elemento = lista[4]
print("(obtener) Elemento =>", elemento)


# Número de la posición en negativo
elemento = lista[-4]
print("(obtener) Elemento =>", elemento)

print('-' * 80)

# Obtener un rango de elementos dentro de una lista

# ----------- Rangos en positivo
print("(rango positivo) Valores =>", lista)
valores = lista[1:5]
print("(rango positivo) Valores =>", valores)

# Rangos de elementos desde una posición inicial hasta
# el final de la lista
valores = lista[2:]
print("(rango positivo) Valores =>", valores)

valores = lista[:8]
print("(rango positivo) Valores =>", valores)

# Rangos de elementos desde una posición inicial hasta
# el final de la lista por medio de saltos entre elementos
valores = lista[1:5:2]
print("(rango positivo saltos) Valores =>", valores)

# ----------- Rangos en negativo
valores = lista[-4:-1]
print("(rango negativo) Valores =>", valores)

# Rangos de elementos desde una posición final hasta
# el inicio de la lista
valores = lista[:-3]
print("(rango negativo) Valores =>", valores)

# Rangos de elementos desde una posición final hasta
# el inicio de la lista por medio de saltos entre elementos
valores = lista[:]
print("(rango negativo saltos) Valores =>", valores)

# Invertir una lista
print(lista)
valores = lista[::-1]
print("Lista invertida", valores)
print('-' * 80)

listan = [3, 4, 5, [5,4,[5,6,7,37,67], 56, 5]]

print(listan[3][2][3])

# ---------------- Misceláneo de funciones con listas --------------
'''
# Obtener la posición de un determinado elemento dentro de la lista
# Si no encuentra el elemento lanza una excepción
posicion = lista.index(13)
print("(posición elemento) Posición =>", posicion)

# Obtener la posición de un determinado elemento dentro de la lista
# a partir de una determinada posición inicial
# Si no encuentra el elemento lanza una excepción
posicion = lista.index(13,2)
print("(posición elemento) Posición =>", posicion)

# Obtener la posición de un determinado elemento dentro de la lista
# a partir de una determinada posición inicial hasta una posición final
# Si no encuentra el elemento lanza una excepción
posicion = lista.index(13, 2, 9)
print("(posición elemento) Posición =>", posicion)


print('-' * 80)

# Ordenar una lista de manera ascendente
orden = lista.sort()
print("(ordenar ascendente) Valores de la lista =>", lista)

# Ordenar una lista de manera descendente
orden = lista.sort(reverse=True)
print("(ordenar descendente) Valores de la lista =>", lista)

# Ordenar una lista en función de una determinada clave
# la clave debe de ser una función a aplicar en la ordenación
# Ordenar una lista en función del número de caracteres de cada elemento

lenguajes = ['go', 'python', 'java', 'julia', 'scala', 'c#', 'c++', 'R']
print("(ordenar por clave) Valores de la lista lenguajes =>", lenguajes)
lenguajes.sort(key=len)
print("(ordenar por clave) Valores de la lista lenguajes =>", lenguajes)

print('-' * 80)

# Contar el número de ocurrencias de un elemento dentro una lista
ocurrencias = lista.count(4)
print(lista)
print("(contar) Número de ocurrencias =>", ocurrencias)

print('-' * 80)

# Copiar una lista modificando la lista original
antigua = [1, 2, 3]
nueva = antigua

expandir = nueva
expandir.extend([45, 99])
nueva.append('a')
antigua.append('x')
print('(copiar) Lista nueva:', nueva)
print('(copiar) List antigua:', antigua)
print('(copiar) List expandir:', expandir)

# Copiar una lista sin modificar la lista original
antigua = [1, 2, 3]
nueva = antigua.copy()
nueva.append('a')
print('(copiar sin modificar) Lista nueva:', nueva)
print('(copiar sin modificar) List antigua:', antigua)

print('-' * 80)

# Devolver una lista con los elementos invertidos por medio de
# la función 'reverse'
numeros = [1, 2, 3, 4, 5]
numeros.reverse()
print("(reverse) Valores de la lista =>", numeros)

# Devolver una lista con los elementos invertidos por medio de
# rango de posiciones de elementos
numeros = [1, 2, 3, 4, 5]
print("(reverse) Valores de la lista =>", numeros[::-1])

# Comprobar si un determinado elemento está dentro de una lista
numeros = [1, 2, 3, 4, 5]
existe = 3 in numeros
print('Existe =>', existe)

'''