'''
   Realizar un programa que solicite por teclado un tiempo expresado en segundos y que escriba ese tiempo en horas, minutos y segundos.

    Ejemplo:
    -------------------------------------------
    Tiempo en segundos: 42100
    Se muestra: 11 h 41 m 40 s
'''

tiempo_segundos = int(input('Tiempo en segundos: '))

horas = tiempo_segundos // 3600
resto_segundos = tiempo_segundos % 3600
minutos = resto_segundos // 60
segundos = resto_segundos % 60

print(tiempo_segundos, 'segundos son', horas, 'h', minutos, 'm', segundos, 's')
