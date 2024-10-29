# ------------------------------------------------------------------------------------------
# Sentencia if completa y anidamiento
# ------------------------------------------------------------------------------------------

valor = int(input("Introduzca un valor numerico entero: "))
suma = 0
if valor > 10000:
    if valor >= 20000:
        suma += valor - 1000
    else:
        suma += valor
elif valor > 5000:
    if valor < 7000:
        suma += valor
    else:
        suma = suma + valor - 500
else:
    if valor < 1:
        suma = 0
    else:
        suma = suma + valor + 10
print("suma", suma)
