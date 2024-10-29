'''
Realizar un programa Python que dado el dataset 'poblaciones.data', mostrar en pantalla
todas las poblaciones de la provincia de Barcelona como una lista, utilizando el
módulo 'Files.py' del paquete 'api' del proyecto
'''
import api.Files as Files

poblaciones = Files.list_file_text('c:/datasets/curso/poblaciones.data', codificacion='utf-8', cab=True)
print(poblaciones)

