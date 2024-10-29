# Realizar un programa que solicite números por teclado hasta introducir el '0',
# y guarde todos los números introducidos en una lista
'''
Y, crear dos listas de números y, realizar la suma de las dos listas y mostrar en pantalla la nueva lista con las sumas
Ejemplo:
 primera = [1, 2, 3, 3]
 segunda = [4, 5, 6]

 suma = [5, 7, 9]
'''

primera_lista = []
segunda_lista = []
suma_listas = []

# Pedir datos de la primera lista
numero = 9
while numero != 0:
    numero = int(input('Número: '))
    if numero != 0:
        primera_lista.append(numero)

# Pedir datos de la segunda lista
numero = -1
while numero != 0:
    numero = int(input('Número: '))
    if numero != 0:
        segunda_lista.append(numero)

# Realizar la suma de las dos listas
elementos_primera = len(primera_lista)
elementos_segunda = len(segunda_lista)
elementos = elementos_primera if elementos_primera < elementos_segunda else elementos_segunda
for x in range(elementos): # 0, 1, .....
    suma = primera_lista[x] + segunda_lista[x]
    suma_listas.append(suma)

print(suma_listas)
