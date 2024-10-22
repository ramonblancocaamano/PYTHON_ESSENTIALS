# ------------------------------------------------------------------------------------------
# Sentencias de control de bucles (for, while)
# ------------------------------------------------------------------------------------------

# ------------------------------------------------------------------------------------------
# La sentencia 'break', se utiliza para la ruptura de la ejecución de un bucle,
# cuando se produce alguna condición especial.
# ------------------------------------------------------------------------------------------

# Ejemplo uso de 'break' en un bucle 'for'
numero = int(input("Introduzca un número: "))
for n in range(100):
    if numero == n:
        print("Has acertado el número")
        break

print("-" * 100)

# Ejemplo uso de 'break' en un bucle 'while'
pares = 0
impares = 0
while True:
    numero = int(input("Introduzca un número: "))
    if numero == 0:
        break
    if numero % 2 == 0:
        pares += 1
    if numero % 2 == 1:
        impares += 1

print("Números pares", pares)
print("Números impares", impares)

print("-" * 100)

# ------------------------------------------------------------------------------------------
# Sentencia 'continue', se utiliza para saltar a la siguiente iteración sin ejecutar
# el código restante dentro del bucle
# ------------------------------------------------------------------------------------------

# Ejemplo uso de 'continue' en un bucle 'for'
for n in range(1, 100):
    if n % 2 == 0:
        continue
    print(n)

print("-" * 100)

# Ejemplo uso de 'continue' en un bucle 'while'
contador = 0
while True:
    numero = int(input("Introduzca un número: "))
    if numero <= 0:
        break
    if numero == 17:
        continue
    contador += 1

print(contador)
