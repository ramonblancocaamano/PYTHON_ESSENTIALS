# Solicitar por teclado una frase y un número que indique el número de veces
# a visualizar en pantalla la frase introducida

frase = input('Frase: ')
veces = int(input('Número de veces: '))

while veces > 0:
    print(frase)
    veces -= 1

