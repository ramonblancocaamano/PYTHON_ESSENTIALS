# Definir una función denominada 'dir_files' que recibe como parámetro de entrada el
# nombre de un directorio y, la función devuelve una lista con todos los nombres de
# archivo completo del directorio

import os

# Versión extendida
def dir_files(directory):
    files = []
    for file in os.listdir(directory):
        name_file = os.path.join(directory, file)
        if os.path.isfile(name_file):
            files.append(name_file)
    return files

# Versión reducida
def dir2_files(dir):
    return [os.path.join(dir, file) for file in os.listdir(dir) if os.path.isfile(os.path.join(dir, file))]

# Definir una función denominada 'tree_files' que recibe como parámetro de entrada el
# nombre de un directorio y, la función devuelve una lista con todos los nombres de
# archivo completo del directorio y de sus subdirectorios

# Versión extendida
def tree_files(dir):
    archivos = []
    for (dir, _, files) in os.walk(dir):
        for file in files:
            archivos.append(os.path.join(dir, file))
    return archivos

# Versión reducida
def tree2_files(dir):
    return [os.path.join(d, file) for (d, _, files) in os.walk(dir) for file in files]

# Definir una función denominada 'dir_list_files', que recibe como parámetro de entrada el
# nombre de un directorio y como segundo parámetro opcional de tipo booleano que indicará
# si queremos obtener los archivos del directorio o de todos los subdirectorios y,
# la función devuelve una lista con todos los nombres de archivo completo
def dir_list_files(dir, recursive=False):
    return tree_files(dir) if recursive else dir_files(dir)

# Definir una función denominada 'list_file_text' que recibe como parámetro de entrada el
# nombre de un archivo y la función devuelve el contenido del archivo como una lista
def list_file_text(archivo, cab=False, codificacion='UTF-8'):
    with open(archivo, 'r', encoding=codificacion) as f:
        texto = f.readlines()
    return texto if not cab else texto[1:]

# Definir una función denominada 'file_text' que recibe como parámetro de entrada el
# nombre de un archivo y la función devuelve todo el contenido del archivo
def file_text(archivo, codificacion='UTF-8'):
    with open(archivo, 'r', encoding=codificacion) as f:
        texto = f.read()
    return texto

# Definir una función denominada 'save_text' que recibe como parámetro de entrada el
# nombre de un archivo y como segundo parámetro el texto a guardar en el archivo
def save_text(archivo, texto, encoding='iso-8859-1'):
    with open(archivo, 'w', encoding=encoding) as file:
        file.write(texto)

# Definir una función denominada 'save_list_text' que recibe como parámetro de entrada el
# nombre de un archivo y como segundo parámetro una lista de elementos del tipo texto a
# guardar en el archivo
def save_list_text(archivo, coleccion, encoding='utf-8', encabezado=None):
    with open(archivo, 'w', encoding=encoding) as file:
        # convertir los elementos de la colección a tipo texto y con salto de línea
        coleccion = [str(elemento) + '\n' for elemento in coleccion]
        if encabezado:
            file.write(F'{encabezado}\n')
        file.writelines(coleccion)

