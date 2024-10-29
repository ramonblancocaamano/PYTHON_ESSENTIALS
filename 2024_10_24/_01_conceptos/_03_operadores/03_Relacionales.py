# ------------------------------------------------------------------------------------------
# Tipos de operadores relacionales
# Los operadores relacionales se utilizan en expresiones booleanas o condiciones.
# Las condiciones realmente son expresiones booleanas que se utilizan principalmente
# en las sentencias 'if' y 'while' de Python
# NOTA: Todos los operadores relacionales devuelven un valor booleano
# ------------------------------------------------------------------------------------------

# Operadores relacionales       Tipo de relación
# ------------------------------------------------------------------------------------------
#       >                       Mayor que
#       <                       Menor que
#       >=                      Mayor que o igual a
#       <=                      Menor que o igual a
#       !=                      Distinto de
#       ==                      Igual a
#       in                      Está en
#       is                      Si hace referencia al mismo objeto

numeros = [3,4,5] # Lista de valores numéricos enteros

# Expresión booleana Mayor que
mayor_que = 17 > 18
print("mayor que", mayor_que)

# Expresión booleana Mayor que o igual a
mayor_que_igual = 16 >= 7
print("mayor que o igual a", mayor_que_igual)

# Expresión booleana Menor que
menor_que = 17 < 18
print("menor que", menor_que)

# Expresión booleana Menor que o igual a
menor_que_igual = 6 <= 7
print("menor que o igual a", menor_que_igual)

# Expresión booleana Igual a
igual = 23 == 89
print("igual a", igual)

# Expresión booleana Distinto de
distinto = 23 != 89
print("distinto de", distinto)

# Expresión booleana Está en
hay_valor = 4 in numeros
print("está en", hay_valor)

nombre = "Rosale"
hay_vocal_e = "e" in nombre
print("hay vocal e", hay_vocal_e)

# Expresión booleana Si hace referencia al mismo objeto
primero = 10
segundo = 10
iguales = primero is segundo
print("iguales", iguales)
print("primero", id(primero))
print("segundo", id(segundo))

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
print(lista_a == lista_b) # True
print(lista_a is lista_b) # False
print("lista_a", id(lista_a))
print("lista_b", id(lista_b))