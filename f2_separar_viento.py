
def salida_f2(diccionario):
    ciudades_leidas = {}
    contador = 0
    for clave,valor in diccionario.items():
        valor_v1 = (valor['Viento']).split()
        try:
            if valor_v1[0] == 'Calma':
                direccion_viento = 'Inexistente'
                velocidad_viento = '0'
            else:
                direccion_viento = valor_v1[0]
                velocidad_viento = valor_v1[1]
        except(IndexError):
            pass        
        ciudades_leidas[clave] = {'Direccion_viento':direccion_viento,'Velocidad_viento':velocidad_viento}
    return ciudades_leidas
		
# Convierte un campo de viento como 'Norte  3' en (direccion, velocidad).
# Contempla el caso 'Calma' (sin velocidad numérica)		
