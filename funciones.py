import sys
import json
from datetime import date, datetime , timedelta

def salida_f1(dato: str) -> dict:
    # Lee el archivo de observaciones del SMN (.txt) y devuelve un diccionario
    # {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento
    # ya separado en dirección y velocidad."""
    meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
    salida = {}
    with open (dato, encoding = 'cp1252') as f:
        for i in f:
            linea = i.split(';')
            ciudad = linea[0].strip()
            if len(linea) == 10:
                fecha_y_hora = aux_fecha_y_hora(linea)
                c_cielo = linea[3]
                visibilidad = linea[4]
                temperatura = float(linea[5])
                s_térmica = linea[6]           
                humedad = linea[7]
                presion = linea[9].strip()
                viento = linea[8].split()
                direccion_viento = aux_viento(viento)[0]
                velocidad_viento = aux_viento(viento)[1]    
                salida[ciudad] = {
                    'Fecha_y_hora': fecha_y_hora,
                    'Condición del cielo':c_cielo,
                    'Visibilidad':visibilidad,
                    'Temperatura':temperatura,
                    'Sensación térmica':s_térmica,
                    'Humedad':humedad,
                    'Direccion_viento': direccion_viento,
                    'Velocidad_viento':velocidad_viento,
                    'Presión':presion}             
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
        if len(valor) != 9:
            ciudades_incompletas.append(clave)
        if valor['Direccion_viento'] == 'Calma':
            ciudades_incompletas.append(clave)
    ciudades_incompletas_conjunto = set(ciudades_incompletas)
    cantidad_de_incompletas = len(ciudades_incompletas_conjunto)
    ciudades_completas = set(diccionario) - ciudades_incompletas_conjunto
    cantidad_completas = cantidad_de_ciudades - cantidad_de_incompletas
    return {'Cantidad_ciudades_completas':cantidad_completas,'Ciudades_completas':ciudades_completas}


def salida_f5(diccionario: dict,tipo: int,cantidad: int,sentido: int) -> list:          # 1 Temperatura / 2 Viento / 3 Ascendente / 4 Descendente
    # Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor (o al revés si descendente=False), 
    # en una lista. Reutilizable para temperatura y viento.
    salida = []
    lista_1 = []
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
    datos_SMN = sys.argv[1]
    par_tipo = int(input('Para la funcion f5 eliga tipo escribiendo: 1 (para temperatura) o 2 (para viento): '))
    par_sentido = int(input('Para la funcion f5 eliga tipo de orden escribiendo: 3 (para ascendente) o 4 (para descendente): '))
    par_cantidad = int(input('Para la funcion f5 ingrese la cantidad de ciudades con un numero entero: '))
    diccionario = salida_f1(datos_SMN)
    viento = salida_f2(diccionario)
    cantidad_ciudades_leidas = salida_f3(diccionario)
    cantidad_ciudades_completas = salida_f4(diccionario)
    top_n_ciudades = salida_f5(diccionario,par_tipo,par_cantidad,par_sentido)
    ciudades_temp = salida_f7(diccionario)
    ciudades_vel = salida_f8(diccionario)
    faltan_campos = salida_f9(datos_SMN)
    faltan_datos_en_columnas = salida_f10(datos_SMN)     
    print('=' * 197 + '\nf6_mostrar_resumen')
    print ('=' * 197 + '\nf1_leer_observaciones:')
    print (diccionario)
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
    print ('=' * 197 + '\nf9_ciudades_con_campos_faltantes:') 
    print (json.dumps(faltan_campos, indent = 4, ensure_ascii = False))
    print ('=' * 197 + '\nf10_ciudades_con_columnas_incompletas_completas:')
    print (json.dumps(faltan_datos_en_columnas, indent = 4, ensure_ascii = False))
    print ('=' * 197) 

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

