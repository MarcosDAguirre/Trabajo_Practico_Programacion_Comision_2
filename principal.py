import sys
from f1_leer_observaciones import salida_f1
from f2_separar_viento import salida_f2
from f3_cantidad_de_ciudades import salida_f3
from f4_cantidad_de_ciudades_completas import salida_f4

datos_SMN = sys.argv[1]

# funciones importadas
diccionario = salida_f1(datos_SMN)
viento = salida_f2(diccionario)
cantidad_ciudades_leidas = salida_f3(diccionario)
cantidad_ciudades_completas = salida_f4(diccionario)

print (diccionario)
print (viento)	
print (cantidad_ciudades_leidas)
print (cantidad_ciudades_completas)

     


