# Ejemplo de for comprehension para crear colecciones de tipo lista (list)

lenguajes = ['Python', 'Java', 'c++', 'Go', 'JavaScript', 'PHP']

# Sintáxis: [ valor_elemento for variable_bucle_for in tipo_de_coleccion [condición o filtro] ]

numeros_pares = [numero for numero in range(2, 51, 2)]
print(numeros_pares)

nuevos = [xc for xc in lenguajes if xc.startswith('J')]
print(nuevos)

nuevos = []
for xc in lenguajes:
    if xc.startswith('J'):
        nuevos.append(xc)
print(nuevos)
