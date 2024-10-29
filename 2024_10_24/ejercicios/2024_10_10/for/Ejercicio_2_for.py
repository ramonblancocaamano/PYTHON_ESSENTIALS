'''
   Realizar un programa que solicite un número por teclado y muestre en pantalla la tabla de multiplicar del 1 al 10 del número introducido.

    Ejemplo de salida en pantalla:

    Número: 7

    7 x 1 = 7
    7 x 2 = 14
      .
      .
    7 x 10 = 70
'''

numero = int(input('Número: '))
for n in range(1, 11):
    print(numero, '*', n, '=', numero * n)

