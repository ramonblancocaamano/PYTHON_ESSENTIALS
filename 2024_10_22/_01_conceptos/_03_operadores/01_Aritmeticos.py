# ------------------------------------------------------------------------------------------
# Tipos de operadores aritméticos numéricos
# ------------------------------------------------------------------------------------------

# Operador aritmético   Operación aritmética
# ------------------------------------------------------------------------------------------
#       **              Exponente o elavar a
#       *               Multiplicación
#       /               División
#       //              División entera
#       %               Módulo o resto
#       +               Suma
#       -               Resta

base8 = 2 ** 8 # Operación elevar a (256)
entero = 3 // 2 # Operación división entera (1)
print(entero)

formula = 4 ** 2 / (5 + (4 - 5 + 7 * 3)) ** 2 * 2 - 7
print(formula)

# ------------------------------------------------------------------------------------------
# Tipos de operadores aritméticos cadenas de texto
# ------------------------------------------------------------------------------------------

# Operador aritmético   Operación aritmética
# ------------------------------------------------------------------------------------------
#       +               Concatena dos o más cadenas de texto
#       *               Replica una cadena de texto un número determinado de veces

palabra_1 = 'Hola '
palabra_2 = "caracola."
frase = palabra_1 + palabra_2 # Concatena dos cadenas de texto
print(frase)

palabra = "Python "
palabras = palabra * 61 # Replica la palabra 'Python ' seis veces
print(palabras)
