'''
Definir una función en Python que recibe como parámetro el nombre de un directorio y,
la función debe de devolver el tamaño en bytes de todos los archivos de ese directorio y
de todos sus subdirectorios.
'''

import os

def bytes_dir(directory):
    bytes = 0
    for (dir, _, files) in os.walk(directory):
        for file in files:
            name_file = os.path.join(dir, file)
            bytes += os.path.getsize(name_file)
    return bytes

total = bytes_dir('c:/datasets/')
print('Total bytes =>', total)
