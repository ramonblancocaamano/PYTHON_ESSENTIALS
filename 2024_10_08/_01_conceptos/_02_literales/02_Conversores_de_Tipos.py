# ------------------------------------------------------------------------------------------
# Conversores de tipos numéricos (int, float, complex)
# ------------------------------------------------------------------------------------------

numero = "13"

numero_int = int(numero) # Convertir a tipo numérico entero
numero_binario = bin(numero_int) # Convertir a tipo numérico entero en base binaria
numero_octal = oct(numero_int) # Convertir a tipo numérico entero en base octal
numero_hexa = hex(numero_int) # Convertir a tipo numérico entero en base hexadecimal
numero_float = float(numero) # Convertir a tipo numérico coma flotante
numero_complex = complex(numero) # Convertir a tipo numérico complejo

# ------------------------------------------------------------------------------------------
# Conversores de tipos booleanos
# ------------------------------------------------------------------------------------------

numero = "0"
verdadero = bool(numero) # Convertir a tipo booleano

# ------------------------------------------------------------------------------------------
# Conversores de tipos _02_cadenas de texto
# ------------------------------------------------------------------------------------------

numero = 196
numero_texto = str(numero) # Convertir a tipo cadena de texto
numero_char = chr(numero) # Convertir a tipo cadena de texto
valor_letra = ord("A") # Devuelve el valor del caracter 'A'

palabra = "mañana" # Formato cadena de texto 'iso-8859-1'
nueva = palabra.encode(encoding="utf-8") # Convertir a formato cadena de texto 'utf-8'
palabra = nueva.decode(encoding="utf-8") # Convertir a formato cadena de texto 'iso-8859-1'

