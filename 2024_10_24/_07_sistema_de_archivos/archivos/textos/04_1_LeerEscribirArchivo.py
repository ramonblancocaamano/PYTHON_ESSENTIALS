from os import strerror


def leer_archivo_entero(nombre):
    try:
        fichero = open(nombre, 'r+')
        fichero.read()
        fichero.write('Otra Nueva linea\n')
        fichero.write('Segunda Nueva linea\n')
        fichero.close()
    except IOError as e:
        print(strerror(e.errno))

leer_archivo_entero('c:/datasets/data/ejemplo_lineas_20.txt')