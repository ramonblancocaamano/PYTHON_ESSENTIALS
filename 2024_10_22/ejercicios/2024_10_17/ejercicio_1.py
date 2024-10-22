'''
Realizar un programa que solicite por teclado un texto y, en base al texto introducido mostrar en pantalla una colección de tipo diccionario con todas las
palabras únicas (independientemente mayúsculas o minúsculas) del texto introducido con sus correspondientes números de apariciones.

Ejemplo:

Si por teclado se introduce el siguiente texto: 'Esto es un nuevo comentario de texto y un nuevo texto'

Se muestra en pantalla: {'esto':1, 'es':1, 'un':2, 'nuevo':2, 'comentario':1, 'de':1, 'y':1, 'texto':2}
'''

texto = input('Texto a introducir: ')
palabras = {unique : texto.lower().count(unique) for unique in set(texto.lower().strip().split())}
print(palabras)
