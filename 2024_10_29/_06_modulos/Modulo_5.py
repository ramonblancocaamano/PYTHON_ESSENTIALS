from api.Inputs import read_int, read_float
#from api.Inputs import *

if __name__ == '__main__':
    nombre = input('Nombre: ')
    edad = read_int('Edad: ')
    altura = read_float('Altura: ')
    print(nombre, edad, altura)

