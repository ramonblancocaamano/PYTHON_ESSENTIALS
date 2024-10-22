# Solicitar valores numéricos enteros por teclado hasta introducir el valor 0 y, mostrar en
# pantalla todos los valores como una coleccion de tipo lista, utilizando las funciones
# definidas en el módulo 'Numbers' del paquete 'api'

import api.Numbers as n

valores = []
while True:
    numero = n.read_int()
    if numero == 0:
        break
    valores.append(numero)

print(valores)
