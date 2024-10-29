# ------------------------------------------------------------------------------------------
# Ejemplo de for comprehension para crear colecciones de tipo generador
# ------------------------------------------------------------------------------------------

impares = (number for number in range(1, 100, 2))
for number in impares:
    print('Número:', number)

print('=' * 80)

frase = "Esta frase se utiliza en un generador"
letras = (letra for letra in frase)

for caracter in letras:
    print(caracter)

#next(letras)

print('-' * 80)

import random
random_numbers = lambda x: (random.randint(0, 100) * 1.1 for _ in range(x))

for _ in random_numbers(20):
    print(_)
