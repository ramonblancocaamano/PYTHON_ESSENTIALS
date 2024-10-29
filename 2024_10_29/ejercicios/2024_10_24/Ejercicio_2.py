'''
Ejercicio número 2
------------------------------------------------------------------------------------------------------------------------------------------------------
Definir una función que recibe dos valores de entrada, el primer valor corresponde al número de datos de mujeres y el segundo valor corresponde
al número de datos de hombres, utilizar los siguientes datasets: 'nombres.data', 'apellidos.data', 'provincias.data', 'poblaciones.data'.
La función devolverá una lista con todos los datos generados tanto de hombres como mujeres.
Utilizar los módulos oportunos del paquete 'api' del proyecto.

Esquema de los datos a generar para hombres y mujeres es el siguiente:
nombre apellido1 apellido2|sexo|nif|provincia|poblacion|cp|fecha de nacimiento|número de móvil|número de fax|email
Los datos generados por cada persona se guardarán como un diccionario.

- El nombre y apellidos de la persona se generará aleatoriamente utilizando los datasets de 'nombres.data' y 'apellidos.data'
- El sexo de la persona ya viene indicado por el nombre de la persona
- La provincia se obtendrá aleatoriamente del dataset 'provincias.data'
- La población se obtendrá aleatoriamente del dataset 'poblaciones.data' en función de la provincia obtenida anteriormente
- El código postal se generará aleatoriamente con el siguiente esquema:
  código de la provincia más un número de tres dígitos generado aleatoriamente
  El código postal deberá tener una longitud de 5 dígitos numéricos. Ejemplo: 08546
- El nif se generará aleatoriamente, hay que tener en cuenta que los nifs no se pueden repetir, el formato del nif es el siguiente:
  8 dígitos numéricos más una letra en mayúscula. Ejemplo: 00756764G
- La fecha de nacimiento se generará aleatoriamente y tendrá que ser una fecha válida, teniendo en cuenta los años bisiestos,
  el formato de la fecha debe de ser: AAAA-MM-DD (A=año, M=número de mes, D=número de día). Ejemplo: 1996-03-09
- El número de móvil se generará aleatoriamente, teniendo en cuenta que los números de móvil no se pueden repetir y,
  el número de móvil deberá tener una longitud de 9 dígitos numéricos y el primer dígito debe de empezar por '6'
- El número de fax se generará aleatoriamente, teniendo en cuenta que los números de fax no se pueden repetir y,
  el número de fax deberá tener una longitud de 9 dígitos numéricos y el primer dígito debe de empezar por '9'
- El email se generará aleatoriamente, y tendrá el siguiente formato:
  nombre_de_la_persona.primer_apellido.número_aleatorio_de_tres_dígitos@curso.python.org
  El email no puede contener los siguientes caracteres: las vocales acentuadas, ni caracteres especiales excepto el ('.') punto, la arroba ('@') y,
  el guión bajo (_). Todas las vocales con acentos (¨`^´~) se substituirán por su correspondiente vocal sin acento, los caracteres 'ñ' y 'ç' se
  substituirán por 'n' y 'c' respectivamente. El email generado debe de estar todo en minúsculas.
------------------------------------------------------------------------------------------------------------------------------------------------------
Tipos de datos de los datos generados de personas.
------------------------------------------------------------------------------------------------------------------------------------------------------
Nombre del dato           Tipo de dato
------------------------------------------------------------------------------------------------------------------------------------------------------
nombre                    Cadena de texto
apellido1 y apellido2     Cadena de texto
sexo                      Cadena de texto
nif                       Cadena de texto
provincia                 Cadena de texto
poblacion                 Cadena de texto
código postal             Cadena de texto
fecha de nacimiento       Cadena de texto
número de móvil           Número entero
número de fax             Número entero
email                     Cadena de texto
------------------------------------------------------------------------------------------------------------------------------------------------------
'''

import random
from api import Paths, Files

