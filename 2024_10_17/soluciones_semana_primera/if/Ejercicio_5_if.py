'''
    Realizar un programa que solicite por teclado una distancia en centímetros y que escriba esa distancia en kilómetros, metros y
    centímetros (escribiendo todas las unidades).

    Ejemplos:
    -------------------------------------------
    Distancia en centímetros: 43210
    Se muestra: 43210 son 0 km 432 m 10 cm
    -------------------------------------------
    Distancia en centímetros: 56
    Se muestra: 56 son 0 km 0 m 56 cm
'''

distancia_cm = int(input('Distancia en cm: '))
kilometros = distancia_cm // 100000
resto_cm = distancia_cm % 100000
metros = resto_cm // 100
centimetros = resto_cm % 100
print(distancia_cm, 'son =>', kilometros, 'km', metros, 'm', centimetros, 'cm')
