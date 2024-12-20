# ------------------------------------------------------------------------------------------
# Funciones recursivas
# ------------------------------------------------------------------------------------------

def factorial(n): # n=6    6! = 6.5.4.3.2.1
    if n < 2:
        return 1
    else:
        return n * factorial(n - 1)

print('Factorial =>', factorial(4))

print('-' * 80)

def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci =>", fibonacci(8)) # 0, 1, 1, 2, 3, 5, 8, 13, 21

print('-' * 80)

def sumatorio(n): # n=5 = 5 + 4 + 3 + 2 + 1
    return 1 if n < 2 else n + sumatorio(n - 1)

suma = sumatorio(5)
print("Sumatorio =>", suma)


# Función que devuelve una lista con todas las ocurriencias de una palabra en un texto
# proporcionado.

def ocurriencias(texto, palabra, palabras=[]):
    posicion = texto.lower().find(palabra.lower())
    if posicion == -1:
        return palabras
    else:
        word = texto[posicion : ]
        pos_final = word.find(' ')
        word = word[ : pos_final] if pos_final != -1 else word
        palabras.append(word)
        texto = texto[posicion + len(palabra) : ]
        return ocurriencias(texto, palabra, palabras)

texto = 'NUeva frase frase nuEVa Nueva'

print(ocurriencias(texto, 'NUEVA'))
