# ------------------------------------------------------------------------------------------
# Las funciones también pueden contener funciones internas
# ------------------------------------------------------------------------------------------

def suma_doble(numeros):

    def suma():
        suma = 0
        for n in numeros:
            suma += n
        return suma

    if len(numeros) > 0:
        return suma() * 2
    return 0


rdo = suma_doble([10, 20])
print("suma_doble =>", rdo)

print('-' * 80)


def suma_caracteres(palabras):
    caracteres = 0

    def longitud(palabra):
        return len(palabra)

    for palabra in palabras:
        caracteres += longitud(palabra)

    return caracteres


idiomas = ['inglés', 'francés', 'italiano']

letras = {'x' * n for n in range(4, 10)}

rdo1 = suma_caracteres(['java', 'python', 'c++'])
rdo2 = suma_caracteres(idiomas)
rdo3 = suma_caracteres(letras)
print('suma_caracteres =>', rdo1)
print('suma_caracteres =>', rdo2)
print('suma_caracteres =>', rdo3)

