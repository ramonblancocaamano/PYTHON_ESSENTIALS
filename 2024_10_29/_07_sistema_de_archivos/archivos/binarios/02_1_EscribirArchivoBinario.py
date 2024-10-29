from os import strerror
import random


def escribir_numeros(nombre, numero=20):
    try:
        data = bytearray(numero)
        fichero = open(nombre, 'wb')
        for n in range(numero):
            data[n] = random.randint(0, 255)
        fichero.write(data)
        fichero.close()

        '''with open(nombre, 'wb') as file:
            _01_bucle_for n in range(numero):
                data[n] = random.randint(0, 255)
            file.write(data)'''


    except IOError as e:
        print(strerror(e.errno))


def copiar(origen, destino):
    # Archivo tiene 70000
    buffer = bytearray(65536)
    total = 0
    try:
        source_file = open(origen, 'rb')
        destination_file = open(destino, 'wb')
        readin = source_file.readinto(buffer)
        while readin > 0:
            written = destination_file.write(buffer[:readin])
            total += written
            readin = source_file.readinto(buffer)
    except IOError as e:
        print("Error: ", strerror(e.errno))
        exit(e.errno)
    print(total, 'byte(s) escritos con éxito')
    source_file.close()
    destination_file.close()

escribir_numeros('c:/datasets/data/aleatorios.bin')
#copiar('c:/datasets/data/aleatorios.bin', 'c:/datasets/data/aleas.bin')