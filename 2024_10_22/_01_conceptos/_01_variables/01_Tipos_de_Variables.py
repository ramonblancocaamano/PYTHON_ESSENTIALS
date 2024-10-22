# ---------------------------------------------------------------------------------------------
# Tipos de variables en Python
# ---------------------------------------------------------------------------------------------

# - Numéricos: int, float, complex
# - Booleanos: bool
# - Colecciones: str, list, set, tuple, dict, range, generator
# - Objetos: class

# Una característica muy importante de Python, es que, el tipo de las variables es dinámico, es decir,
# pueden cambiar su tipo inicial a otro tipo de variable.
# Esta característica en los lenguajes tipeados (como java, c#, scala, c++, rust) no está soportada.

# ---------------------------------------------------------------------------------------------
# Tipo                      Tipo Python             Ejemplo
# ---------------------------------------------------------------------------------------------
# Numérico entero           int                     12
# Numérico real             float                   12.63
# Numérico complejo         complex                 4.8 - 2.4j
# Booleano                  bool                    True, False
# ---------------------------------------------------------------------------------------------
# Tipos de colecciones en Python
# ---------------------------------------------------------------------------------------------
# Cadena de texto           str                     'Mia', "Rouse"
# Rangos numéricos enteros  range                   range(8), range(3, 9), range(1, 24, 3)
# Listas                    list                    [5,6,9]
# Conjuntos                 set                     {4, 6, 7}
# Tuplas                    tuple                   (2,3,4,8)
# Diccionarios              dict                    {"Mar": 28, "Carla": 23}
# Generadores               generator               (n for n in range(9))

# ---------------------------------------------------------------------------------------------
# Ejemplos de tipos de variables en Python
# ---------------------------------------------------------------------------------------------

# Variable numérica entera
numero = 21
print("numero", numero, "tipo", type(numero))

# Variable numérica coma flotante
altura = 1.83
print("altura", altura, "tipo", type(altura))

# Variable numérica compleja
base = 7.4 + 48.6j
print("base", base, "tipo", type(base))

# Variable booleana
mayor = True
print("mayor", mayor, "tipo", type(mayor))

# Variable de tipo colección cadena de texto
provincia = "La Rioja"
print("provincia", provincia, "tipo", type(provincia))

# Variable de tipo colección de lista
lista = [4, 8, 1]
print("lista", lista, "tipo", type(lista))

# Variable de tipo colección de tupla
tupla_sin = 4, 8, 1 # Sin paréntesis
tupla_con = (5, 6, 3) # Con paréntesis
print("tupla_sin", tupla_sin, "tipo", type(tupla_sin))
print("tupla_con", tupla_con, "tipo", type(tupla_con))

# Variable de tipo colección de conjunto
conjunto = {4, 8, 1}
print("conjunto", conjunto, "tipo", type(conjunto))

# Variable de tipo colección de diccionario
dicci = {"nombre": "Carla", "edad": 23}
print("dicci", dicci, "tipo", type(dicci))

# Variable de tipo colección de rango
rango = range(8)
rango = list(rango) # Aquí convertimos el rango en una lista para poder
                    # visualizar los valores del rango generado
print("rango", rango, "tipo", type(rango))

# Variable de tipo colección de generador
generador = (n for n in range(1, 10, 2))
print("generador", generador, "tipo", type(generador))
[print(n) for n in generador] # Visualizamos los valores del generador

# ---------------------------------------------------------------------------------------------
# Variables de tipo objeto
# ---------------------------------------------------------------------------------------------
class Gps(object):
    def __init__(self, latitud=0.0, longitud=0.0, altitud=0.0):
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud
    def __str__(self):
        return f"latitud: {self.latitud} longitud: {self.longitud} altitud: {self.altitud}"

# Variable 'posicion' de tipo objeto
posicion = Gps(1.3, 3.4, 12.8)
print("posicion", posicion, "tipo", type(posicion))

