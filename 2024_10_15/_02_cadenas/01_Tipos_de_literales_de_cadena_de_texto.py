# ------------------------------------------------------------------------------------------
# Las cadenas en Python o strings son un tipo inmutable que permite almacenar
# secuencias de caracteres.
# En Python se consideran espacios en blanco los siguiente caracteres:
# - El espacio en blanco, la tabulación, el salto de línea y el retorno de carro
# ------------------------------------------------------------------------------------------

# Ejemplos de cadenas en Python

# Utilizando las doble comillas
nombre = "Xoan"
print(nombre)

# Utilizando las comillas simples
nombre = 'Xoan'
print(nombre)

# Una situación que muchas veces se puede dar, es cuando queremos introducir
# una comilla, bien sea simple ' o doble " dentro de una cadena.
#frase = "Esta frase utiliza "comillas" dobles internas"

# Secuencias de escape
# Secuencia         Representa
# ----------         ----------
# \t                Tabulación
# \n                Nueva línea
# \'                Comilla simple
# \"                Comilla doble
# \\                Barra invertida
# \u                Carácter unicode (con 4 dígitos hexadecimales)
# \U                Carácter unicode (con 8 dígitos hexadecimales)

frase = "hola\t\t\thola"

# Ejemplos de secuencias de escape
frase1 = "Esta frase utiliza \"comillas\" dobles internas"
frase2 = 'Esta frase utiliza \'comillas\' dobles internas'
frase2b = 'Esta frase utiliza "comillas" dobles internas'
frase3 = 'Esta frase \t\t\tcontiene un tabulador interno'
frase4 = "La frase tiene un salto de \nlínea interno"
carpeta = 'c:\\temp\muestra\\'
frase5 = "\u00A9 Derechos de autor"
frase6 = "\U0001F604 Cara Sonriente"
print(frase1)
print(frase2)
print(frase3)
print(frase4)
print(carpeta)
print(frase5)
print(frase6)

print('-' * 80)

# Caracteres de Escape Raw (r) o (R)
# Si queremos que los caracteres de escape no sean interpretados en una
# cadena, puedemos utilizar el prefijo 'r' para crear una cadena de escape cruda.
directorio = R"C:\Directorio\Archivo"
print(directorio)
