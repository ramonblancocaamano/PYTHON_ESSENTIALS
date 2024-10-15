import random

numbers = [random.randint(0, 100) * 1.1 for _ in range(20)]
print(numbers)

# Ordenación de una lista utilizando el método Bubble Sort
def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for k in range(0, n - i - 1):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]

# Ordenación de una lista utilizando el método Quick Sort
def quickSort(array):
    if len(array) > 1:
        value = array[len(array) // 2]
        left = [v for v in array if v < value]
        middle = [v for v in array if v == value]
        right = [v for v in array if v > value]
        return quickSort(left) + middle + quickSort(right)
    else:
        return array



#numbers.sort(reverse=True)
#print(numbers)

#bubbleSort(numbers)
#print(numbers)

#numbers = quickSort(numbers)
#print(numbers)

ciudades = ['Girona', 'Alacant', 'Burgos', 'barcelona', 'Palencia', 'Jaén', 'Ceuta']

ciudades.sort()
print(ciudades)

# Ordenar la lista 'ciudades' en función de la longitud del número de
# caracteres de la ciudad
ciudades.sort(key=lambda x: len(x))
print(ciudades)

tuplas = [(4, 6, 'x'), (1, 2, 'b'), (3, 8, 's'), (0, 5, 'm'), (5, 6, 'k')]

# Ordenar la lista 'tuplas' en función del tercer elemento de la tupla
tuplas.sort(key=lambda x: x[1], reverse=True)
print(tuplas)

registro = [
            {"edad": 26, "altura": 1.94},
            {"edad": 52, "altura": 1.82},
            {"edad": 17, "altura": 1.78},
            {"edad": 31, "altura": 1.73}
           ]

# Ordenar la lista 'registro' en función del campo 'altura' y en orden descendente
registro.sort(key=lambda x: x['edad'])
print(registro)

persons =  [
            {"edad": 26, "altura": 1.94, "nombre": "Luisa", "ciudad": "Cáceres"},
            {"edad": 42, "altura": 1.82, "nombre": "Luisa", "ciudad": "Cáceres"},
            {"edad": 17, "altura": 1.78, "nombre": "Carla", "ciudad": "Málaga"},
            {"edad": 31, "altura": 1.73, "nombre": "Mía", "ciudad": "Barcelona"}
           ]

def persona(dato, keys):
    pass

# Ordenar la lista 'persons' en función de los campos 'ciudad', 'nombre' y 'altura'
fields = ['edad', 'altura']
keys = persons[0].keys()
persons.sort(key=lambda person: tuple(person[f.lower()] for f in fields if f.lower() in keys))
print(persons)
