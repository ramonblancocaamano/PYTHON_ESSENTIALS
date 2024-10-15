# Solicitar por teclado una frase y mostrar en pantalla,
# si la frase acaba en una vocal.
# Visualizar True si acaba en vocal en caso contrario False
frase = input("Frase: ")
#acaba = frase.endswith(('a', 'e', 'i', 'o', 'u')) # None
#print(acaba)

# Versión 2
print (frase[-1] in "aeiou")

# Versión 3
print (frase[-1].lower() in "aeiou")
