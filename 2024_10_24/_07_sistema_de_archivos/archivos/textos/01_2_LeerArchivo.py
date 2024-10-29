from os import strerror


def leer_archivo_entero(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as fichero:
            texto = fichero.read()
        print(texto)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_caracter(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as fichero:
            char = fichero.read(1)
            counter = 0
            while char != '':
                print(char, end='')
                counter += 1
                char = fichero.read(1)
        print("\n\nCaracteres en el archivo:", counter)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_linea(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as fichero:
            linea = fichero.readline()
            count_char = 0
            count_linea = 0
            while linea != '':
                count_linea += 1
                for char in linea:
                    print(char, end='')
                    count_char += 1
                linea = fichero.readline()
        print("\n\nCaracteres en el archivo:", count_char)
        print("Líneas en el archivo:     ", count_linea)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_lineas(nombre):
    try:
        with open(nombre, 'r', encoding='utf-8') as fichero:
            lineas = fichero.readlines()
            count_linea = len(lineas)
            count_char = 0
            for linea in lineas:
                for char in linea:
                    print(char, end='')
                    count_char += 1
        print("\n\nCaracteres en el archivo:", count_char)
        print("Líneas en el archivo:     ", count_linea)
    except IOError as e:
        print(strerror(e.errno))


def ejemplos_leer_archivos():
    # leer_archivo_entero(Path.RUTA_ARCHIVOS_DATA + 'provincias.data')
    # leer_archivo_por_caracter(Path.RUTA_ARCHIVOS_DATA + 'provincias.data')
    # leer_archivo_por_linea(Path.RUTA_ARCHIVOS_DATA + 'provincias.data')
    # leer_archivo_por_lineas(Path.RUTA_ARCHIVOS_DATA + 'provincias.data')
    pass


if __name__ == '__main__':
    ejemplos_leer_archivos()
