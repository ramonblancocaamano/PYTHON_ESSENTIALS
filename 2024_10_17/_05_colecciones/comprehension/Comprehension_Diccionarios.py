# Ejemplo de for comprehension para crear colecciones de tipo diccionario (dict)

lenguajes = ['Python', 'Java', 'c++', 'Go', 'JavaScript', 'PHP']

diccionario = { t : len(t) for t in lenguajes if t != 'Go' }
print(diccionario)

diccionario = dict( (t, len(t)) for t in lenguajes    )
print(diccionario)

