'''
Dado el dataset 'taxi_flota_diario.csv', realizar un programa que muestre en pantalla lo siguiente:

- Todas las marcas únicas de vehículos.
- Número total de vehículos por cada tipo marca. Indicando la marca y el número de vehículos
- Número total de vehículos por tipo de combustible. Indicando el tipo de combustible y el número de vehículos
- Número total de vehículos por año de matriculación. Indicando el año de matriculación y el número de vehículos

Utilizar todos los módulos oportunos del paquete 'api' del proyecto.
'''

from api import Paths, Files

taxis = Files.list_file_text(Paths.FILE_TAXIS)[1:]

# Todas las marcas únicas de vehículos.
# -------------------------------------------------------------------------------------------------------------------
uni_marcas = [reg.split(';')[3] for reg in taxis]
marcas_unicas = set(uni_marcas)
print(marcas_unicas)

# Número total de vehículos por cada tipo marca. Indicando la marca y el número de vehículos
# -------------------------------------------------------------------------------------------------------------------
marcas = {}
for marca in marcas_unicas:
    filtrado = [r for r in taxis if r.split(';')[3] == marca]
    marcas[marca] = len(filtrado)
print(marcas)

# Número total de vehículos por tipo de combustible. Indicando el tipo de combustible y el número de vehículos
# -------------------------------------------------------------------------------------------------------------------
tipos = [reg.split(';')[8] for reg in taxis]
tipo_combustibles = set(tipos)
combustibles = {}
for combustible in tipo_combustibles:
    filtrado = [r for r in taxis if r.split(';')[8] == combustible]
    combustibles[combustible] = len(filtrado)
print(combustibles)

# Número total de vehículos por año de matriculación. Indicando el año de matriculación y el número de vehículos
# -------------------------------------------------------------------------------------------------------------------
anhos = [reg.split(';')[2].split('/')[2] for reg in taxis]
anhos_matriculacion = set(anhos)
matriculaciones = {}
for anho in anhos_matriculacion:
    filtrado = [r for r in taxis if r.split(';')[2].split('/')[2] == anho]
    matriculaciones[anho] = len(filtrado)
print(matriculaciones)
