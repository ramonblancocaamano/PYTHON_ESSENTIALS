# ------------------------------------------------------------------------------------------
# Sentencia if ternaria
# ------------------------------------------------------------------------------------------
# Sintáxis de la if ternaria de Python
# valor if condición else valor

precio = 235

tipo_de_iva = 4 if precio == 189 else 21

if precio < 189:
    tipo_de_iva = 4
else:
    tipo_de_iva = 21

print(tipo_de_iva)
