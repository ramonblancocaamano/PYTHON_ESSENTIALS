'''
    Realizar un programa que solicite un número por teclado y muestre en pantalla todos los números (entre 1 y 1000) que sean divisibles entre
    el número introducido por teclado.
'''

numero = int(input('Número: '))
divisibles = 0
for n in range(1, 1001):
    if n % 2 == 0:
        divisibles += 1
print('Numeros divisibles', divisibles)
