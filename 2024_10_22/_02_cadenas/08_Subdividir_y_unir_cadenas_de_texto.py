# ------------------------------------------------------------------------------------------
# Subdividir y unir cadenas de texto
# ------------------------------------------------------------------------------------------

# Dividir una cadena en subcadenas según un determinado carácter o caracteres
frase = 'esta-es-una-frase-a-subdividir'
print("split=>", frase.split('-'))

frase = 'esta<->es<->una<->frase<->a<->subdividir'
print("split=>", frase.split('<->'))

frase = 'esta-es---una--frase--a-----subdividir'
tokens = [elemento for elemento in frase.split('-') if len(elemento) > 0]
print("split2=>", tokens)

frase = 'Devuelve una lista como una cadena'
print("split2=>", frase.split('a'))
print('-' * 80)



# Devuelve una lista como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = '1', '2', '3', '4', '5'
cadena = ", ".join(numeros)
print(type(cadena))
print("join =>", cadena)
cadena2 = ":".join( str(h) for h in range(9) )
print("join cadena2 =>", cadena2)

# Devuelve un conjunto como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
numeros = {'1', '2', '3', '4', '5'}
print("join =>", "<=>".join(numeros))

# Devuelve una cadena como una cadena de caracteres unida por el carácter
# o caracteres de la cadena especificada, por medio de la función 'join'
frase = 'nueva frase'
print("join =>", "-".join(frase))

print('-' * 80)

frase = "------esta-----frase--tiene---muchos----espacios----"
'''texto_sin_espacios = frase.strip()
print('texto_sin_espacios =>', texto_sin_espacios)
print(texto_sin_espacios.split())

datos = [g for g in frase.split() if len(g) > 0]'''
print(frase.strip('-').split('-'))
rdo = " ".join( g for g in frase.strip('-').split('-') if len(g) > 0 )
print(rdo)
