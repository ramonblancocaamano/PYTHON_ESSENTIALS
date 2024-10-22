'''
Realizar un programa que solicite por teclado valores numéricos enteros hasta que se introduzca el '0' y, mostrar en pantalla
una lista con todos los números introducidos que no sean repetidos.
'''
numbers = []
while True:
    number = int(input('Enter a number: '))
    if number == 0: break
    numbers.append(number)

print(list(set(numbers)))
