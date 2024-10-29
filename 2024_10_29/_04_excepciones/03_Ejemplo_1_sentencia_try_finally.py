try:
    y = 1 / 0
except ZeroDivisionError:
    print("¡División entre Cero!")
finally:
    print('Este código siempre se ejecuta')

print("FIN.")