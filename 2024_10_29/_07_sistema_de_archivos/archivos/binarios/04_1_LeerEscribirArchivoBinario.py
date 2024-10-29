from os import strerror

def leer_numeros(nombre):
    try:
        bytes = bytearray(3)
        bytes[0] = 67
        bytes[1] = 66
        bytes[2] = 65
        with open(nombre, 'rb+') as fichero:
            data = bytearray(fichero.read())
            fichero.seek(20)
            fichero.write(bytes)
        for b in data:
            print(b, end=' ')

    except IOError as e:
        print(strerror(e.errno))

