# Definir una función denominada 'suma' que devuelva la suma de dos valores
def suma(primer_valor, segundo_valor):
    rdo = primer_valor + segundo_valor
    return rdo

s = suma(120, 600)
s_real = suma(120.67, 89.9)
s_cad = suma('Hola ', '¿cómo estás?')
print("Suma =>", s)
print("Suma =>", s_real)
print("Suma =>", s_cad)


# Definir una función denominada 'area' que devuelva el área de un círculo
# area_circulo = pi * radio al cuadrado
def area(radio):
    area_circulo = 3.14 * radio ** 2
    return area_circulo

def area_circulo(radio):
    return 3.14 * radio ** 2

# Definir una función denominada 'longitud' que devuelva el número de caracteres de una cadena de texto
def longitud(texto):
    caracteres = 0
    for c in texto:
        caracteres += 1
    return caracteres

long = longitud('Hola')
print(long)

# Definir una función denominada 'mayor' que devuelva True si la edad es mayor de 17 o False en caso contrario
def mayor(edad):
    return edad > 17

def mayor2(edad):
    if edad > 17:
        return True
    return False

def mayor3(edad):
    return True if edad > 17 else False

# Definir una función denominada 'sumas' que recibe un valor de entrada indicando el
# número de veces que se pedirá por teclado un número, y la función devolverá la suma
# de todos los números introducidos
def sumas(numeros_a_introducir):
    suma = 0
    for n in range(numeros_a_introducir):
        suma += int(input("Número: "))
    return suma

def sumas2(numeros_a_introducir):
    suma = 0
    while numeros_a_introducir != 0:
        suma += int(input("Número: "))
        numeros_a_introducir -= 1
    return suma

rdo = sumas(4)
print("La suma es =>", rdo)

