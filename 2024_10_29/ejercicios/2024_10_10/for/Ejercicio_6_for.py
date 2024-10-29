'''
Realizar un programa que muestre en pantalla todos los años bisiestos que hay entre 1900 y 2024 ambos inclusive.
'''

for anho in range(1900, 2025):
    if anho % 4 == 0 and (anho % 100 != 0 or anho % 400 == 0):
        print(anho)
