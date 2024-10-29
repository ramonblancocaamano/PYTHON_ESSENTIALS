'''
   Realizar un programa que solicite un número por teclado y, calcule y muestre el factorial del número introducido.

    Cálculo factorial de un número:
    factorial de 5 = 5 * 4 * 3 * 2 * 1
    factorial de 9 = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
'''

factorial = 1
numero = int(input('Número: '))
for n in range(1, numero + 1):
    factorial *= n
print('factorial =>', factorial)
