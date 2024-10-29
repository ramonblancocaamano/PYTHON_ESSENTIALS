'''
    Escribe un programa que pida el límite inferior y superior de un intervalo. Si el límite inferior es mayor que el superior lo tiene que
    volver a pedir. A continuación se van introduciendo números hasta que introduzcamos el '0'.
    Cuando termine el programa dará las siguientes informaciones:
    – La suma de los números que están dentro del intervalo (intervalo abierto).
    – Cuantos números están fuera del intervalo.
    – Informa si hemos introducido algún número igual a los límites del intervalo.
'''

limite_superior = int(input('Límite superior: '))
limite_inferior = limite_superior + 1
while limite_inferior > limite_superior:
    limite_inferior = int(input('Límite inferior: '))
suma_numeros = 0
numeros_limite = 0
numeros_fuera = 0
while True:
    numero = int(input('Número: '))
    if numero == 0:
        break
    if numero > limite_inferior and numero < limite_superior:
        suma_numeros += numero
    elif numero > limite_superior or numero < limite_inferior:
        numeros_fuera += 1
    elif numero == limite_inferior or numero == limite_superior:
        numeros_limite += 1
print("Suma números", suma_numeros)
print("Números fuera de límite", numeros_fuera)
print("Números iguales a los límites", numeros_limite)
