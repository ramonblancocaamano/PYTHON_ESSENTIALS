'''
    Realizar un programa que solicite un número entero por teclado y, calcule la siguiente fórmula matemática:

    formula = 1 + 1/2 + 1/3 + 1/4 + ... + 1/numero

    Mostrar el resultado de la fórmula en pantalla.
'''

formula = 1
numero = int(input('Número: '))
while numero > 1:
    formula += (1 / numero)
    numero -= 1

print("resultado =>", formula)
