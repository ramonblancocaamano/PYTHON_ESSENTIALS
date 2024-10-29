'''
    Realizar un programa que solicite tres números por teclado y los muestre en pantalla de menor a mayor.
'''

numero_1 = int(input('Primer número: '))
numero_2 = int(input('Segundo número: '))
numero_3 = int(input('Tercer número: '))

if numero_1 < numero_2 and numero_1 < numero_3:
    if numero_2 < numero_3:
        print(numero_1)
        print(numero_2)
        print(numero_3)
    else:
        print(numero_1)
        print(numero_3)
        print(numero_2)
elif numero_2 < numero_1 and numero_2 < numero_3:
    if numero_1 < numero_3:
        print(numero_2)
        print(numero_1)
        print(numero_3)
    else:
        print(numero_2)
        print(numero_3)
        print(numero_1)
elif numero_3 < numero_1 and numero_3 < numero_2:
    if numero_1 < numero_2:
        print(numero_3)
        print(numero_1)
        print(numero_2)
    else:
        print(numero_3)
        print(numero_2)
        print(numero_1)
