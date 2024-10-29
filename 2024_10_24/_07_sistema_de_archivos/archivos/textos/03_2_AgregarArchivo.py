from os import strerror


def escribir_lineas(nombre, numero=20):
    try:
        with open(nombre, 'a') as fichero:
            for n in range(1, numero + 1):
                fichero.write(f'Línea número {n}\n')
    except IOError as e:
        print(strerror(e.errno))


def escribir_colecciones(nombre, coleccion):
    try:
        with open(nombre, 'a') as fichero:
            fichero.writelines(coleccion)
    except IOError as e:
        print(strerror(e.errno))


def ejemplos_agregar_archivos():
    lenguajes = ['Python\n', 'Java\n', 'C#\n', 'C/C++\n', 'JavaScript\n']
    numeros = ('1', '2', '3', '4', '5')
    piezas = {'Rey', 'Dama', 'Alfil', 'Torre', 'Caballo', 'Peón'}

    # escribir_lineas(Path.RUTA_ARCHIVOS_MODIFICAR + 'lineas.txt')
    # escribir_colecciones(Path.RUTA_ARCHIVOS_MODIFICAR + 'lenguajes.txt', lenguajes)
    # escribir_colecciones(Path.RUTA_ARCHIVOS_MODIFICAR + 'numeros.txt', numeros)
    # escribir_colecciones(Path.RUTA_ARCHIVOS_MODIFICAR + 'piezas.txt', piezas)


if __name__ == '__main__':
    ejemplos_agregar_archivos()
