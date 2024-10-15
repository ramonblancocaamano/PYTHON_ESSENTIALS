'''
Realizar un programa que solicite números por teclado hasta introducir el valor '0', visualizar
en pantalla una lista con todos los números pares y una lista con todos los números impares introducidos
'''
lista_pares = []
lista_impares = []
numero = 9
while numero != 0:
    numero = int(input("Valor: "))
    if numero == 0:
        continue # break
    elif numero % 2 == 0:
        lista_pares.append(numero)
    else:
        lista_impares.append(numero)

print(lista_pares)
print(lista_impares)