import sys
import json
from datetime import date, datetime , timedelta

meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
def salida_f1(dato: str) -> dict:
    # Lee el archivo de observaciones del SMN (.txt) y devuelve un diccionario
    # {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    # ya separado en dirección y velocidad."""
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
                    velocidad_viento = 0.0
                elif viento_v1[0] == 'Direcciones':
                    direccion_viento = 'Direcciones Variables'
                    velocidad_viento = float(viento_v1[2])
                else:
                    direccion_viento = viento_v1[0]
                    velocidad_viento = float(viento_v1[1])           
                salida[ciudad] = {'Fecha':fecha,'Hora':hora,'Condición del cielo':c_cielo,'Visibilidad':visibilidad,'Temperatura':temperatura,'Sensación térmica':s_térmica,'Humedad':humedad,'Direccion_viento': direccion_viento,'Velocidad_viento':velocidad_viento,'Presión':presion}    
    return salida

def salida_f2(diccionario: dict) -> dict:
    # Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
    # Contempla el caso 'Calma' (sin velocidad numérica)
    ciudades_leidas = {}
    contador = 0
    for clave,valor in diccionario.items():
        valor_velocidad = valor['Velocidad_viento']
        if valor['Direccion_viento'] == 'Calma':
                direccion_viento = 'Inexistente'
                velocidad_viento = 0.0
        elif valor['Direccion_viento'] == 'Direcciones Variables':
                direccion_viento = 'Variable'
                velocidad_viento = valor_velocidad
        else:
                direccion_viento = valor['Direccion_viento']
                velocidad_viento = valor_velocidad
        ciudades_leidas[clave] = {'Direccion_viento':direccion_viento,'Velocidad_viento':velocidad_viento}
    return ciudades_leidas	

def salida_f3(diccionario: dict) -> dict:
    # Devuelve la cantidad total de ciudades leídas.
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

def salida_f4(diccionario:dict) -> dict:
    # Devuelve la cantidad de ciudades sin ningún dato faltante.
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

salida = []
lista_1 = []
def salida_f5(diccionario: dict,tipo: int,cantidad: int,sentido: int) -> list:          # 1 Temperatura / 2 Viento / 3 Ascendente / 4 Descendente
    # Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor
    # (o al revés si descendente=False), en una lista. Reutilizable tanto para temperatura
    # como para viento.
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
                        valor_velocidad_viento = valor['Velocidad_viento']
                    else:
                        valor_velocidad_viento = valor['Velocidad_viento']
                except(IndexError):
                    pass
                salida.append((valor_velocidad_viento,clave))
    if sentido == 3:
        lista_1 = (sorted(salida))
    if sentido == 4:
        lista_1 = ((sorted(salida))[::-1])
    return (lista_1[:cantidad])                    

def salida_f6() -> None:
    # Imprime por pantalla el resumen con todas las características solicitadas.
    # Parametros de entrada
	datos_SMN = sys.argv[1]
	par_tipo = int(input('Para la funcion f5 eliga tipo escribiendo: 1 (para temperatura) o 2 (para viento): '))
	par_cantidad = int(input('Para la funcion f5 ingrese la cantidad de ciudades con un numero entero: ')) 
	par_sentido = int(input('Para la funcion f5 eliga tipo de orden escribiendo: 3 (para ascendente) o 4 (para descendente): '))
	# Llamadas a funciones
	diccionario = salida_f1(datos_SMN)
	viento = salida_f2(diccionario)
	cantidad_ciudades_leidas = salida_f3(diccionario)
	cantidad_ciudades_completas = salida_f4(diccionario)
	top_n_ciudades = salida_f5(diccionario,par_tipo,par_cantidad,par_sentido)
	ciudades_temp = salida_f7(diccionario)
	ciudades_vel = salida_f8(diccionario)
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
	print (ciudades_temp)
	print ('=' * 197 + '\nf8_ciudades_viento:')
	print (ciudades_vel)

def salida_f7(diccionaro:dict) -> dict:
    #Devuelve la/s ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima. Nota: n = 5
    temperaturas = []
    for clave,valor in diccionaro.items():
        valor_temperatura = valor['Temperatura']
        temperaturas.append((valor_temperatura,clave))
    return {'Temperaturas_minimas':(sorted(temperaturas))[:5],'Temperaturas_maximas':((sorted(temperaturas))[::-1])[:5]}

def salida_f8(diccionario: dict) -> dict:
    # Devuelve la/s ciudad(es)[:n] con velocidades máximas y mínimas de viento. Nota: n = 5
    velocidades_viento = []
    for clave,valor in diccionario.items():
        valor_velocidad_viento = valor['Velocidad_viento']
        velocidades_viento.append((valor_velocidad_viento,clave))
    return {'Velocidades_minimas_viento':(sorted(velocidades_viento))[:5],'Velocidades_maximas_viento':((sorted(velocidades_viento))[::-1])[:5]}