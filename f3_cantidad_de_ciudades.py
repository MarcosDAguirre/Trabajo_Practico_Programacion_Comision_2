
def salida_f3(diccionario):
    ciudades_leidas = []
    contador = 0
    for clave in diccionario.keys():
        ciudades_leidas.append(clave)
        contador += 1
    return {'Ciudades_leidas':ciudades_leidas,'Cantidad_de_ciudades_leidas':contador}

# Devuelve la cantidad total de ciudades leídas.