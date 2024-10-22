# ------------------------------------------------------------------------------------------
# Ejemplos de diccionarios en Python

# Un diccionario en Python es una colección de elementos, donde cada uno
# tiene una llave key y un valor value. Los diccionarios se pueden crear
# con paréntesis {} separando con una coma cada par key: value.

# Algunas propiedades de los diccionario en Python son las siguientes:

# Son dinámicos, pueden crecer o decrecer, se pueden añadir o
# eliminar elementos.
# Son indexados, los elementos del diccionario son accesibles a través
# del key.
# Y son anidados, un diccionario puede contener a otro diccionario en
# su campo value.
# ------------------------------------------------------------------------------------------

# Crear diccionarios
dicc = {
    "Nombre" : "Sara",
    "Edad" : 27,
    "Documento" : 1003.882,
    "Datos" : {
        "Ciudad": "Barna",
        'Números': [2,3,4,5,4,44,4]
    }
}
print(dicc)

# Crear un diccionario en Python usando dict() e introduciendo los
# pares key: value entre paréntesis.
dicc = dict(   [ ('Nombre', 'Sara'), ('Edad', 27), ('Documento', 1003.882) ]    )
print(dicc)


# También es posible usar el constructor dict() para crear un diccionario.
dicc = dict(Nombre='Sara', Edad=27, Documento=1003.882, Lista=[8,9,6])
print(dicc)

print('-' * 80)

# Acceder y modificar elementos

# Se puede acceder a sus elementos con [] o también con la función get()
print(dicc['Nombre'])     #Sara
print(dicc.get('Nombre')) #Sara


# Para modificar un elemento basta con usar [] con el nombre del key y
# asignar el valor que queremos.
print(dicc)
dicc['Nombre'] = "Laura"
print(dicc)

# Si el key al que accedemos no existe, se añade automáticamente.
dicc['Direccion'] = "Calle 123"
dicc['EDAD'] = 28
print(dicc)

print('-' * 80)

# Iterar diccionario
print(dicc.keys())

# Mostrar los key del diccionario
for clave in dicc:
    print("Clave =>", clave)

print('-' * 80)


# Mostrar los value del diccionario
for clave in dicc:
    print("Valor =>", dicc[clave])

# Mostrar el key y el value a la vez.
for x, y in dicc.items(): # [(k,v), (k,v), (k,v), (k,v)]
    print("Clave =>",x, ", Valor =>", y)

for clave in dicc.keys():
    print(clave)

for valor in dicc.values():
    print(valor)

print('-' * 80)



# Los diccionarios en Python pueden contener uno dentro de otro.
anidado1 = {"a": 1, "b": 2}
anidado2 = {"a": 1, "b": 2}
d = {
  "anidado1" : anidado1,
  "anidado2" : anidado2
}
print("Anidado =>", d)

print('-' * 80)

# Funciones en diccionarios Python

# La función clear() elimina todo el contenido del diccionario.
d = {'a': 1, 'b': 2}
d.clear()
print("Clear =>", d) #{}

print('-' * 80)

# La función get() nos permite consultar el value para un key determinado
d = {'a': 1, 'b': 2}
print("Get =>", d.get('a')) #1
print("Get =>", d.get('z')) #No encontrado

print('-' * 80)

# La función items() devuelve una lista con los keys y values del diccionario.
d = {'a': 1, 'b': 2}
it = d.items()
print("Items =>", it)             #dict_items([('a', 1), ('b', 2)])
print("Items =>", list(it))       #[('a', 1), ('b', 2)]
print("Items =>", list(it)[0][0]) #a

print('-' * 80)

# La función keys() devuelve una lista con todas las keys del diccionario.
d = {'a': 1, 'b': 2}
k = d.keys()
print("Keys =>", k)       #dict_keys(['a', 'b'])
print("Keys =>", list(k)) #['a', 'b']

print('-' * 80)

# La función values() devuelve una lista con todos los values o valores
# del diccionario.
d = {'a': 1, 'b': 2}
print("Values =>", list(d.values())) #[1, 2]

print('-' * 80)

# La función pop() busca y elimina la key que se pasa como parámetro y
# devuelve su valor asociado.
d = {'a': 1, 'b': 2}
d.pop('a')
print("Pop =>", d) #{'b': 2}

# También se puede pasar un segundo parámetro que es el valor a devolver
# si la key no se ha encontrado.
d = {'a': 1, 'b': 2}
d.pop('c', -1)
print("Pop =>", d) #{'a': 1, 'b': 2}

print('-' * 80)

# La función update() se llama sobre un diccionario y tiene como entrada
# otro diccionario. Los value son actualizados y si alguna key del nuevo
# diccionario no esta, es añadida.
d1 = {'a': 1, 'b': [1,2,2,3,3,3], 'nom': 'Ana'}
d2 = {'a': 0, 'd': 400, 'e': False}
d2.update(d1)
print("Update", d2)

d2['D'] = 500
print(d2)
