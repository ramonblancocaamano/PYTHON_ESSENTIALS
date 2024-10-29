# ------------------------------------------------------------------------------------------
# Funciones de orden superior en Python
# ------------------------------------------------------------------------------------------

# Función de orden superior que recibe como primer parámetro una función
# y los restantes parámetros representan valores que se le enviarán a la función
def operation(funcion_de_entrada, param1, param2):
    return funcion_de_entrada(param1, param2)

def function(func, *args, **kwargs):
    return func(*args, **kwargs)

def multiply(r, m=9):
    return r * m

def divide(u, m):
    return u // m

def restar():
    return 0

def longis(text1, text2):
    return len(text1) > len(text2)

multiplicar = operation(multiply, 7, 6)
es_mayor = operation(longis, 'Java', 'Python')
caracteres = operation(lambda x, y: len(x)+ len(y), 'Java', 'Python')
print(caracteres)


def sum_lengths(*words, **key_words):
    suma = sum([len(word) for word in words]) if len(words) > 0 else 0
    suma2 = sum([len(word) for word in key_words.values()]) if len(key_words) > 0 else 0
    return suma + suma2

multiplicar = operation(multiply, 8, 6)
dividir = operation(divide, 78, 4)
sum_length_words = function(sum_lengths, 'Python', 'Java', s='Scala', j='Julia')

print(multiplicar)
print(dividir)
print(sum_length_words)

print('-' * 90)

#----------------------------------------------------------------------

# Función de orden superior que devuelve una función
def calc(type=0):
    if type == 1:
        return multiply
    elif type == 2:
        return divide
    return function

multiplicar = calc(1)
dividir = calc(2)
funcion = calc()

print(multiplicar(3, 4))
print(dividir(23, 5))
print(funcion(sum_lengths, 'Python', 'Java', s='Scala', j='Julia'))

print('-' * 90)

print(calc(1)(3, 4))
print(calc(2)(23, 5))
print(calc()(sum_lengths, 'Python', 'Java', s='Scala', j='Julia'))
