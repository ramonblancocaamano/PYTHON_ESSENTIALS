# ------------------------------------------------------------------------------------------
# Las cadenas en Python o strings son un tipo inmutable que permite almacenar
# ------------------------------------------------------------------------------------------

# Para obtener subcadenas de una cadena de texto se utilizarán por medio de los
# índices posicionales de los caracteres de la cadena de texto

cadena_de_texto = "obtener subcadenas de una cadena de texto"

# Obtener subcadenas por medio de índices por posición

caracter = cadena_de_texto[0]
print("caracter=>", caracter)

palabra_inicio = cadena_de_texto[27 : 7 : 1]
print("palabra inicio (1)=>", palabra_inicio)

palabra_inicio = cadena_de_texto[:7]
print("palabra inicio (2)=>", palabra_inicio)

numero_caracteres = len(cadena_de_texto)
desde_posicion = numero_caracteres - 13

resto_frase = cadena_de_texto[desde_posicion : numero_caracteres]
print("resto frase (1)=>", resto_frase)

resto_frase = cadena_de_texto[desde_posicion : ]
print("resto frase (2)=>", resto_frase)

caracteres_varios = cadena_de_texto[3 : 23 : 3]
print("caracteres varios (1)=>", caracteres_varios)

caracteres_varios = cadena_de_texto[23 : 3 : -3]
print("caracteres varios (2)=>", caracteres_varios)

toda_la_frase = cadena_de_texto[::]
print("toda la frase=>", toda_la_frase)

cadena_invertida = cadena_de_texto[::-1]
print("cadena invertida=>", cadena_invertida)

# Obtener subcadenas por medio de índices por posición negativos

un_caracter = cadena_de_texto[-5]
print("un caracter=>", un_caracter)

varios_caracteres = cadena_de_texto[-8 : -3]
print("varios caracteres (1)=>", varios_caracteres)

varios_caracteres = cadena_de_texto[-8:]
print("varios caracteres (2)=>", varios_caracteres)

varios_caracteres = cadena_de_texto[ : -8] # cadena de texto
print("varios caracteres (3)=>", varios_caracteres)

letras = cadena_de_texto[-21 : -3 : 3] # cadena de texto mas 'larga que la anter'ior
                                       # lgq  t
print("letras (1)=>", letras)

letras = cadena_de_texto[-3 : -13 : -3] # ca'dena de te'xto
print("letras (2)=>", letras)

texto = "Rosana"
for n in range(len(texto)): # 0, 1, 2, 3, 4, 5
    print(texto[n])

print("=" * 100)

for n in (3,2,1,5,4,0):
    print(texto[n])

print("=" * 100)

for n in texto:
    print(n)

texto[2]='y'
