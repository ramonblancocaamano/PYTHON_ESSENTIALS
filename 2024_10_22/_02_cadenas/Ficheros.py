nombre_archivo = r'C:\datasets\csv\housing.data'

with open(nombre_archivo, 'r') as file:
    lineas_texto = file.readlines()

for n in lineas_texto[1:]:
    print(n.strip())

