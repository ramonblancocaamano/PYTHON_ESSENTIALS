# ------------------------------------------------------------------------------------------
# Ejemplos de conjuntos en Python

# Algunas propiedades de los conjuntos:
# Los elementos de un set son únicos, lo que significa que no puede haber
# elementos duplicados.
# Los set no son indexados, es decir, no se puede acceder a los elementos del
# set por medio de un índice
# Los set son desordenados, lo que significa que no mantienen el orden de
# cuando son declarados.
# Sus elementos son inmutables.
# ------------------------------------------------------------------------------------------

# No se puede acceder a elementos del set por medio de un índice
#print(s[0])

# Crear conjuntos utilizando la función 'set'
s = set([5, 4, 6, 8, 8, 1])
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

# Crear conjuntos utilizando las llaves '{' y '}'
s = {5, 4, 6, 8, (4,5), 8, 1, (2,3,3,3)}
s.add(67)
print(s)       #{1, 4, 5, 6, 8}
print(type(s)) #<class 'set'>

print('-' * 80)

# Operaciones con sets

# A diferencia de las listas, en los set no podemos modificar un elemento a través de su índice.
s = set([15, 6, 6, 57, 8])
s = {4, 6, (8,9), 7,8}
#s[0] = 3 #Error! TypeError

print('Conjunto datos =>', s)

# Los elementos de un set deben ser inmutables, por lo que un elemento
# de un set no puede ser ni un diccionario ni una lista.
s = set([5, 6, 7, 8, 7, 7])
print(s)
lista = ["Perú", "Argentina"]
#s = set(["México", "Bolivia", lista]) #Error! TypeError

print('-' * 80)

# Los sets se pueden iterar de la misma forma que las listas
s = set([5, 6, 7, 8])
for ss in s:
    print(ss) #8, 5, 6, 7

print('-' * 80)

# Operaciones y funciones con conjuntos
c1 = {1, 2, 3, 4, 5, 6}
c2 = {2, 4, 6, 8, 10}
c3 = {1, 2, 3}
c4 = {4, 5, 6}


# Unión de varios conjuntos
rdo = c1 | c2 | c3
print("Unión =>", rdo)

rdo = c1.union(c2).union(c3)
print("Unión =>", rdo)

print('-' * 80)

# Intersección de varios conjuntos
rdo = c1 & c2 & c3
print("Intersección =>", rdo)

rdo = c1.intersection(c2).intersection(c3)
print("Intersección =>", rdo)

print('-' * 80)

# Diferencia de dos conjuntos A y B, A – B, es el conjunto de elementos
# que están en A pero no en B.
rdo = c2 - c1
print("Diferencia =>", rdo)

rdo = c1.difference(c2)
print("Diferencia =>", rdo)

print('-' * 80)

# Unión exclusiva, también conocida como diferencia simétrica, es el
# conjunto de elementos que están en A o B, pero no en ambos
rdo = c1 ^ c2
print("Unión exclusiva =>", rdo)

rdo = c1.symmetric_difference(c2)
print("Unión exclusiva =>", rdo)

print('-' * 80)

'''r5 = c1 + c2
print("Suma sets", r5)
print('-' * 80)'''

# Funciones con sets

# La función add() permite añadir un elemento al set.
s = {1,2,3,4}
s.add(7)
print("add =>", s)

print('-' * 80)

# La función remove() elimina el elemento que se pasa como parámetro.
s = {1,2,3,4}
s.remove(3)
print("remove =>", s)

print('-' * 80)

# La función discard() es muy parecido al remove(), borra el elemento
# que se pasa como parámetro, y si no se encuentra no hace nada.
s = {1,2,3,4}
s.discard(13)
print("discard =>", s)

print('-' * 80)

# La función pop() elimina un elemento aleatorio del set.
s = {1,2,3,4}
s.pop()
print("pop =>", s)

print('-' * 80)

# La función clear() elimina todos los elementos de set.
s = {1,2,3,4}
s.clear()
print("clear =>", s)

print('-' * 80)

# Comprobar si un elemento está dentro de un conjunto
s = {1,2,3,4}
existe = 21 in s
print("Existe =>", existe)

lista = [1,1,1,1,1,2,33,3,3,3,3,3,3,3,4]
x = set(lista)
print(x)
lista = list(x)
print(lista)
print(type(lista))
