# ------------------------------------------------------------------------------------------
# Funciones en Python
# ------------------------------------------------------------------------------------------

# Cualquier función tendrá un nombre, unos argumentos o parámetros de
# entrada, un código a ejecutar y unos valores de salida.

# Todas las funciones en Python devuelven un valor, de manera implícita o explícita.
# ------------------------------------------------------------------------------------------

# Una función sin parámetros de entrada ni valores de salida.
def primera():
    print('Primera función en Python')

x = primera()
print("x=>", x)
print('-' * 80)

a = 67
b = 89

# Una función con dos parámetros de entrada y devuelve un valor
def resta(a, b):
    a += 3
    rdo = a - b
    return rdo

restar = resta(10, 3)
print("Resta =>", restar)
print("a=>",a, "b=>", b)

resta_2 = resta(8)

print('-' * 80)

# Función que devuelve un valor o ninguno 'None'
def longitud(msg):
    caracteres = len(msg)
    if caracteres > 2:
        return caracteres


rdo1 = longitud('Mi nombre')
rdo2 = longitud('M')
rdo3 = longitud(75673)
print("rdo1 =>", rdo1)
print("rdo2 =>", rdo2)
print("rdo3 =>", rdo3)
