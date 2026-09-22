lista = ['Calma','Direcciones']

def salida_f4(diccionario):
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
        if valor['Viento'] in lista:
            ciudades_incompletas.append(clave)

    ciudades_incompletas_conjunto = set(ciudades_incompletas)
    cantidad_de_incompletas = len(ciudades_incompletas_conjunto)
    ciudades_completas = set(diccionario) - ciudades_incompletas_conjunto
    cantidad_completas = cantidad_de_ciudades - cantidad_de_incompletas

    return {'Cantidad_ciudades_completas':cantidad_completas,'Ciudades_completas':ciudades_completas}
          
             
# Devuelve la cantidad de ciudades sin ningún dato faltante.