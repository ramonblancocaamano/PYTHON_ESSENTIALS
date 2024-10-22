'''
    Realizar un programa que solicite por teclado los siguientes datos (hasta que se introduzca un nombre vacío):
    - El nombre de una persona
    - La edad de la persona
    - Y el sexo de la persona: 'h' o 'H' para el hombre y 'm' o 'M' para la mujer

    Contabilizar el número total de hombres y el número total mujeres que se han introducido, además calcular
    la edad media de los hombres y la edad media de las mujeres, mostrando en pantalla los resultados.
'''

numero_hombres = 0
numero_mujeres = 0
edades_hombres = 0
edades_mujeres = 0
while True:
    nombre = input('Nombre: ')
    if nombre == '':
        break
    edad = int(input('Edad: '))
    sexo = input('Sexo (h/m): ')
    if sexo == 'h' or sexo == 'H':
        numero_hombres += 1
        edades_hombres += edad
    elif sexo == 'm' or sexo == 'M':
        numero_mujeres += 1
        edades_mujeres += edad

edad_media_hombres = edades_hombres // numero_hombres
edad_media_mujeres = edades_mujeres // numero_mujeres

print('numero hombres =>', numero_hombres)
print('numero mujeres =>', numero_mujeres)
print('edad media hombres =>', edad_media_hombres)
print('edad media mujeres =>', edad_media_mujeres)
