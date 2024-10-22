# ------------------------------------------------------------------------------------------
# Tipos de operadores de asignación
# ------------------------------------------------------------------------------------------

# Operador de asignación    Equivale a                  Descripción
# ------------------------------------------------------------------------------------------
#       **=                 x = x ** n                  Exponente o elavar a
#       *=                  x = x * n                   Multiplicación
#       /=                  x = x / n                   División
#       //=                 x = x // n                  División entera
#       %=                  x = x % n                   Módulo o resto
#       +=                  x = x + n                   Suma
#       -=                  x = x - n                   Resta
#       &=                  x = x & n                   Operación and a nivel bits
#       |=                  x = x | n                   Operación or a nivel bits
#       ^=                  x = x ^ n                   Operación xor a nivel bits
#       <<=                 x = x << n                  Operación desplazamiento de bits a la izquierda a nivel bits
#       >>=                 x = x >> n                  Operación desplazamiento de bits a la derecha a nivel bits

valor = 1
valor += 9    # valor = valor + 9
valor -= 1    # valor = valor - 1
valor *= 2    # valor = valor * 2
valor //= 2   # valor = valor // 2
valor %= 3    # valor = valor % 3
valor **= 4   # valor = valor ** 4
valor /= 3    # valor = valor / 3
