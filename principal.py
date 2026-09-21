import sys
from f1_leer_observaciones import salida_f1
from f3_cantidad_de_ciudades import salida_f3
from f4_cantidad_de_ciudades_completas import salida_f4

datos_SMN = sys.argv[1]

# funciones importadas
diccionario = salida_f1(datos_SMN)
cantidad_ciudades = salida_f3(datos_SMN)
cantidad_ciudades_completas = salida_f4(datos_SMN)
print (diccionario)	
print (f'Hay un total de {cantidad_ciudades} ciudades')
print (f'Hay {cantidad_ciudades_completas} ciudades completas')
     


