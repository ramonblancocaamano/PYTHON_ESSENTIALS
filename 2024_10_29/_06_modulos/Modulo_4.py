from api import Inputs as I
from _06_modulos import Modulo_1 as M

#import api.Inputs as I
#import _06_modulos.Modulo_1 as M

def __suma(s,b):
    return s+b

if __name__ == '__main__':
    nombre = input('Nombre: ')
    edad = I.read_int('Edad: ')
    nueva_edad = M.inc(edad)
    print(nombre, edad, nueva_edad)

