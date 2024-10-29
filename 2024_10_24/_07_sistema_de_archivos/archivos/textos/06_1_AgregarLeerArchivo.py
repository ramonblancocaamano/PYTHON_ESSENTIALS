from os import strerror

def agregar_leer_archivo(nombre):
    try:
        f = open(nombre, 'a+')
        f.seek(0)
        lines = f.readlines()
        f.write("\n" + str(len(lines)))
        f.close()
    except IOError as e:
        print(strerror(e.errno))

