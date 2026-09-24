import sys
import json
from datetime import date, datetime , timedelta

meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
def salida_f1(dato):
	salida = {}
	con_errores_1 = []
	with open (dato, encoding = 'cp1252') as f:
		for i in f:
			linea = i.split(';')
			if len(linea) == 10:
				ciudad = linea[0].strip()  
				fecha = linea[1].split('-')
				fecha[1] = str(meses[fecha[1]])
				fecha = '/'.join(fecha)  
				fecha = datetime.strptime(fecha, "%d/%m/%Y").strftime('%d/%m/%Y')  
				hora = datetime.strptime(linea[2],'%H:%M').strftime('%H:%M')
				c_cielo = linea[3]
				visibilidad = linea[4]
				temperatura = float(linea[5])
				s_térmica = linea[6]           
				humedad = linea[7]
				presion = linea[9].strip()
				viento_v1 = linea[8].split()
				if viento_v1[0] == 'Calma':
					direccion_viento = 'Calma'
					velocidad_viento = ' '
				elif viento_v1[0] == 'Direcciones':
					direccion_viento = 'Direcciones Variables'
					velocidad_viento = viento_v1[2]
				else:
					direccion_viento = viento_v1[0]
					velocidad_viento = viento_v1[1]           
				salida[ciudad] = {'Fecha':fecha,'Hora':hora,'Condición del cielo':c_cielo,'Visibilidad':visibilidad,'Temperatura':temperatura,'Sensación térmica':s_térmica,'Humedad':humedad,'Direccion_viento': direccion_viento,'Velocidad_viento':velocidad_viento,'Presión':presion}    
	return salida
# Lee el archivo de observaciones del SMN y devuelve un diccionario
# {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
# ya separado en dirección y velocidad."""

def salida_f2(diccionario):
    ciudades_leidas = {}
    contador = 0
    for clave,valor in diccionario.items():
        valor_velocidad = valor['Velocidad_viento']
        if valor['Direccion_viento'] == 'Calma':
                direccion_viento = 'Inexistente'
                velocidad_viento = '0'
        elif valor['Direccion_viento'] == 'Direcciones Variables':
                direccion_viento = 'Variable'
                velocidad_viento = valor_velocidad
        else:
                direccion_viento = valor['Direccion_viento']
                velocidad_viento = valor_velocidad
        ciudades_leidas[clave] = {'Direccion_viento':direccion_viento,'Velocidad_viento':velocidad_viento}
    return ciudades_leidas	
# Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
# Contempla el caso 'Calma' (sin velocidad numérica)	

def salida_f3(diccionario):
    ciudades_leidas = []
    contador = 0
    total_ciudades = len(diccionario)
    for clave in diccionario.keys():
        ciudades_leidas.append(clave)
        contador += 1
    if total_ciudades == contador:
        return {'Cantidad_de_ciudades_leidas':contador,'Ciudades_leidas':ciudades_leidas}
    else:
        return "Error en cálculo de ciudades_leidas"
# Devuelve la cantidad total de ciudades leídas.


def salida_f4(diccionario):
    ciudades_incompletas = []
    cantidad_de_ciudades = len(diccionario)
    for clave,valor in diccionario.items():
        valor_ST = valor['Sensación térmica']
        try:
            float(valor_ST)                                   
        except(ValueError):
            ciudades_incompletas.append(clave)
        if len(valor) != 10:
            ciudades_incompletas.append(clave)
        if valor['Direccion_viento'] == 'Calma':
            ciudades_incompletas.append(clave)
    ciudades_incompletas_conjunto = set(ciudades_incompletas)
    cantidad_de_incompletas = len(ciudades_incompletas_conjunto)
    ciudades_completas = set(diccionario) - ciudades_incompletas_conjunto
    cantidad_completas = cantidad_de_ciudades - cantidad_de_incompletas
    return {'Cantidad_ciudades_completas':cantidad_completas,'Ciudades_completas':ciudades_completas}
# Devuelve la cantidad de ciudades sin ningún dato faltante.

salida = []
lista_1 = []
def salida_f5(diccionario,tipo,cantidad,sentido):           # 1 Temperatura / 2 Viento / 3 Ascendente / 4 Descendente
    for clave,valor in diccionario.items():
            if tipo == 1:
                valor_temp = valor['Temperatura']
                salida.append((valor_temp,clave))
            if tipo == 2:
                valor_v1 = valor['Direccion_viento']
                try:
                    if valor_v1 == 'Calma':
                        valor_velocidad_viento = 0.0
                    elif valor_v1 == 'Direcciones Variables':
                        valor_velocidad_viento = float(valor['Velocidad_viento'])
                    else:
                        valor_velocidad_viento = float(valor['Velocidad_viento'])
                except(IndexError):
                    pass
                salida.append((valor_velocidad_viento,clave))
    if sentido == 3:
        lista_1 = (sorted(salida))
    if sentido == 4:
        lista_1 = ((sorted(salida))[::-1])
    return (lista_1[:cantidad])                    
# Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
# (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
# como para viento.

salida1 = []
sal_min1 = {}
sal_max1 = {}
def salida_f7(diccionario,cant):           
    for clave,valor in diccionario.items():
                valor_temp = valor['Temperatura']
                salida1.append((valor_temp,clave))
    temp_min = (sorted(salida))[:cant]
    temp_max = ((sorted(salida))[::-1])[:cant]
        
    for par in temp_min:
            sal_min1[par[1]] = par[0]
    for par in temp_max:
            sal_max1[par[1]] = par[0] 
    d_salida = {'Temperaturas_minimas':sal_min1,'Temperaturas_maximas':sal_max1}       
    return d_salida
# ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima.

salida2 = []
sal_min2 = {}
sal_max2 = {}
def salida_f8(diccionario,cant):
    ciudades_leidas = {}
    contador = 0
    for clave,valor in diccionario.items():
        valor_direccion = valor['Direccion_viento']
        try:
            if valor_direccion == 'Calma':
                direccion_viento = 'Inexistente'
                velocidad_viento = 0.0
            elif valor_direccion == 'Direcciones':
                direccion_viento = 'Variable'
                velocidad_viento = float(valor['Velocidad_viento'])
            else:
                direccion_viento = valor_direccion
                velocidad_viento = float(valor['Velocidad_viento'])
        except(IndexError):
            pass      
        salida2.append((velocidad_viento,clave))
    vel_min = (sorted(salida))[:cant]
    vel_max = ((sorted(salida))[::-1])[:cant]
    for par in vel_min:
            sal_min2[par[1]] = par[0]
    for par in vel_max:
            sal_max2[par[1]] = par[0]
    v_salida = {'Velocidades_minimas_viento':sal_min2,'Velocidades_maximas_viento':sal_max2}     
    return v_salida

def salida_f6():
	# Parametros de entrada
	datos_SMN = sys.argv[1]
	par_tipo = int(input('Para la funcion f5 eliga tipo escribiendo: 1 (para temperatura) o 2 (para viento): '))
	par_cantidad = int(input('Para la funcion f5 ingrese la cantidad de ciudades con un numero entero: ')) 
	par_sentido = int(input('Para la funcion f5 eliga tipo de orden escribiendo: 3 (para ascendente) o 4 (para descendente): '))
	cantidad_ciudades = int(input('Para las funciones f7 y f8 ingrese un número entero para visualizar esa cantidad de ciudades: '))
	# Llamadas a funciones
	diccionario = salida_f1(datos_SMN)
	viento = salida_f2(diccionario)
	cantidad_ciudades_leidas = salida_f3(diccionario)
	cantidad_ciudades_completas = salida_f4(diccionario)
	top_n_ciudades = salida_f5(diccionario,par_tipo,par_cantidad,par_sentido)
	ciudades_temp = salida_f7(diccionario,cantidad_ciudades)
	ciudades_vel = salida_f8(diccionario,cantidad_ciudades)
	# Para imprimir 
	print ('=' * 197 + '\nf6_mostrar_resumen')
	print ('=' * 197 + '\nf1_leer_observaciones:')
	print (json.dumps(diccionario,indent = 4, ensure_ascii = False ))
	print ("=" * 197 + '\nf2_separar_viento:')
	print (json.dumps(viento, indent = 4, ensure_ascii = False))
	print ("=" * 197)	
	print (f'f3_cantidad_de_ciudades:\n{cantidad_ciudades_leidas}')
	print ("=" * 197)
	print (f'f4_cantidad_de_ciudades_completas:\n{cantidad_ciudades_completas}')
	print ("=" * 197)
	print (f'f5_top_n_de_ciudades:\n {top_n_ciudades}')
	print ('=' * 197 + '\nf7_ciudades_temperatura:')
	print (json.dumps(ciudades_temp,indent = 4, ensure_ascii = False))
	print ('=' * 197 + '\nf8_ciudades_viento:')
	print (json.dumps(ciudades_vel,indent = 4, ensure_ascii = False))
# Imprime por pantalla el resumen con todas las 
# características calculadas. Usar n=5