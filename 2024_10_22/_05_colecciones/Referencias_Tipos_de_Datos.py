# Datos por valor
a = 23
n = a
a = 13
print(a)
print("Posición de memoria de a", id(a))
print("Posición de memoria de n", id(n))

print('=' * 100)

# Datos por referencia
n1 = [3,4,4,4,4]
print("Posición de memoria de n1", id(n1))
n2 = n1
n3 = n2
print("Posición de memoria de n2", id(n2))
print(n1)
print(n2)
print(id(n1))
print(id(n2))
n2.append(7)
n1.append(99)
print(n1)
print(n2)
