# Identificadores, se utilizan para definir los nombres de las variables,
# funciones y clases

# Identicadores válidos: deben de empezar por letra (alfabeto inglés) o guión bajo (_),
# seguido de letras o números o guiones

edad = 27               # Variable numérica entera
_altura = 1.89          # Variable numérica coma flotante
complejo_2 = 4.8 + 2.4j # Variable numérica compleja
mayor = True            # Variable booleana
nombre = "Xoan"         # Variable de texto o cadena

# Sintaxis de escritura de los identificadores:
# - Snake Case: Se utiliza para los identificadores de variables y funciones, y todas las
#   letras deben de estar en minúsculas, para el separador de palabras se utiliza el guión bajo (_)
#   Ejemplo:

edad_maxima = 99
altura_minima = 0.18

def suma_doble(primer_valor, segundo_valor):
    return (primer_valor + segundo_valor) * 2

# - Camel Case: Se utiliza para los identificadores de clases, la primera letra del
#   identificador irá en mayúsculas y después minúsculas
#   Ejemplo:

class HousePosition(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

class HousePosition(object):
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# Aunque en Python no existen las constantes (las variables que nunca cambian de valor), para representar
# este tipo de variables, los identificadores se escriben en mayúsculas
GRAVEDAD = 9.80665
NUMERO_PI = 3.14

# Python es Case Sensitive, es decir, distingue mayúsculas de minúsculas
edad = 'xoan'
EDAD = 20
Edad = 13.6
eDaD = False

print(edad)
print(EDAD)
print(Edad)
print(eDaD)
