# ------------------------------------------------------------------------------------------
# Reemplazar cadenas de texto
# ------------------------------------------------------------------------------------------

# Elimina por la izquierda el caracter que se le indica, si se llama sin
# parámetros elimina el espacio en blanco
frase = 'rrrrrrrHorla'
print("lstrip =>", frase.lstrip('r'))

frase2 = 'rrrrrmrrggggggggHorla'
print("lstrip2 =>", frase2.lstrip('grHo'))


# Elimina por la derecha el caracter que se le indica, si se llama sin
# parámetros elimina el espacio en blanco
frase = 'Holaxxxxxxxxx'
print("rstrip =>", frase.rstrip('x'))

# Elimina por la izquierda y derecha el caracter que se le indica, si se
# llama sin parámetros elimina el espacio en blanco
frase = 'xxxxxxxxxxwwwwxxxxxxxxxwww'
print("strip vacio =>", frase.strip('xw'))

print('-' * 80)

# Rellena con ceros una cadena por la izquierda con una determinada longitud
cad = 'nueva'
print("zfill =>", cad.zfill(1))

print('-' * 80)

# Reemplazar caracteres de una cadena por otros caracteres
frase = 'frase para utilizar en el reemplazo'
print("replace=>", frase.replace('para', 'PARA'))
