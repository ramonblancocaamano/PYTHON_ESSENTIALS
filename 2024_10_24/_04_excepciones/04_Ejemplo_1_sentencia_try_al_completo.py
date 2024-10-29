try:
    y = int(input('Numero: '))
except ZeroDivisionError:
    print("¡División entre Cero!")
else:
    print('Se ejecuta el código del else')
finally:
    print('Se ejecuta el código del finally')

print("FIN.")