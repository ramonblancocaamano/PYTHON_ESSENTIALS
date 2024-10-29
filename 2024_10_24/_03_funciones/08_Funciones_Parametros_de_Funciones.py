# ------------------------------------------------------------------------------------------
# Funciones con parámetros de funciones
# ------------------------------------------------------------------------------------------

def operacion(funcion, parametro_1, parametro_2):
    return funcion(parametro_1, parametro_2)

def calculo(funcion, *parametro_1, **parametro_2):
    return funcion(*parametro_1, **parametro_2)

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def sumatorio(*numeros, **valores):
    total = 0
    for n in numeros:
        total += n
    for v in valores.values():
        total += v
    return total

opera = calculo(sumatorio, 2, 4, 5, f=7, r=3, t=10, w=30)
print(opera)

def conversor(value):
    if value == 1:
        return int
    if value == 2:
        return float
    return str

d = 2
tipo = conversor(2)
print(tipo(d))


