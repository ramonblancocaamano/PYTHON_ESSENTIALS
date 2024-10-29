# ------------------------------------------------------------------------------------------
# Tipos de operadores a nivel de bit
# ------------------------------------------------------------------------------------------

# Operador a nivel de bit   Operación
# ------------------------------------------------------------------------------------------
#       |                   or
#       &                   and
#       ^                   xor
#       ~                   not
#       >>                  desplazamiento de bits a la derecha
#       <<                  desplazamiento de bits a la izquierda

# ------------------------------------------------------------------------------------------
# Operador or
# ------------------------------------------------------------------------------------------
n1 = 14
n2 = 9
r1 = n1 | n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# ------------------------------------------------------------------------------------------
# Operador and
# ------------------------------------------------------------------------------------------
n1 = 14
n2 = 9
r1 = n1 & n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# ------------------------------------------------------------------------------------------
# Operador xor
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
# Tabla de verdad del operador xor
# ------------------------------------------------------------------------------------------
# Condicion_1       Condicion_2     Resultado
#       F               F               F
#       F               V               V
#       V               F               V
#       V               V               F

n1 = 14
n2 = 9
r1 = n1 ^ n2
print(r1)
print(bin(n1))
print(bin(n2))
print(bin(r1))

print('-' * 70)

# ------------------------------------------------------------------------------------------
# Operador not
# ------------------------------------------------------------------------------------------
n1 = 255
r1 = ~n1
print(r1)
print(n1)
print(bin(r1))
r2 = ~r1
print(r2)
print(bin(r2))
print('-' * 70)

# ------------------------------------------------------------------------------------------
# Operador desplazamiento a la izquierda
# ------------------------------------------------------------------------------------------
n1 = 1
n2 = 3

r1 = n1 << n2  # Los bits de n1 se desplazan a la izquierda tantas posiciones
               # como indique la variable 'n2'
print(r1)
print(bin(n1))
print(bin(r1))

print('-' * 70)

# ------------------------------------------------------------------------------------------
# Operador desplazamiento a la derecha
# ------------------------------------------------------------------------------------------
n1 = 254
n2 = 4
r1 = n1 >> n2
print(r1)
print(bin(n1))
print(bin(r1))

potencia_base_2 = 1 << 3 # 2 elevado a 3
potencia_base_2 = 1 << 16 # 2 elevado a 16
potencia_base_2 = 1 << 33 # 2 elevado a 33

print('-' * 70)

n1 = 12
n2 = 2
r1 = n1 >> n2
print(r1)
print(bin(n1))
print(bin(r1))
