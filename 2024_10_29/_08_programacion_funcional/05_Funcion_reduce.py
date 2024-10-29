# ------------------------------------------------------------------------------------------
# Programación funcional en Python: Función 'reduce'
# ------------------------------------------------------------------------------------------

from functools import reduce

numbers = [1, 3, 5, 6, 2]

def multiplicar(primero, segundo):
    return primero * segundo

def sumar(o, y):
    return o + y

# Operación reduce que calcula el valor máximo de una lista
maximo = reduce(lambda a, b: a if a > b else b, numbers, 0)
print(maximo)

# Operación reduce que calcula la multiplicación de todos los valores de una lista
multiplica = reduce(multiplicar, numbers)
print('multiplica =>', multiplica)

sumatorio = reduce(sumar, numbers,0)
print(sumatorio)

# Operación reduce para aplanar una lista bidimensional
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(reduce(lambda x, y: x + y, matrix))

# Operación reduce que calcula cuantos números son pares en una lista
values = [26, 4, 12, 43, 19, 71, 20]
print(reduce(lambda acc, num: acc + 1 if num % 2 == 0 else acc, values, 0))

print('=' * 90)

# ------------------------------------------------------------------------------------------
# Operaciones 'reduce' con diccionarios
# ------------------------------------------------------------------------------------------

# Ejemplo 1
names = ['Xoan', 'Mia', 'Lolo', 'Ana', 'Rodrigo']

def transform(accumulate, name):
    accumulate[name] = len(name)
    return accumulate

results = reduce(transform, names, {})
print(results)

print('=' * 90)

# ------------------------------------------------------------------------------------------

# Ejemplo 2
list_of_attendees = [
    {"email": "alex@example.com", "name": "Alex", "status": "attending"},
    {"email": "brian@example.com", "name": "Brian", "status": "declined"},
    {"email": "carol@example.com", "name": "Carol", "status": "pending"},
    {"email": "derek@example.com", "name": "Derek", "status": "attending"},
    {"email": "ellen@example.com", "name": "Ellen", "status": "attending"}
]

def transform_data(accumulate, invitee):
    accumulate[invitee["email"]] = invitee["status"]
    return accumulate

invitados = reduce(transform_data, list_of_attendees, {})
print(invitados)

print('=' * 90)
# ------------------------------------------------------------------------------------------

# Ejemplo 3
list_of_attendees = [
    {"name": "Zeke",
     "vegan": True,
     "brought_guests": True,
     "guests": [
         {"name": "Amanda", "vegan": False},
         {"name": "Wayne", "vegan": True}
     ]
    },
    {"name": "Xavier",
     "vegan": True,
     "brought_guests": False
    },
    {"name": "Yohanna",
     "vegan": False,
     "brought_guests": True,
     "guests": [
         {"name": "Lily", "vegan": True},
         {"name": "Stefano", "vegan": True}
     ]
    },
    {"name": "Kael",
     "vegan": False,
     "brought_guests": False
    },
    {"name": "Landon",
     "vegan": True,
     "brought_guests": False
    },
]

# Calcular el número de asistentes que trajeron invitados y el número total de invitados
def derive_guest_count(accumulate, attendee):
    accumulate["total_guests"] += 1
    if attendee["brought_guests"]:
        accumulate["guest_who_brought_guests"] += 1
        accumulate["total_guests"] += len(attendee["guests"])
    return accumulate

results = reduce(
    derive_guest_count,
    list_of_attendees,
    {
       "guest_who_brought_guests": 0,
       "total_guests": 0
    }
)

print(results)

print('=' * 90)
# ------------------------------------------------------------------------------------------

# Ejemplo 4

# Calcular el número de asistentes que son veganos y no veganos

def derive_vegan_info(accumulate, attendee):
    if attendee["vegan"]:
        accumulate["vegan"] += 1
    else:
        accumulate["non_vegan"] += 1
    if attendee.get("brought_guests"):
        for guest_brought in attendee["guests"]:
            # Check guests recursively
            accumulate = derive_vegan_info(accumulate, guest_brought)
    return accumulate

results = reduce(derive_vegan_info, list_of_attendees, {"vegan": 0, "non_vegan": 0})
print(results)
