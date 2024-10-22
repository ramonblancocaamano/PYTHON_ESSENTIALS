# ------------------------------------------------------------------------------------------
# Tipos de operadores lógicos
# ------------------------------------------------------------------------------------------

# Operador lógico       Descripción
# ------------------------------------------------------------------------------------------
#       or              Devuelve True si alguno de los operandos es True
#       and             Devuelve True si ambos operandos son True
#       not             Devuelve la negación de los operandos

# ------------------------------------------------------------------------------------------
# Tabla de verdad del operador or
# ------------------------------------------------------------------------------------------
# Condicion_1       Condicion_2     Resultado
#       F               F               F
#       F               V               V
#       V               F               V
#       V               V               v

# Utilizando el operador OR

bool3 = 5 == 6 or 6 != 6 or 7 != 8
print("bool3=", bool3)

# ------------------------------------------------------------------------------------------
# Tabla de verdad del operador and
# ------------------------------------------------------------------------------------------
# Condicion_1       Condicion_2     Resultado
#       F               F               F
#       F               V               F
#       V               F               F
#       V               V               V

bool4 = 5 <= 6 and 6 == 6 and 7 < 8
print("bool4=", bool4)

bool5 = (5 <= 6 or 6 < 9) and 8 > 10
print("bool5=", bool5)

print("not =>", not 5 <= 6)
print("not =>", not False)
