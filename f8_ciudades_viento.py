salida = []
sal_min = {}
sal_max = {}
def salida_f8(diccionario,cantidad):
    ciudades_leidas = {}
    contador = 0
    for clave,valor in diccionario.items():
        valor_v1 = (valor['Viento']).split()
        try:
            if valor_v1[0] == 'Calma':
                direccion_viento = 'Inexistente'
                velocidad_viento = 0.0
            elif valor_v1[0] == 'Direcciones':
                direccion_viento = 'Variable'
                velocidad_viento = float(valor_v1[2])
            else:
                direccion_viento = valor_v1[0]
                velocidad_viento = float(valor_v1[1])
        except(IndexError):
            pass      
        salida.append((velocidad_viento,clave))

    vel_min = (sorted(salida))[:cantidad]
    vel_max = ((sorted(salida))[::-1])[:cantidad]

    for par in vel_min:
            sal_min[par[1]] = par[0]
    for par in vel_max:
            sal_max[par[1]] = par[0]
    v_salida = {'Velocidades_minimas_viento':sal_min,'Velocidades_maximas_viento':sal_max}     
    return v_salida
