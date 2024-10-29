# ------------------------------------------------------------------------------------------
# Programación funcional en Python: Función 'map'
# ------------------------------------------------------------------------------------------

lenguajes = ['python', 'java', 'go', 'javascript']

mayus = [p.upper() for p in lenguajes]

def length(word):
    return len(word)

print(mayus)

print('=' * 80)

lenguajes = ['python', 'java', 'go', 'javascript']

mayus = [l.upper() for l in lenguajes]

map_lenguajes = list(map(lambda k: k.upper(), lenguajes))
print(map_lenguajes)

rangos = range(100)
print(list(rangos))

map_length = map(length, lenguajes)
print(map_length)

dobles = map(lambda v: v * 2, range(1,100))
print(list(dobles))

