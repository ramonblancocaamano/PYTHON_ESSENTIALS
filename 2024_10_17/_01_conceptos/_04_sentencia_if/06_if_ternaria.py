# ------------------------------------------------------------------------------------------
# Sentencia if ternaria
# ------------------------------------------------------------------------------------------
# Sintáxis de la if ternaria de Python
# valor if condición else valor

precio = 189

tipo_de_iva = 4 if precio == 189 else 21  # (2 > 1 ? 8 : 9)

if precio < 189:
    tipo_de_iva = 4
else:
    tipo_de_iva = 21

print(tipo_de_iva)

cp = '08000'
cp = 'Barcelona' if cp == '08002' else 'Otra provincia'
print(cp)
