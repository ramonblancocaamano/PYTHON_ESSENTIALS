'''
Realizar un programa que solicite un número entero por teclado y, calcule el número mayor por el cual es divisible el número introducido.
'''

numero = int(input('Número: '))
dividir = 2
mayor_divisor = 1
while dividir < numero:
    if numero % dividir == 0:
        mayor_divisor = dividir
    dividir += 1

print("mayor divisor =>", mayor_divisor)
