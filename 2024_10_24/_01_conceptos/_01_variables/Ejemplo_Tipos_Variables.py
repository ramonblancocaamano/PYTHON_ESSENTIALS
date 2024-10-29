numero_entero = 5
numero_coma_flotante = 4.5
numero_complejo = 5+7j
valor_booleano = True
coleccion_lista = []
coleccion_conjunto = {2,3,4,4}
coleccion_tupla = (2,3,4,4)
coleccion_diccionario = { "Nombre": "Ana", "Edad": 35}

print(type(numero_entero))
print(type(coleccion_diccionario))

if type(coleccion_diccionario) == dict:
    print("El tipo de dato es entero")

if coleccion_conjunto == coleccion_tupla:
    print("Son iguales")
else:
    print("No son iguales")