def personas(numero_mujeres, numero_hombres):
    provincias = Files.list_file_text(Paths.FILE_PROVINCIAS)[1:]
    poblaciones = Files.list_file_text(Paths.FILE_POBLACIONES)[1:]
    nombres = Files.list_file_text(Paths.FILE_NOMBRES)[1:]
    apellidos = Files.list_file_text(Paths.FILE_APELLIDOS)[1:]

    nifs = []
    mobiles = []
    faxes = []

    def to_nif(number):
        return str(number).zfill(8) + 'TRWAGMYFPDXBNJZSQVHLCKE'[number % 23]

    def get_nif():
        while True:
            number = random.randint(0, 99999999)
            nif = to_nif(number)
            if nif not in nifs:
                nifs.append(nif)
                break
        return nif

    def get_mobile():
        while True:
            ini = '6'
            fin = str(random.randint(0, 99999999)).zfill(8)
            number = int(ini + fin)
            if number not in mobiles:
                mobiles.append(number)
                break
        return number

    def get_fax():
        while True:
            ini = '9'
            fin = str(random.randint(0, 99999999)).zfill(8)
            number = int(ini + fin)
            if number not in faxes:
                faxes.append(number)
                break
        return number

    def es_bisiesto(anho):
        return anho % 400 == 0 or (anho % 100 != 0 and anho % 4 == 0)

    def get_date():
        year = random.randint(1940, 2020)
        month = random.randint(1, 12)
        day = 0
        if month in [1, 3, 5, 7, 8, 10, 12]:
            day = random.randint(1, 31)
        elif month in [4, 6, 9, 11]:
            day = random.randint(1, 30)
        elif month == 2:
            day = random.randint(1, 28 + (1 if es_bisiesto(year) else 0))
        return f'{year}-{str(month).zfill(2)}-{str(day).zfill(2)}'

    def get_cp(id_provincia):
        return id_provincia.zfill(2) + str(random.randint(1, 999)).zfill(3)

    def to_abc(texto):
        texto = texto.lower()
        chars = {
            **{a: 'a' for a in 'áàâäã'},
            **{e: 'e' for e in 'éèêë'},
            **{i: 'i' for i in 'íìîï'},
            **{o: 'o' for o in 'óòôöõ'},
            **{u: 'u' for u in 'úùûü'},
            **{'ñ': 'n', 'ç': 'c', 'ÿ': 'y', 'ý': 'y'},
            **{chr(n): '' for n in range(48)},
            **{chr(n): '' for n in range(58, 65)},
            **{chr(n): '' for n in range(91, 95)},
            **{chr(n): '' for n in range(123, 128)}
        }
        for k, v in chars.items(): texto = texto.replace(k, v)
        return texto

    def to_email(text):
        text = to_abc(text) \
            .replace(' de ', ' ') \
            .replace(' del ', ' ') \
            .replace(' el ', ' ') \
            .replace(' la ', ' ') \
            .replace(' las ', ' ') \
            .replace(' da ', ' ') \
            .replace(' das ', ' ') \
            .replace(' do ', ' ') \
            .replace(' dos ', ' ') \
            .replace(' lo ', ' ') \
            .replace(' los ', ' ')
        return '.'.join(text.split())

    def get_email(name, last_name):
        number = str(random.randint(1, 999)).zfill(3)
        email = f'{to_email(name)}.{to_email(last_name)}.{number}@curso.python.org'
        return email

    def get_poblaciones(id_provincia):
        return [r for r in poblaciones if r.split(';')[1] == id_provincia]

    def get_names(sex):
        filtrados = [x for x in nombres if x.strip().split(';')[1] == sex]
        return [x.split(';')[0] for x in filtrados]

    def get_record(sex):
        names = get_names(sex)
        f_surname = apellidos[random.randint(0, len(apellidos) - 1)].rstrip()
        s_surname = apellidos[random.randint(0, len(apellidos) - 1)].rstrip()
        data = {}
        data['nombre'] = names[random.randint(0, len(names) - 1)]
        data['apellidos'] = f'{f_surname} {s_surname}'
        data['sexo'] = sex
        data['nif'] = get_nif()
        provincia = provincias[random.randint(0, len(provincias) - 1)]
        id_provincia = provincia.split(';')[0]
        nombre_provincia = provincia.split(';')[1]
        data['provincia'] = nombre_provincia
        poblaciones = get_poblaciones(id_provincia)
        poblacion = poblaciones[random.randint(0, len(poblaciones) - 1)]
        data['poblacion'] = poblacion.split(';')[2].rstrip()
        data['cp'] = get_cp(id_provincia)
        data['nacimiento'] = get_date()
        data['movil'] = get_mobile()
        data['fax'] = get_fax()
        data['email'] = get_email(data['nombre'], f_surname)
        return data

    men = [get_record('h') for _ in range(numero_hombres)]
    women = [get_record('m') for _ in range(numero_mujeres)]
    records = men + women
    random.shuffle(records)
    return records

data = personas(10, 10)
print(data)
