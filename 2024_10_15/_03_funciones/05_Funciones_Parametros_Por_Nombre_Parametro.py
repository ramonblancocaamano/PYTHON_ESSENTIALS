# ------------------------------------------------------------------------------------------
# Funciones con argumentos o parámetros por defecto y llamadas a funciones
# utilizando nombres de parámetros y valores
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
# Ejemplo 1:
# ------------------------------------------------------------------------------------------

def sumas(a, b, c, d):
    rdo = a + b + c + d
    return rdo

sumas_x = sumas(1,2,3,4)

suma_0 = sumas(a=1, b=2, c=3, d=4)

suma_1 = sumas(b=3, d=4, a=5, c=8)
suma_2 = sumas(3, c=4, d=5, b=7)
suma_3 = sumas(3, 4, d=5, c=7)
suma_4 = sumas(c=3, a=4, d=5, b=7)

print(suma_1)
print(suma_2)
print(suma_3)
print(suma_4)

# ------------------------------------------------------------------------------------------
# Ejemplo 2:
# ------------------------------------------------------------------------------------------

def dividir(a, b=1, entera=False):
    if entera:
        rdo = a // b
    else:
        rdo = a / b
    return rdo

entera = dividir(entera=True, a=8123, b=4)
real = dividir(b=3, entera=False, a=43212)
print("división entera=>", entera)
print("división real=>", real)
