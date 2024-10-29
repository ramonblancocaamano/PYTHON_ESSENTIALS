from os import strerror


def leer_archivo_entero(nombre):
    try:
        with open(nombre, 'r+') as fichero:
            fichero.seek(13)
            fichero.write('Tercera Nueva linea\n')
            fichero.read()
            fichero.write('Segunda Nueva linea\n')
    except IOError as e:
        print(strerror(e.errno))


if __name__ == '__main__':
    leer_archivo_entero('c:/datasets/curso/ejemplo_lineas_20.txt')
