from os import strerror


def agregar_leer_archivo(nombre):
    try:
        with open(nombre, 'a+') as f:
            f.seek(0)
            lines = f.readlines()
            f.write("\n" + str(len(lines)))
    except IOError as e:
        print(strerror(e.errno))

agregar_leer_archivo('c:/datasets/data/lineas.txt')
