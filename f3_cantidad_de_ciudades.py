
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