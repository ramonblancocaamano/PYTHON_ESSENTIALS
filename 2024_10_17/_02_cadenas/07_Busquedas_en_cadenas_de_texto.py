# ------------------------------------------------------------------------------------------
# Búsquedas en cadenas de texto
# ------------------------------------------------------------------------------------------

# Comprobar si una determinada cadena está dentro de otra cadena
buscar = 'Py'
existe = buscar in 'Programación en Python'
print(existe)

# Buscar la posición de una cadena dentro de otra cadena con 'find'
# Esta función 'find' devuelve -1 si no encuentra la ocurrencia
frase = 'frase para utilizar en la búsqueda para texto'
print("find=>", frase.find('xara'))


# Comprobar si el caracter 'I' está entre la posición 6 y 10
frase = 'Hoy es miercoles'
posi = frase.find('i', 6, 10)
print(posi)


# Buscar la posición de una cadena dentro de otra cadena con 'index'
# Esta función 'index' lanza una excepción si no encuentra la ocurrencia
frase = 'frase para utilizar en la búsqueda'
print("index=>", frase.index('para'))

# Cuenta el número de ocurrencias de un texto dentro de una cadena de texto
#texto = "Cuenta el número de ocurrencias de un texto dentro de una cadena de texto"
#palabra = input('Texto a buscar: ')
texto = 'Hola'
ocurrencias = texto.count('')
print("ocurrencias=>", ocurrencias)
print(len(texto))

