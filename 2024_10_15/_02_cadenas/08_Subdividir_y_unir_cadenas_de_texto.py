# ------------------------------------------------------------------------------------------
# Subdividir y unir cadenas de texto
# ------------------------------------------------------------------------------------------

# Dividir una cadena en subcadenas según un determinado carácter o caracteres
frase = 'esta-es-una-frase-a-subdividir'
print("split=>", frase.split('-'))

frase = 'esta<->es<->una<->frase<->a<->subdividir'
print("split=>", frase.split('<->'))

frase = 'esta-es---una--frase--a-----subdividir'
print("split=>", frase.split('-'))

frase = '  '
print("split2=>", frase.split(' '))
print('-' * 80)

# Devuelve una lista como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = ['1', '2', '3', '4', '5']
print("join =>", ", ".join(numeros))

# Devuelve un conjunto como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = {'1', '2', '3', '4', '5'}
print("join =>", "<=>".join(numeros))

# Devuelve una cadena como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
frase = 'nueva frase'
print("join =>", "-".join(frase))

print('-' * 80)

frase = "       esta      frase      tiene     muchos     espacios   "
texto_sin_espacios = frase.strip()
print('texto_sin_espacios =>', texto_sin_espacios)
print(texto_sin_espacios.split())

datos = [g for g in frase.split() if len(g) > 0]
rdo = " ".join(datos)
print(rdo)

