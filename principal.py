import sys
from f1_leer_observaciones import salida_f1
from f3_cantidad_de_ciudades import salida_f3

datos_SMN = sys.argv[1]

# funciones importadas
diccionario = salida_f1(datos_SMN)
cantidad_ciudades = salida_f3(datos_SMN)
print (diccionario)	
print (cantidad_ciudades)
     


