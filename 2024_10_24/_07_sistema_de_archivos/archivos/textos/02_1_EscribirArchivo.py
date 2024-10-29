from os import strerror

def escribir_lineas(nombre, numero=20):
    try:
        with open(nombre, 'w') as fichero:
            for n in range(1, numero + 1):
                fichero.write(f'Línea número {n}\n')
    except IOError as e:
        print(strerror(e.errno))


def escribir_colecciones(nombre, coleccion):
    try:
        fichero = open(nombre, 'w')
        fichero.writelines(coleccion)
        fichero.close()
    except IOError as e:
        print(strerror(e.errno))

'''try:
    fichero = open('c:/datasets/data/ejemplo2.txt', 'w')
    _01_bucle_for x in range(4):
        fichero.write('Alicante\n')
    fichero.close()
except:
    print('Error de escritura')'''

#escribir_lineas('c:/datasets/data/ejemplo_lineas_20.txt', 20)

nombres = ['Ana', 'Pepa', 'Juan']
#nombres_con_salto = [n + '\n' _01_bucle_for n in nombres]
nombres_con_salto = map(lambda elemento: elemento + '\n', nombres)
# filter(funcion, coleccion)
escribir_colecciones('c:/datasets/data/colecciones_nombres.txt', nombres_con_salto)
