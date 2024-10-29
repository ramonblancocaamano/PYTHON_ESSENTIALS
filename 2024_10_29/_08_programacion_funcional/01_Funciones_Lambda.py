# ------------------------------------------------------------------------------------------
# Funciones lambda en Python
# ------------------------------------------------------------------------------------------

def es_mayor(number):
    return number > 17

alturas = [1.78, 1.94, 1.84, 1.65, 1.89]
edades = {'a':23, 'c':45, 'k':27, 'u':31}

# Función lambda que devuelve la suma de dos valores
suma = lambda a, b: a + b

# Función lambda que comprueba si el valor es mayor que 17
mayor = lambda x: es_mayor(x)


# Función lambda que devuelve el sumatorio de una lista de valores
sumatorio = lambda *values: sum(values) if len(values) > 0 else 0

# Función lambda que devuelve el sumatorio de los valores de una colección tipo 'dict' (diccionario)
suma_claves = lambda **dictionary: sum(dictionary.values()) if len(dictionary.values()) > 0 else 0

if __name__ == '__main__':
    try:
        print('Función lambda suma', suma(8,5))
        print('Función lambda mayor', mayor(24))
        print('Función lambda sumatorio', sumatorio(8,7,7,5,4,4,3,5,6,6))
        print('Función lambda suma_claves', suma_claves(c=9,v=7,n=4,y=3))
    except:
        pass
    print('=' * 80)

    print('Función lambda sumatorio', sumatorio(*alturas))
    print('Función lambda suma_claves', suma_claves(**edades))

