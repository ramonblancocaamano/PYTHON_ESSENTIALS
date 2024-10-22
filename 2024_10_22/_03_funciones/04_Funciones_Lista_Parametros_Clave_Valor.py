# ------------------------------------------------------------------------------------------
# Funciones con argumentos o parámetros en formato de clave y valor
# Usando doble ** es posible también tener como parámetro de entrada
# una lista de elementos almacenados en forma de clave y valor.
# ------------------------------------------------------------------------------------------

diccionario = {'f':3, 'h':9}

def suma_valores(*parms1, **params2):
    print(type(parms1))
    suma = sum(parms1)
    for _, value in params2.items():
        suma += value
    return suma

rdo99 = suma_valores(**diccionario)
#print(rdo99)

rdo0 = suma_valores()
rdo1 = suma_valores(10, 20)
rdo2 = suma_valores(v=5, h=5, m=20)
rdo3 = suma_valores(a=10, b=20, c=40, d=50, b4=90)

rdo4 = suma_valores(1, 2, 3, 4, v=6, h=8, m=9)
rdo5 = suma_valores(1, 2, 3, 4)
print("suma_valores -> rdo4 =>", rdo4) # 33
print("suma_valores -> rdo5 =>", rdo5) # 10
print("suma_valores -> rdo0 =>", rdo0)
print("suma_valores -> rdo1 =>", rdo1)
print("suma_valores -> rdo2 =>", rdo2)
print("suma_valores -> rdo3 =>", rdo3)

print('-' * 80)

# ------------------------------------------------------------------------------------------
# Las funciones con parámetros de clave/valor también se pueden
# combinar con parámetros por posición
# ------------------------------------------------------------------------------------------

def suma_multi_por_valor(valor, **kwargs):
    suma = 0
    for key, value in kwargs.items():
        suma += value * valor
    return suma


rdo1 = suma_multi_por_valor(10, a=1, b=1)
print("suma_multi_por_valor -> rdo1 =>", rdo1)

print('-' * 80)

# ------------------------------------------------------------------------------------------
# A una función con parámetros clave/valor le podemos pasar un diccionario
# como parámetro de entrada.
# Nota: El ** se utiliza para descomponer un diccionario en parámetros
# de clave/valor
# ------------------------------------------------------------------------------------------

diccionario = {'a': 10, 'b': 20}
rdo1 = suma_valores(**diccionario)
print("suma_valores -> rdo1 =>", rdo1)

print('-' * 80)

# ------------------------------------------------------------------------------------------
# Función con argumentos o parámetros de longitud variable y argumentos o
# parámetros en formato de clave y valor
# ------------------------------------------------------------------------------------------

def procesar(*args, **kwargs):
    suma = 0
    for x in args:
        suma += x
    for key, value in kwargs.items():
        suma += value
    return suma


rdo1 = procesar(1, 2, 4, 5, c=9, d=8, g=20)
print("procesar -> rdo1 =>", rdo1)

# De igual manera, podemos pasar una lista y un diccionario como
# parámetro de entrada.
lista = [1, 3, 5, 4]
conjunto = {1, 2, 3, 4}
tupla = (2, 3, 4)
diccionario = {'a': 10, 'b': 20}
rdo1 = procesar(*lista, **diccionario)
rdo2 = procesar(*conjunto, **diccionario)
rdo3 = procesar(*tupla, **diccionario)
print("procesar -> rdo1 =>", rdo1)
print("procesar -> rdo2 =>", rdo2)
print("procesar -> rdo3 =>", rdo3)

print('-' * 80)

# Con distintos tipos de parámetros
def suma_todo(w, y=1, *args, **kwargs):
    suma = 0
    suma += w
    suma += y
    for x in args:
        suma += x
    for key, value in kwargs.items():
        suma += value
    return suma

lista = [10, 30, 50, 40]
conjunto = {11, 22, 33, 44}
tupla = (20, 30, 40)
diccionario = {'a': 10, 'b': 20}

rdo1 = suma_todo(2, 20, 10, 10, k=10, l=30)
rdo2 = suma_todo(2, 10, 10, k=10, l=30)
rdo3 = suma_todo(2, 20, 10, 10, k=10, l=30)
rdo4 = suma_todo(2, *lista, **diccionario)
rdo5 = suma_todo(2, *conjunto, **diccionario)
rdo6 = suma_todo(2, *tupla, **diccionario)
print("suma_todo -> rdo1 =>", rdo1)
print("suma_todo -> rdo2 =>", rdo2)
print("suma_todo -> rdo3 =>", rdo3)
print("suma_todo -> rdo4 =>", rdo4)
print("suma_todo -> rdo5 =>", rdo5)
