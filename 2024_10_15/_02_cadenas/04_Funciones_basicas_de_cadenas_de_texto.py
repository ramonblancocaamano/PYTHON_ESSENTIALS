# ------------------------------------------------------------------------------------------
# Funciones principales de las cadenas de texto, todas las cadenas de texto
# derivan de la clase 'str' que proporciona una serie de métodos (funciones)
# para utilizar con las cadenas de texto, como por ejemplo, hacer
# una búsqueda dentro de una cadena de texto, reemplazar un determinado
# texto, etc.
# ------------------------------------------------------------------------------------------

# Funciones de cadenas
frase = "cadena de texto en Python"

# Devuelve el número de caracteres que hay dentro de una cadena de texto
numero_de_caracteres = len(frase)
print(numero_de_caracteres)

# Convertir una cadena a mayúsculas
print(frase.upper())

# Convertir una cadena a minúsculas
print(frase.lower())

# Capitalizar una cadena de texto
print(frase.capitalize())

# Comprueba si empieza por una determinada cadena de texto
print(frase.startswith('cad'))

# Comprueba si finaliza por una determinada cadena de texto
print(frase.endswith('python'))

# Comprueba si todos los caracteres de una cadena son alfanuméricos
email = 'correo@dominio.com'
print(email.isalnum())

# Comprueba si todos los caracteres de una cadena son alfabéticos
nombre = 'Xoan'
print(nombre.isalpha())

# Comprueba si todos los caracteres de una cadena son dígitos numéricos
edad = '273'
print(edad.isnumeric())
