from os import strerror
import random


def escribir_numeros(nombre, numero=20):
    try:
        data = bytearray(numero)
        for n in range(numero):
            data[n] = random.randint(0, 255)
        with open(nombre, 'ab') as fichero:
            fichero.write(data)
    except IOError as e:
        print(strerror(e.errno))

escribir_numeros('c:/datasets/data/aleatorios.bin')
