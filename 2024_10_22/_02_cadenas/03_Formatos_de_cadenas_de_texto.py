# ------------------------------------------------------------------------------------------
# Formatos de cadenas de texto
# https://docs.python.org/3/library/stdtypes.html#old-string-formatting
# ------------------------------------------------------------------------------------------
'''
# Utilizando el carácter '%'
numero = 5
cadena1 = "El número es %d decimal" % numero
cadena2 = "El número es " + str(numero) + " decimal"
print(cadena1)
print(cadena2)
nombre = "Ana Manuela"
edad = 28
datos = "Nombre: %s, Edad: %d, Mayor: %f" % ('Ana', edad, 1.78)
print(datos)

nombre = "Ana Manuela"
mayor = True
datos = "Nombre: %s, Mayor: %s" % (nombre, mayor)
print(datos)

print('-' * 80)

edad = 9
'''
# Utilizando la función 'format' de la clase 'str'
s = "Los números son {} y {}, la suma es {}".format(5, 10, 15)
print(s)

s = "Los números por posición son {1} y {0}".format(5, 10)
print(s)
n = "Lucas"
s = "Los números son {u} y {w} de {n}".format(w=35, u=13, n=n)
print(s)

print('-' * 80)


def suma(a, b):
    return a + b

# Utilizando cadenas literales (f) o (F)
a = 50
b = 100
s = f"Los números son {a} y {b}"
print(s)

s = F"La suma de {a} y {b} es { a + b }"
print(s)

x = 200
y = 400
s = f"El resultado de la función es {suma(x, y)}"
print(s)
