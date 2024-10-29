# Solicitar por teclado líneas de texto hasta que se introduzca una cadena vacía y,
# mostrar cuántas cadenas de texto superan los 6 caracteres

mas_de_6 = 0
while True:
    linea = input('Texto a introducir: ')
    if linea == '':
        break
    if len(linea) > 6:
        mas_de_6 += 1
print(f'Nº de líneas introducidas => {mas_de_6}')

