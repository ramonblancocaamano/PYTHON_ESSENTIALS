'''
Dado el siguiente código Python:
valores = [6, [7, 9], False, 'funcion', 7.32, 6.6-8.7j]

Mostrar en pantalla si todos los elementos de la lista 'valores' son del mismo tipo.
'''

valores = [6, [7, 9], False, 'funcion', 7.32, 6.6-8.7j]
#valores = [6,8,7,6,6]
iguales = True
for element in valores[1:]:
    if type(element) != type(valores[0]):
        iguales = False
        break
print(iguales)
