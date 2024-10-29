# ------------------------------------------------------------------------------------------
# Ejemplo de for comprehension para crear colecciones de tipo lista (list)
# ------------------------------------------------------------------------------------------

lenguajes = ['Python', 'Java', 'c++', 'Go', 'JavaScript', 'PHP']

# Sintáxis: [ valor_elemento for valor_elemento in tipo_de_coleccion [condición o filtro] ]

numeros_pares = [numero for numero in range(1, 51) if numero % 7 != 0]
print(numeros_pares)
numeros_pares = []
for numero in range(1, 51):
    if numero % 7 != 0:
        numeros_pares.append(numero)


nuevos = [xc for xc in lenguajes if xc.startswith('J')]
print(nuevos)

nuevos = []
for xc in lenguajes:
    if xc.startswith('J'):
        nuevos.append(xc)
print(nuevos)
