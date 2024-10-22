# ------------------------------------------------------------------------------------------
# Sentencia if con múltiples condiciones
# ------------------------------------------------------------------------------------------

edad = int(input("Edad: "))

if edad > 0 and edad <= 10:
    print("Infantil")
elif edad > 10 and edad < 14:
    print("Alevín")
elif edad > 13 and edad < 18:
    print("Adolescente")
else:
    print("Es mayor")

