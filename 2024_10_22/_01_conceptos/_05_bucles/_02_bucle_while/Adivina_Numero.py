# Realizar un programa para adivinar un número generado aleatoriamente, y para ello
# solicitaremos un número por teclado para adivinar el número aleatorio, se estará
# solicitando el número hasta que se acierte el número aleatorio.
# Mostrando en pantalla el número total de intentos que ha realizado para adivinar el número

import random # importamos la librería 'random'

aletorio = random.randint(1, 1000) # Se genera un número aleatorio entre 1 y 10000
                                    # ambos inclusive
# aleatorio = 800
# Número entre 1 y 1000
# 600
# Número entre 600 y 1000
# 900
# Número entre 600 y 900
# 700
# Número entre 700 y 900
# 800
# Has acertado, número de intentos 4
intentos = 0
numero = 0
maximo = 10000
minimo = 1
while numero != aletorio: # 800
    print("Número entre", minimo, " y", maximo)
    numero = int(input('Numero: '))
    intentos += 1
    if intentos == 15:
        break
    if numero < aletorio:
        minimo = numero
    elif numero > aletorio:
        maximo = numero

print("Enhorabuena, nº de intentos ", intentos)

