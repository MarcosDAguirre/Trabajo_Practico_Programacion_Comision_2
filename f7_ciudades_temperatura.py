salida = []
sal_min = {}
sal_max = {}
def salida_f7(diccionario,cantidad):           
    for clave,valor in diccionario.items():
                valor_temp = valor['Temperatura']
                salida.append((valor_temp,clave))
    temp_min = (sorted(salida))[:cantidad]
    temp_max = ((sorted(salida))[::-1])[:cantidad]
        
    for par in temp_min:
            sal_min[par[1]] = par[0]
    for par in temp_max:
            sal_max[par[1]] = par[0]

    d_salida = {'Temperaturas_minimas':sal_min,'Temperaturas_maximas':sal_max}       
            
    return d_salida
# ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima.