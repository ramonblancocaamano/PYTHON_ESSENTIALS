import os
import datetime

# Muestra el tipo de sistema operativo
def tipo_so():
    # Muestra   Sistema operativo
    # ---------------------------
    # posix     Si es Unix/Linux
    # nt        Si es Windows
    print(os.name)


# Crea un directorio, lanza un excepción si ya existe el directorio
def crear_directorio(directorio):
    try:
        os.mkdir(directorio)
    except FileExistsError as fee:
        print('El directorio ya existe')


# Crea directorios, lanza un excepción si ya existen los directorios
def crear_directorios(directorios):
    try:
        os.makedirs(directorios)
    except FileExistsError as fee:
        print('El directorio ya existe')


# Crea directorios
def crear2_directorios(directorios):
    os.makedirs(directorios, exist_ok=True)


# Cambia de directorio, lanza una excepción si el directorio no existe
def cambiar_directorio(directorio):
    try:
        os.chdir(directorio)
    except FileNotFoundError as fnfe:
        print('El directorio no existe')

# Elimina el directorio, lanza una excepción si el directorio no existe
def eliminar_directorio(directorio):
    try:
        os.rmdir(directorio)
    except FileNotFoundError as fnfe:
        print('El directorio no existe')
    except OSError as oe:
        print('El directorio no está vacío')


# Elimina los directorios, lanza una excepción si los directorios non existen o no están vacíos
def eliminar_directorios(directorios):
    try:
        os.removedirs(directorios)
    except FileNotFoundError as fnfe:
        print('Los directorios no existen')
    except OSError as oe:
        print('Los directorios no están vacíos')


# Muestra la ruta actual del directorio de trabajo
def mostrar_ruta_actual():
    print(os.getcwd())


# Ejecuta un comando del sistema operativo
def ejecuta_comando(comando):
    valor = os.system(comando)
    print(valor)


# Obtiene los _06_sistema y subdirectorios de un directorio, lanza una excepción si el directorio no existe
def obtener_archivos(directorio):
    try:
        for fichero in os.listdir(directorio):
            print(fichero)
    except FileNotFoundError as fnfe:
        print('El directorio no existe')

def obtener2_archivos(directorio):
    try:
        with os.scandir(directorio) as entries:
            for entry in entries:
                print(entry.stat())
    except FileNotFoundError as fnfe:
        print('El directorio no existe')

# Obtiene los archivos de un directorio y de sus subdirectorios, lanza una excepción si el directorio no existe
def obtener_todos_archivos(directorio):
    for (dir, subdir, files) in os.walk(directorio):
        for file in files:
            print(os.path.join(dir, file))


# Muestra el nombre completo del archivo (directorio y nombre del archivo)
def mostrar_archivos_completos(directorio):
    try:
        for fichero in os.listdir(directorio):
            nombre_fichero = os.path.join(directorio, fichero)
            print(nombre_fichero)
    except FileNotFoundError as fnfe:
        print('El directorio no existe')


# Eliminar los archivos de un directorio
def eleminar_archivos(directorio):
    for file in os.listdir(directorio):
        os.remove(os.path.join(directorio, file))


# Muestra el estado del archivo o directorio
def estado_archivos(directorio):
    try:
        for fichero in os.listdir(directorio):
            nombre_fichero = os.path.join(directorio, fichero)
            print(os.stat(nombre_fichero))
    except FileNotFoundError as fnfe:
        print('El directorio no existe')


# Devuelve la ruta completa del directorio al cual pertenece el archivo
def get_directorio(file_name):
    try:
        return os.path.dirname(file_name)
    except FileNotFoundError as fnfe:
        print('El directorio no existe')


# Comprueba si un archivo es un archivo
def es_archivo(file_name):
    return os.path.isfile(file_name)


# Comprueba si un archivo es un directorio
def es_directorio(file_name):
    return os.path.isdir(file_name)


# Comprueba si un archivo es un acceso directo
def es_enlace(file_name):
    return os.path.islink(file_name)


# Comprueba si un archivo o directorio existe
def existe(file_name):
    return os.path.exists(file_name)


# Devuelve el tamaño de un archivo o directorio en bytes
def tamanho_bytes(directorio):
    try:
        for fichero in os.listdir(directorio):
            nombre_fichero = os.path.join(directorio, fichero)
            bytes = os.path.getsize(nombre_fichero)
            print(bytes)
    except FileNotFoundError as fnfe:
        print('El archivo o directorio no existe')


def data(file):
    stat = os.stat(file)
    data = {}
    path, name = os.path.split(file)
    data['path'] = path
    data['name'] = name
    data['file'] = file
    data['size'] = stat.st_size
    data['access'] = datetime.datetime.fromtimestamp(stat.st_atime)
    data['last'] = datetime.datetime.fromtimestamp(stat.st_mtime)
    data['create'] = datetime.datetime.fromtimestamp(stat.st_ctime)
    return data

def ejemplos_modulo_os():
    #tipo_so()
    # crear_directorio('c:\\install\\nuevo')
    # crear_directorios('c:\\install\\nuevo\\datos')
    # crear2_directorios('c:\\install\\nuevo\\datos')
    # cambiar_directorio('c:\\lucaas')
    # eliminar_directorio('c:\\datasets\datos')
    # eliminar_directorios('c:\\datasets\datos')
    # mostrar_ruta_actual()
    # ejecuta_comando("mkdir c:\\install\\nuevo")
    # obtener_archivos('c:\\datasets')
    # obtener_todos_archivos('c:\\datasets')
    # mostrar_archivos_completos('c:\\lucaas')
    # eleminar_archivos('c:\\lucaas')
    # estado_archivos(Path.RUTA_ARCHIVOS_DATA)
    # tamanho_bytes(Path.RUTA_ARCHIVOS_DATA)
    pass
