lista = [2, 3]
conj = {5, 6}
tupla = (8, 9)

def suma(*valores):
    suma = 0
    for n in valores:
        suma += n
    return suma

s = suma(*lista) # suma(2, 3)
print(s)

s = suma(*conj) # suma(5, 6)
print(s)

s = suma(*tupla) # suma(8, 9)
print(s)
