import api.Files as Files

datos = Files.list_file_text('c:/datasets/curso/taxi_flota_diario.csv', codificacion='utf-8')
cabecera = datos[0]
campos_cab = cabecera.split(';')
datos_total = []
for linea_datos in datos[1:]:
    datos_linea = linea_datos.split(';')
    data = {}
    for indice in range(len(campos_cab)):
        data[  campos_cab[indice]  ] = datos_linea[indice]
    datos_total.append(data)

