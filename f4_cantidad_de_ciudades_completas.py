
def salida_f4(diccionario):
    contador = 0
    ciudades_completas = []
    for clave,valor in diccionario.items():
        valor_ST = valor['Sensación térmica']
        try:
                        float(valor_ST)
                        contador += 1
                        ciudades_completas.append(clave)
        except(ValueError):
                pass
    return {'Ciudades_completas':ciudades_completas,'Cantidad_ciudades_completas':contador}
          
             
# Devuelve la cantidad de ciudades sin ningún dato faltante.