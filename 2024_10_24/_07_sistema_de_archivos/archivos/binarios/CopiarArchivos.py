import shutil

source = 'c:/datasets/data/nomes_catalans.pdf'
destination = 'c:/datasets/data/nomes.pdf'

try:
    shutil.copy(source, destination)
    print("Archivo copiado.")
except shutil.SameFileError:
    print("El origen y el destino son el mismo archivo.")
except PermissionError:
    print("Permison denegado.")
except:
    print("Ha ocurrido un Error mientras se copiaba el archivo.")

