# ------------------------------------------------------------------------------------------
# Programación funcional en Python: Función 'filter'
# ------------------------------------------------------------------------------------------

lenguajes = ['python', 'Java', 'scala', 'julia', 'Javascript']

def only_j(name):
    return name.lower().startswith('j')

filtro = list(filter(lambda text: len(text) > 4, lenguajes))
print(filtro)

filtro = list(filter(only_j, lenguajes))
print(filtro)
