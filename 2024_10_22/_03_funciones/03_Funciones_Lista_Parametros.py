# ------------------------------------------------------------------------------------------
# Funciones con lista de argumentos o parámetros de longitud variable
# ------------------------------------------------------------------------------------------

def sumatorio(*numeros):
    print(type(numeros))
    total = 0
    for n in numeros:
        total += n
    return total

rdo1 = sumatorio()
rdo2 = sumatorio(3)
rdo3 = sumatorio(5, 6)
rdo4 = sumatorio(5, 5, 5, 5, 5)
rdo5 = sumatorio(5, 5, 5, 5, 5,5,5,6,6,6,7,7,7,78,78,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,77,8)
print("sumatorio -> rdo1 =>", rdo1)
print("sumatorio -> rdo2 =>", rdo2)
print("sumatorio -> rdo3 =>", rdo3)
print("sumatorio -> rdo4 =>", rdo4)
print("sumatorio -> rdo5 =>", rdo5)

print('-' * 80)

# ------------------------------------------------------------------------------------------
# Los parámetros de longitud variable se pueden combinar con parámetros por posición
# ------------------------------------------------------------------------------------------

def mostrar(veces, *palabras):
    for p in palabras:
            print("mostrar =>", p.upper() * veces)

mostrar(3, 'primera', 'segunda')

print('-' * 80)

# ------------------------------------------------------------------------------------------
# A una función con parámetros de longitud variable se le puede enviar
# también una lista, un conjunto, una tupla
# ------------------------------------------------------------------------------------------

lista = [1, 3, 5, 4]
conjunto = {4,8,6}
tupla = (5,5,5,5,5)

# ------------------------------------------------------------------------------------------
# Nota: El asterisco se utiliza para descomponer una lista, un conjunto o
# una tupla en una lista de parámetros
# ------------------------------------------------------------------------------------------

rdo1 = sumatorio(*lista)
rdo2 = sumatorio(*conjunto)
rdo3 = sumatorio(*tupla)
print("Sumatorio lista =>", rdo1)
print("Sumatorio conjunto =>", rdo2)
print("Sumatorio tupla =>", rdo3)

print('-' * 80)
