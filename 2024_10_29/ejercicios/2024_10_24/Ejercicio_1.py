'''
Ejercicio número 1
------------------------------------------------------------------------------------------------------------------------------------------------------
Dado los siguientes datasets: 'nombres.data' y 'apellidos.data'
Definir una función que recibe dos parámetros de entrada indicando el número de nombres masculinos y el número de nombres femeninos, devolviendo
una lista con todos los nombres masculinos y femeninos generados.

El formato del nombre es: Nombre Apellido1 Apellido2

Los nombres se obtendrán del dataset 'nombres.data' y los apellidos del dataset 'apellidos.data'
Para la lectura de los datasets anteriores utilizar las funciones correspondientes del módulo 'Files.py' del paquete 'api'.
Utilizar también la librería 'random' de Python para la generación de valores aleatorios.
'''

import random
from api import Files, Paths

def nombres(numero_masculinos, numero_femeninos):
    nombres_personas = Files.list_file_text(Paths.FILE_NOMBRES)[1:]
    apellidos_personas = Files.list_file_text(Paths.FILE_APELLIDOS)[1:]
    nombres_masculinos = [n for n in nombres_personas if n.rstrip().split(';')[1] == 'h']
    nombres_femeninos = [n for n in nombres_personas if n.rstrip().split(';')[1] == 'm']
    lista_nombres = []
    for _ in range(numero_masculinos):
        aleatorio = random.randint(0, len(nombres_masculinos) - 1)
        nombre = nombres_masculinos[aleatorio].rstrip().split(';')[0]
        aleatorio = random.randint(0, len(apellidos_personas) - 1)
        apellido_1 = apellidos_personas[aleatorio].rstrip()
        aleatorio = random.randint(0, len(apellidos_personas) - 1)
        apellido_2 = apellidos_personas[aleatorio].rstrip()
        lista_nombres.append(F'{nombre} {apellido_1} {apellido_2}')
    for _ in range(numero_femeninos):
        aleatorio = random.randint(0, len(nombres_femeninos) - 1)
        nombre = nombres_femeninos[aleatorio].rstrip().split(';')[0]
        aleatorio = random.randint(0, len(apellidos_personas) - 1)
        apellido_1 = apellidos_personas[aleatorio].rstrip()
        aleatorio = random.randint(0, len(apellidos_personas) - 1)
        apellido_2 = apellidos_personas[aleatorio].rstrip()
        lista_nombres.append(F'{nombre} {apellido_1} {apellido_2}')
    random.shuffle(lista_nombres)
    return lista_nombres

print(nombres(50, 50))
