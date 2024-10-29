'''
Realizar un programa que solicite 7 números por teclado y,
calcular cuántos números introducidos son divisibles entre 2, 3 ó 7
Y mostrar en pantalla los resultados
'''
divisible_2 = 0
divisible_3 = 0
divisible_7 = 0

for n in range(7):
    numero = int(input('Número: '))
    if numero % 2 == 0:
        divisible_2 += 1
    if numero % 3 == 0:
        divisible_3 += 1
    if numero % 7 == 0:
        divisible_7 += 1

print("Números divisibles entre 2 =>", divisible_2)
print("Números divisibles entre 3 =>", divisible_3)
print("Números divisibles entre 7 =>", divisible_7)

