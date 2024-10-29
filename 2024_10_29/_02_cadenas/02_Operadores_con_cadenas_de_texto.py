# ------------------------------------------------------------------------------------------
# Tipos de operadores aritméticos utilizados con cadenas de texto
# ------------------------------------------------------------------------------------------

# Para concatenar una cadena con otra utilizamos el operador +, las cadenas
# se pueden concatenar con otro tipo de variables como por ejemplo variables
# numéricas (enteras, reales y complejas), booleanas, etc.

# Concatenar una cadena con otra cadena
nombre = 'Xoan'
apellido = 'Gallego'
nome = nombre + ' ' + apellido
print(nome)

# Concatenar una cadena con una variable numérica
nombre = "Ana Manuela"
edad = 28
datos = "Nombre: " + nombre + ", Edad: " + str(edad)
print(datos)

# Concatenar una cadena con una variable booleana
nombre = "Ana Manuela"
mayor = True
datos = "Nombre: " + nombre + ", Mayor: " + str(mayor)
print(datos)

print('<>' * 80)

# Replicar o repetir una cadena con el operador '*'
palabra = 'Python '
print(palabra * 3)
