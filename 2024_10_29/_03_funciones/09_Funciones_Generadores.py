# ------------------------------------------------------------------------------------------
# Funciones del tipo generador
# ------------------------------------------------------------------------------------------

def ciudades():
    yield 'Vigo'
    yield 'Barcelona'

def valores():
    for n in range(4):
        dic = {}
        dic['v'] = n
        yield dic

def numeros(numbers):
    for n in range(numbers):
        yield n

ciudades = ciudades()
vigo = next(ciudades)
barcelona = next(ciudades)
print(vigo)
print(barcelona)

print('-' * 80)

genera = valores()

print(next(genera))
print(next(genera))
print(next(genera))
print(next(genera))
#print(next(genera))

print('-' * 80)

for value in valores():
    print(value)

print('-' * 80)

for numero in numeros(10):
    print(numero)
