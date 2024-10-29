archivo = R'C:/datasets/curso/housing.csv'

with open(archivo, 'r', encoding='utf-8') as archi:
    lineas = archi.readlines()


print(lineas[12933 : ])
