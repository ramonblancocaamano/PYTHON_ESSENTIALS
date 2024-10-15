# ------------------------------------------------------------------------------------------
# Funciones con argumentos o parámetros por defecto.
# ------------------------------------------------------------------------------------------

def dividir(a, b=1, entera=False):
    if entera:
        rdo = a // b
    else:
        rdo = a / b
    return rdo

rdo1 = dividir(4, 5, True)
rdo2 = dividir(4, 5)
rdo3 = dividir(4)
print("dividir -> rdo1 =>", rdo1)
print("dividir -> rdo2 =>", rdo2)
print("dividir -> rdo3 =>", rdo3)

print('-' * 80)

# ------------------------------------------------------------------------------------------
# Podemos asignar un valor por defecto a todos los parámetros de la función,
# por lo que se podría llamar a la función sin ningún argumento de entrada.
# ------------------------------------------------------------------------------------------

def sumas(a=0, b=0, c=0):
    return a + b + c

print(sumas(1,3,4))
rdo2 = sumas(1,3)
rdo3 = sumas(1)
rdo4 = sumas()
print("sumas -> rdo1 =>", rdo1)
print("sumas -> rdo2 =>", rdo2)
print("sumas -> rdo3 =>", rdo3)
print("sumas -> rdo4 =>", rdo4)
