'''
Realizar un programa que solicite un texto por teclado y, en base al texto introducido mostrar un pantalla un nuevo texto en minúsculas según las siguientes indicaciones:
	- Las vocales 'áàâäã' se substituirán por la vocal 'a'
	- Las vocales 'éèêë' se substituirán por la vocal 'e'
	- Las vocales 'íìîï' se substituirán por la vocal 'i'
	- Las vocales 'óòôöõ' se substituirán por la vocal 'o'
	- Las vocales 'úùûü' se substituirán por la vocal 'u'
	- Las consonantes 'ñ', 'ç', 'ÿ', 'ý' se substituirán por 'n', 'c', 'y', 'y' respectivamente
	- Los espacios en blancos se substituirán por una cadena vacía

Ejemplo:
Texto introducido por teclado: 'Ésta MAÑANA del Miércoles paseando por BARÇA con mi Pingüino'
Se muestra en pantalla: estamananadelmiercolespaseandoporbarcaconmipinguino
'''

# ------------------------------------------------------------------
# Versión 1 del ejercicio
# ------------------------------------------------------------------
texto = input('Texto a introducir: ').lower()

aes = {a: 'a' for a in 'áàâäã'}
ees = {e: 'e' for e in 'éèêë'}
ies = {i: 'i' for i in 'íìîï'}
oes = {o: 'o' for o in 'óòôöõ'}
ues = {u: 'u' for u in 'úùûü'}

letters = {'ñ': 'n', 'ç': 'c', 'ÿ': 'y', 'ý': 'y'}

special_1 = {chr(n): '' for n in range(48)}
special_2 = {chr(n): '' for n in range(58, 65)}
special_3 = {chr(n): '' for n in range(91, 95)}
special_4 = {chr(n): '' for n in range(123, 128)}

chars = {
    **aes, **ees, **ies, **oes, **ues,
    **letters,
    **special_1, **special_2,
    **special_3, **special_4
}

print(chars)

for k, v in chars.items(): texto = texto.replace(k, v)

print(texto)

# ------------------------------------------------------------------
# Versión 2 del ejercicio
# ------------------------------------------------------------------
texto = input('Texto a introducir: ').lower()
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
print(texto)
