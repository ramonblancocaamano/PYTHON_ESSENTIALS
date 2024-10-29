'''
Realizar un programa que solicite los siguientes datos por teclado hasta indicar que no queramos introducir más datos:
	- Nombre de una persona
	- Provincia de la persona
	- Edad de la persona
	- Altura de la persona
    Nota: Una vez introducidos los datos anteriores se preguntará si queremos introducir más datos.
          Los datos anteriores (nombre, provincia, edad, altura) se guardarán como un diccionario.

Mostrar en pantalla una colección de tipo lista con todos los datos introducidos.

Ejemplo de salida por pantalla de los datos introducidos:
[{'nombre':'Mia', 'provincia':'Barcelona', 'edad': 9, 'altura':1.45}, {'nombre':'Rosa', 'provincia':'Granada', 'edad': 39, 'altura':1.68}]
'''

records = []
while True:
    data = {}
    data['nombre'] = input('Nombre: ')
    data['provincia'] = input('Provincia: ')
    data['edad'] = float(input('Edad: '))
    data['altura'] = float(input('Altura: '))
    records.append(data)
    if input('Desea introducir más datos (s/n): ').lower() != 's': break

print(records)
