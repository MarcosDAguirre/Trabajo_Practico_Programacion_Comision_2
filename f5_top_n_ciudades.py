salida = []
lista_1 = []
lista_raro = ['Calma','Direcciones']

def salida_f5(diccionario,tipo,cantidad,sentido):           # 1 Temperatura / 2 Viento / 3 Ascendente / 4 Descendente
    for clave,valor in diccionario.items():
            if tipo == 1:
                valor_temp = valor['Temperatura']
                salida.append((valor_temp,clave))
            if tipo == 2:
                valor_v1 = (valor['Viento']).split()
                try:
                    if valor_v1[0] in lista_raro:
                        valor_velocidad_viento = 0.0
                    else:
                        valor_velocidad_viento = float(valor_v1[1])
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