def salida_f9(dato: str) -> dict:
    # Muestra la cantidad de datos faltantes por campo, y en qué estaciones ocurre. 'No se calcula' en Sensación Térmica se considera dato faltante'
    # lista_de_campos: 'Fecha','Hora','Condicion_del_cielo','Visibilidad','Temperatura','Sensacion_termica','Humedad','Viento','Presion'
    with open (dato, encoding = 'cp1252') as f:
        diccionario_incompletas = {}
        for i in f:
            dato_presente = []
            lista = i.split(';')
            contador_A = 0
            if len(lista) == 10:
                for campo_10 in lista:
                    if campo_10 == 'No se calcula':
                        diccionario_incompletas[lista[0]] = ['Sensacion_termica']                                                   
            if len(lista) < 10:
                for campo in lista[1:]:
                    contador_A += aux_filtro(campo)
                    lista_incompleta = []
                    if '2026' in campo:
                        dato_presente.append('Fecha')
                    if ":" in campo:
                        dato_presente.append('Hora')
                    if campo != 'Calma': 
                        if campo != 'No se calcula':
                            if ''.join(campo.split()).isalpha():
                                dato_presente.append('Condicion_del_cielo')
                    if 'km' in campo:                                                                        
                        dato_presente.append('Visibilidad')
                    if campo[0] == ' ':
                        dato_presente.append('Humedad')
                    try:
                        if campo == 'Calma':
                            dato_presente.append('Direccion_velocidad_viento')
                        if (campo.split())[0].isalpha() and (campo.split())[1].isdigit():
                            dato_presente.append('Direccion_velocidad_viento')
                    except Exception:
                        pass
                    if '/' in campo:
                        dato_presente.append('Presion')
                if 'Fecha' not in dato_presente:
                        lista_incompleta.append('Fecha')
                if 'Hora' not in dato_presente:
                        lista_incompleta.append('Hora')
                if 'Condicion_del_cielo' not in dato_presente :                                           
                        lista_incompleta.append('Condicion_del_cielo')
                if 'Visibilidad' not in dato_presente:
                        lista_incompleta.append('Visibilidad')
                if 'Humedad' not in dato_presente:
                        lista_incompleta.append('Humedad')
                if 'Direccion_velocidad_viento' not in dato_presente:
                        lista_incompleta.append('Direccion/velocidad_viento')
                if 'Presion' not in dato_presente:
                        lista_incompleta.append('Presion')
                if contador_A == 1 and 'No se calcula' in lista:
                        lista_incompleta.append('Sensacion_termica')
                elif contador_A == 1 and 'No se calcula' not in lista:
                        lista_incompleta.append('Temperatura o Sensacion_termica')
                elif contador_A == 0:
                    lista_incompleta.append('Temperatura')
                    lista_incompleta.append('Sensacion_termica')  
                diccionario_incompletas[lista[0]] = lista_incompleta                                   
    return diccionario_incompletas

def salida_f10(dato: str) -> dict:
    # Devuelve un diccionario con la cantidad de columnas esperados que no están presentes en alguna línea (según su ciudad). También indica que ciudades tienen  
    # completas sus columnas.
    completas_incompletas = {}
    con_faltantes = {}
    completas = {}
    with open (dato, encoding = 'cp1252') as f:
        con_faltantes = {}
        for i in f:
            linea = i.split(';')
            if len(linea) < 10:
                con_faltantes[linea[0]] = (f'Le faltan {10 - len(linea)} columnas')
            elif len(linea) == 10:
                 completas[linea[0]] = 'Tiene las columnas completas'
    completas_incompletas['Incompletas'] = con_faltantes
    completas_incompletas['Completas'] = completas                  
    return completas_incompletas

def aux_fecha_y_hora(fila:str) -> str:
    # Entrega fecha y hora en formato datetime(Y,m,d,H,M)
    meses = {'enero':1,'febrero':2,'marzo':3,'abril':4,'mayo':5,'junio':6,'julio':7,'agosto':8,'septiembre':9,'octubre':10,'noviembre':11,'diciembre':12}
    fecha1 = fila[1].split('-')
    hora1= fila[2].split(':')
    fecha = datetime(int(fecha1[2]),meses[fecha1[1]],int(fecha1[0]) ,int(hora1[0]), int(hora1[1]))
    return fecha         

def aux_viento(campo:str) -> list:
    # Devuelve una lista con los datos de direccion y velocidad del viento.
    if campo[0] == 'Calma':
        direccion_viento = 'Calma'
        velocidad_viento = 0.0
    elif campo[0] == 'Direcciones':
        direccion_viento = 'Direcciones Variables'
        velocidad_viento = float(campo[2])
    else:
        direccion_viento = campo[0]
        velocidad_viento = float(campo[1]) 
    return [direccion_viento,velocidad_viento]

def aux_filtro(dato:str) -> int:
    # Filtra los datos para obtener la cantidad de datos de Temperatura y Sensacion_termica presentes en la fila.
    contador = 0
    try:
        if type(abs(int(''.join(dato.split('.'))))).__name__ == 'int':
            if dato[0] != ' ' and (abs(int(''.join(dato.split('.'))))) < 900:
                contador += 1
    except Exception:
        pass
    return contador                      