from os import strerror

def leer_archivo_entero(nombre, encoding='utf-8'):
    try:
        # https://unicode.org

        # Codificación UTF-8, ISO-8859-1
        fichero = open(nombre, 'r', encoding=encoding)
        texto = fichero.read()
        fichero.close()
        print(texto)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_caracter(nombre, encoding='utf-8'):
    try:
        fichero = open(nombre, 'r', encoding=encoding)
        char = fichero.read(1)
        counter = 0
        while char != '':
            print(char, end='')
            counter += 1
            char = fichero.read(1)
        fichero.close()
        print("\n\nCaracteres en el archivo:", counter)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_linea(nombre, encoding='utf-8'):
    try:
        # \r\n o \n o \t
        fichero = open(nombre, 'r', encoding=encoding)
        linea = fichero.readline()
        linea = linea.rstrip()   # trim -> Java, C#, JavaScript, explode (php)
        count_char = 0
        count_linea = 0
        while linea != '':
            count_linea += 1
            count_char += len(linea)
            linea = fichero.readline()
        fichero.close()
        print("Caracteres en el archivo:", count_char)
        print("Líneas en el archivo:     ", count_linea)
    except IOError as e:
        print(strerror(e.errno))


def leer_archivo_por_lineas(nombre):
    try:
        fichero = open(nombre, 'r', encoding='utf-8')
        lineas = fichero.readlines()
        print(type(lineas))
        count_linea = len(lineas)
        count_char = 0
        for linea in lineas:
            count_char += len(linea)
        fichero.close()
        print(len(lineas))
        print(type(lineas))
        print(lineas)
        #print("\n\nCaracteres en el archivo:", count_char)
        #print("Líneas en el archivo:     ", count_linea)
    except IOError as e:
        print(strerror(e.errno))


def ejemplos_leer_archivos():
    try:
        fichero = open('c:/datasets/data/texto.txt.txt', 'r')
        caracter = fichero.read()
        fichero.close()
        print(caracter)
    except UnicodeDecodeError as ude:
        print('Error en el tipo de codificación de texto')
    except IOError as e:
        print('No se puede leer el archivo', e)

#leer_archivo_entero('c:/datasets/curso/poblaciones.data')

#leer_archivo_por_caracter('c:/datasets/curso/poblaciones.data')
#leer_archivo_por_linea('c:/datasets/data/poblaciones.data')
leer_archivo_por_lineas('c:/datasets/curso/poblaciones.data')



