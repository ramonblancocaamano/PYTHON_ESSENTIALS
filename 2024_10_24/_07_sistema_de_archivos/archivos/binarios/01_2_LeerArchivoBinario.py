from os import strerror

def leer_numeros(nombre):
    try:
        with open(nombre, 'rb') as fichero:
            data = bytearray(fichero.read())
        for b in data:
            print(b, end=' ')
    except IOError as e:
        print(strerror(e.errno))


def leer(nombre, bytes=10):
    data = bytearray(bytes)
    try:
        with open(nombre, 'rb') as fichero:
            fichero.readinto(data)
        for b in data:
            print(hex(b), end=' ')
    except IOError as e:
        print(strerror(e.errno))


def leer_bytes(nombre, numeros=10):
    try:
        with open(nombre, 'rb') as fichero:
            data = bytearray(fichero.read(numeros))
        for b in data:
            print(hex(b), end=' ')
    except IOError as e:
        print(strerror(e.errno))


def ejemplos_leer_archivos():
    leer_numeros('c:/datasets/data/aleatorios.bin')
    #leer_bytes('c:/datasets/data/aleatorios.bin')
    #leer_bytes('c:/datasets/data/numeros.bin')

ejemplos_leer_archivos()