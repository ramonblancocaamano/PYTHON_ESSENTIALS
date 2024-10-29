'''
Realizar un programa que muestre el sumatorio de todos los múltiplos de 3 encontrados entre el 20 y el 370.
'''

sumatorio = 0
for k in range(20, 370):
    if k % 3 == 0:
        sumatorio += k
print('sumatorio =>', sumatorio)
