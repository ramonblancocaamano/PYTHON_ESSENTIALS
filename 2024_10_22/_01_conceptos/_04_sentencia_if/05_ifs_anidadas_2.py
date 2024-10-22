# ------------------------------------------------------------------------------------------
# Sentencia if completa y anidamiento
# ------------------------------------------------------------------------------------------

valor = int(input("Introduzca un valor numerico entero: "))
if valor > 0 and valor <= 10:
    if valor > 5:
        if valor == 7:
            print("Es un numero primo")
        print(valor)
    else:
        valor *= -1
        print(valor)
elif valor > 10 and valor <= 20:
    if valor > 15:
        if valor == 19:
            print("Es un numero primo")
        print(valor)
    else:
        valor *= -1
        print(valor)
elif valor > 20 and valor <= 30:
    if valor > 25:
        if valor == 29:
            print("Es un numero primo")
        print(valor)
    else:
        valor *= -1
        print(valor)
else:
    if valor < 0:
        print("No se admiten valores negativos")
    else:
        par = valor % 2 == 0
        impar = valor % 2 == 1
        if par == True:
            print("El numero es par")
        if impar == True:
            print("El numero es impar")

