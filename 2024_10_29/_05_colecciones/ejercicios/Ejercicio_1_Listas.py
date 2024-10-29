'''
Realizar un programa que solicite números por teclado hasta introducir el valor '0', visualizar
en pantalla una lista con todos los números pares y una lista con todos los números impares introducidos
'''

numeros_pares = []
numeros_impares = []
numero = -1
while numero != 0:
    numero = int(input('Numero: '))
    if numero != 0:
        if numero % 2 == 0:
            numeros_pares.append(numero)
        else:
            numeros_impares.append(numero)

print(numeros_pares)
print(numeros_impares)

