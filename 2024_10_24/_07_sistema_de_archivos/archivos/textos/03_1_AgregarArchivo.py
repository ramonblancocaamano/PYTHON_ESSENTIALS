from os import strerror

def escribir_lineas(nombre, numero=20):
    try:
        with open(nombre, 'a') as fichero:
            for n in range(1, numero + 1):
                fichero.write(f'Línea número {n + 40}\n')
    except IOError as e:
        print(strerror(e.errno))


def escribir_colecciones(nombre, coleccion):
    try:
        fichero = open(nombre, 'a')
        fichero.writelines(coleccion)
        fichero.close()
    except IOError as e:
        print(strerror(e.errno))

'''try:
    fichero = open('c:/datasets/data/datos.txt', 'w')
    _01_bucle_for x in range(4):
        fichero.write('Alicante\n')
    fichero.close()
except:
    print('Error de escritura')
try:
    fichero = open('c:/datasets/data/datos.txt', 'a')
    _01_bucle_for x in range(4):
        fichero.write(f'Numero línea {x + 1}\n')
    fichero.close()
except:
    print('Error de escritura')'''

n = ['Luci', 'Marga']

escribir_lineas('c:/datasets/data/ejemplo_lineas_20.txt')
#escribir_colecciones('c:/datasets/data/lineas.txt', n)
