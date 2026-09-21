from datetime import date,datetime,timedelta

meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}

def salida_f1(dato):
	salida = {}
	with open (dato, encoding = 'cp1252') as f:
		for i in f:
			linea = i.split(';')
			clave = linea[0].strip()  # clave es una ciudad.
			fecha = linea[1].split('-')
			fecha[1] = str(meses[fecha[1]])
			fecha = '/'.join(fecha)  
			fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime('%d/%m/%Y')  
			hora = datetime.strptime(linea[2],'%H:%M').strftime('%H:%M')
			c_cielo = linea[3]
			visibilidad = linea[4]
			temperatura = float(linea[5])
			s_térmica = 'falta'            # ver
			humedad = linea[7]
			viento = 'falta'               # ver
			presion = linea[9].strip()
			salida[clave] = {'Fecha':fecha,'Hora':hora,'Condición del cielo':c_cielo,'Visibilidad':visibilidad,'Temperatura':temperatura,'Sensación térmica':s_térmica,'Humedad':humedad,'Viento':viento,'Presión':presion}
	return salida
 


# Lee el archivo de observaciones del SMN y devuelve un diccionario
# {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
# ya separado en dirección y velocidad."""
