# ------------------------------------------------------------------------------------------
# Bucle for, se utiliza para recorrer colecciones
# ------------------------------------------------------------------------------------------
'''
Sintaxis:
for variable_de_buble in dato_iterable:
    sentencias del bucle
else:
    sentencias en caso de ruptura de la ejecución del bucle
'''
# ------------------------------------------------------------------------------------------

# Funcionalidad de range
# esta función devuelve una serie o lista o colección de valores
# Tiene tres formatos
# - range(8)            # 0, 1, 2, 3, 4, 5, 6, 7
# - range(87, 93)       # 87, 88, 89, 90, 91, 92
# - range(87, 93, 2)    # 87, 89, 91

rango = range(80, 23, -4)
#print(list(rango))
#print("Número de elementos=>", len(rango))


# Muestra en pantalla todos los valores entre 0 y 9, ambos inclusive
for n in range(10): # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    print(n)

print("-" * 100)

# Muestra en pantalla todos los numeros entre 23 y 48, ambos inclusive
for n in range(23, 49):
    print(n)

print("-" * 100)

# Mostrar en pantalla los primeros 'n' números impares
n = int(input('Número '))
for b in range(1, n * 2, 2):
    print(b)

print("-" * 100)

texto = "caracola"
for c in texto:
    print(c)
