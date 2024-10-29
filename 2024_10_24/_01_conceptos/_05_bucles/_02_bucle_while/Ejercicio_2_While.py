# Realizar un programa que un número por teclado y calcule
# el sumatorio del número introducido y el resultado se muestre
# por pantalla

sumatorio = 0
numero = int(input('Número: ')) # 1+2+3+4+5=15
while numero > 0:
    sumatorio += numero
    numero -= 1

print('sumatorio =>', sumatorio)
