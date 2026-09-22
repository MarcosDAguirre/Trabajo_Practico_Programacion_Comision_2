import sys
from f1_leer_observaciones import salida_f1
from f2_separar_viento import salida_f2
from f3_cantidad_de_ciudades import salida_f3
from f4_cantidad_de_ciudades_completas import salida_f4
from f5_top_n_ciudades import salida_f5

# entradas
datos_SMN = sys.argv[1]
par_tipo = int(input('Para la funcion f5 eliga tipo escribiendo: 1 (para temperatura) o 2 (para viento): '))
par_cantidad = int(input('Para la funcion f5 ingrese la cantidad de ciudades con un numero entero: ')) 
par_sentido = int(input('Para la funcion f5 eliga tipo de orden escribiendo: 3 (para ascendente) o 4 (para descendente): '))

# funciones importadas
diccionario = salida_f1(datos_SMN)
viento = salida_f2(diccionario)
cantidad_ciudades_leidas = salida_f3(diccionario)
cantidad_ciudades_completas = salida_f4(diccionario)
top_n_ciudades = salida_f5(diccionario,par_tipo,par_cantidad,par_sentido)

print ('='* 197)
print (f'f1_leer_observaciones.py:\n{diccionario}')
print ("=" * 197)
print (f'f2_separar_viento:\n{viento}')
print ("=" * 197)	
print (f'f3_cantidad_de_ciudades:\n{cantidad_ciudades_leidas}')
print ("=" * 197)
print (f'f4_cantidad_de_ciudades_completas:\n{cantidad_ciudades_completas}')
print ("=" * 197)
print (f'f5_top_n_de_ciudades:\n {top_n_ciudades}')
print ('=' * 197)

  


