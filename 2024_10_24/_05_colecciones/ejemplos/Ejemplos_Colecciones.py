# Tipos de coleccione ess Python
# - Listas
# - Conjuntos
# - Tuplas
# - Diccionarios

# Ejemplo de lista
numeros = [2,2,3,4,5]
diferentes = [2.8, False, 'texto', 23, 4.5-6.7j, None]

vacia= []

lista = list()
lista.append(2)
lista.append("Lola")
lista.append(4.5)
print(lista)

texto = 'mi frase'
nums = [n for n in texto]
print(nums)

una = [1,2,3]
dos = [6,7,8]
tres = una + dos
print(tres)

cuatro = una.copy()
cuatro.append(13)
print("una =>", una)

matriz = [
    [ 3, 4 ],
    [ 6, 5, [9, 3] ]
]
copia = matriz.copy()
print(copia)
# -----------------------------------------------
# Conjuntos
conju = {3,4,4,5,5,6}  # set()
print(conju)

# Tuplas
tupla = (3,4,5,6,7,78,7) # tuple()

# Diccionarios
dic = {"a": 24} # dict()
