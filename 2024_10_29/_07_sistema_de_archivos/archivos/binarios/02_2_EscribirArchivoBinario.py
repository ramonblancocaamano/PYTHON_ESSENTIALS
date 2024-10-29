from os import strerror
import random


def escribir_numeros(nombre, numero=20):
    try:
        data = bytearray(numero)
        for n in range(numero):
            data[n] = random.randint(0, 255)
        with open(nombre, 'wb') as fichero:
            fichero.write(data)
    except IOError as e:
        print(strerror(e.errno))


def copiar(origen, destino):
    buffer = bytearray(65536)
    total = 0
    try:
        with open(origen, 'rb') as source_file:
            with open(destino, 'wb') as destination_file:
                leer = source_file.readinto(buffer)
                while leer > 0:
                    bytes = destination_file.write(buffer[:leer])
                    total += bytes
                    leer = source_file.readinto(buffer)
    except IOError as e:
        print("Error: ", strerror(e.errno))
        exit(e.errno)
    print(total, 'byte(s) escritos con éxito')


#escribir_numeros('c:/datasets/data/aleatorios.bin')
copiar('c:/datasets/data/aleatorios.bin', 'c:/datasets/data/numeros.bin')
