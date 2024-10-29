# Leer el archivo 'poblaciones.data' y mostrar en pantalla todas las poblaciones
# de la provincia de 'Barcelona'

archivo = open('c:/datasets/curso/poblaciones.data', 'r', encoding='utf-8')
lineas = archivo.readlines()
archivo.close()

'''
with open('c:/datasets/curso/poblaciones.data', 'r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
'''

for line in lineas[1:]:
    datos = line.rstrip().split(';')
    if datos[1] == '8':
        print(datos[2])
