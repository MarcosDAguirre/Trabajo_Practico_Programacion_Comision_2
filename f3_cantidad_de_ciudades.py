from datetime import date,datetime,timedelta

meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}

def salida_f3(dato):
	salida = {}
	n = 0
	with open (dato, encoding = 'cp1252') as f:
		for i in f:
			linea = i.split(';')
			clave = linea[0].strip()  # clave es una ciudad.
			n += 1
			salida[clave] = ''
		cantidad_de_ciudades = len(salida)	
	return cantidad_de_ciudades
 


# Lee el archivo de observaciones del SMN y devuelve un diccionario
# {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
# ya separado en dirección y velocidad."""
	
	
	
# Devuelve la cantidad total de ciudades leídas.	
