from os import strerror

def leer_numeros(nombre):
    try:
        fichero = open(nombre, 'rb')
        data = bytearray(fichero.read())
        fichero.close()
        for b in data:
            print(b, end=' ')
    except IOError as e:
        print(strerror(e.errno))


def leer(nombre, bytes=10):
    data = bytearray(bytes)
    try:
        fichero = open(nombre, 'rb')
        fichero.readinto(data)
        fichero.close()
        for b in data:
            print(b, end=' ')
    except IOError as e:
        print(strerror(e.errno))


def leer_bytes(nombre, numeros=10):
    try:
        fichero = open(nombre, 'rb')
        data = bytearray(fichero.read(numeros))
        fichero.close()
        for b in data:
            print(b, end=' ')
    except IOError as e:
        print(strerror(e.errno))


#leer_numeros('c:/datasets/data/nomes.pdf')
#leer_bytes('c:/datasets/data/nomes.pdf')
leer('c:/datasets/data/nomes.pdf', 6)
