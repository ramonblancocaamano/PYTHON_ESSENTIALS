# Realizar un programa que solicite por teclado diez números y
# calcule cuantos números introducidos son mayores de cinco
# y mostrar el resultado

# valor if condición else valor

mayores_5 = 0
numeros = 10
while numeros > 0:
    valor = int(input('Número: '))
    if valor > 5:
        mayores_5 += 1
    numeros -= 1

print('mayores de 5 =>', mayores_5)

