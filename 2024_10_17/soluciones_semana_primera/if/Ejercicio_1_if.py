'''
Realizar un programa que solicite tres números por teclado y, muestre por pantalla cuál es el mayor de los tres números,
cuál es el menor de los tres números o si los números son todos iguales.
'''

numero_1 = int(input('Primer número: '))
numero_2 = int(input('Segundo número: '))
numero_3 = int(input('Tercer número: '))

numero_mayor = numero_1
numero_menor = numero_1

if numero_1 > numero_2:
    numero_mayor = numero_1 if numero_1 > numero_3 else numero_3
else:
    numero_mayor = numero_2 if numero_2 > numero_3 else numero_3
if numero_1 < numero_3:
    numero_menor = numero_1 if numero_1 < numero_2 else numero_2
else:
    numero_menor = numero_2 if numero_2 < numero_3 else numero_3

if numero_mayor == numero_menor:
    print("son todos iguales")
else:
    print("mayor", numero_mayor)
    print("menor", numero_menor)
