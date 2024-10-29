# Realizar un programa que solicite por teclado un número (mientras
# el número introducido sea distinto de cero) y, calcule el número
# total de números pares e impares y, la suma total de todos los números
# pares y la suma total de todos los números impares.
# Mostrar en pantalla el número total de números pares e impares y,
# mostrar en pantalla la suma total de todos los números pares e impares

numero = -1
total_pares = 0
total_impares = 0
suma_pares = 0
suma_impares = 0
while numero != 0:
    numero = int(input('Número: '))
    if numero == 23:
        break
    if numero % 2 == 0:
        total_pares += 1
        suma_pares += numero
    else:
        total_impares += 1
        suma_impares += numero
else:
    print('Gracias por los valores introducidos')

print(total_pares)
print(total_impares)
print(suma_pares)
print(suma_impares)
