'''
    Realizar un programa que muestre los primeros 10 números de la sucesión de Fibonacci. La sucesión comienza con los números 0 y 1 y,
    a partir de éstos, cada elemento es la suma de los dos números anteriores, secuencia Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55 ...
'''

primero = 0
segundo = 1
for n in range(8):
     numero = primero + segundo
     print(numero)
     primero = segundo
     segundo = numero

