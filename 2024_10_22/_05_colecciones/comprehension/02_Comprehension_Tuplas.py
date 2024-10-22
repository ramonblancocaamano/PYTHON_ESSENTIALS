# ------------------------------------------------------------------------------------------
# Ejemplo de for comprehension para crear colecciones de tipo tuplas (tuple)
# ------------------------------------------------------------------------------------------

# for comprehension que genera una colección de tipo tupla
dobles = tuple( n * 2 for n in range(1, 10, 2) if n != 1 and n > 2 ) #1,3,5,7,9
print(dobles)

