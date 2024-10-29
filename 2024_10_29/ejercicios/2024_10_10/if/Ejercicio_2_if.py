'''
    Realizar un programa que solicite por teclado un importe númerico en coma flotante, y una determinada cantidad o unidad y,
    calcule el importe total en base a la siguiente fórmula:

    tipo de iva = 21 / 100

    Cálculo del iva:
    iva = importe (por teclado) * cantidad (o unidad por teclado) * tipo de iva

    importe total = importe (por teclado) * cantidad (o unidad por teclado) + iva

    Cálculo tipo de iva:
    Inicialmente el tipo de iva será del 21%, condiciones que varian el tipo de iva:
    - Si el importe (por teclado) es superior a 50000, el tipo de iva será del 2%
    - Si el importe (por teclado) es superior a 25000, el tipo de iva será del 4%
    - Si el importe (por teclado) es superior a 10000, el tipo de iva será del 8%

    Mostrar en pantalla el importe total resultante.
'''

importe = float(input("Importe: "))
unidades =int(input("Unidades: "))

if importe > 50000:
    tipo_de_iva = 2
elif importe > 25000:
    tipo_de_iva = 4
elif importe > 10000:
    tipo_de_iva = 8
else:
    tipo_de_iva = 21

importe_total = importe * unidades
iva_importe = importe_total * tipo_de_iva / 100
importe_mas_iva = importe_total + iva_importe

print('Importe total =>', importe_mas_iva)
