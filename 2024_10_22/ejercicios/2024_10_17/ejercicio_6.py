'''
Dado el siguiente código en Python:
datos =	[
	  'longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value,ocean_proximity',
	  '-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,452600.0,NEAR BAY',
	  '-122.22,37.86,21.0,7099.0,1106.0,2401.0,1138.0,8.3014,358500.0,NEAR BAY',
	  '-122.24,37.85,52.0,1467.0,190.0,496.0,177.0,7.2574,352100.0,NEAR BAY',
	  '-122.25,37.85,52.0,1274.0,235.0,558.0,219.0,5.6431,341300.0,NEAR BAY',
	  '-122.25,37.85,52.0,1627.0,280.0,565.0,259.0,3.8462,342200.0,NEAR BAY'
	]
Realizar un programa que muestre en pantalla la 'latitude' máxima y mínima en formato numérico, y también la suma total de 'total_rooms'.

Ejemplo utilizando la colección anterior:
Se muestra en pantalla: (37.88, 37.85, 12347.0)
'''

datos =	[
	  'longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,median_house_value,ocean_proximity',
	  '-122.23,37.88,41.0,880.0,129.0,322.0,126.0,8.3252,452600.0,NEAR BAY',
	  '-122.22,37.86,21.0,7099.0,1106.0,2401.0,1138.0,8.3014,358500.0,NEAR BAY',
	  '-122.24,37.85,52.0,1467.0,190.0,496.0,177.0,7.2574,352100.0,NEAR BAY',
	  '-122.25,37.85,52.0,1274.0,235.0,558.0,219.0,5.6431,341300.0,NEAR BAY',
	  '-122.25,37.85,52.0,1627.0,280.0,565.0,259.0,3.8462,342200.0,NEAR BAY'
]

latitudes = []
total_rooms = []
for record in datos[1:]:
    data = record.split(',')
    latitudes.append(float(data[1]))
    total_rooms.append(float(data[3]))
print((max(latitudes), min(latitudes), sum(total_rooms)))
