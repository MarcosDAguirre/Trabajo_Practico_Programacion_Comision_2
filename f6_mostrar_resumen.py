import sys
import json
from f1_leer_observaciones import salida_f1
from f2_separar_viento import salida_f2
from f3_cantidad_de_ciudades import salida_f3
from f4_cantidad_de_ciudades_completas import salida_f4
from f5_top_n_ciudades import salida_f5
from f7_ciudades_temperatura import salida_f7
from f8_ciudades_viento import salida_f8

def salida_f6():
	# Parametros de entrada
	datos_SMN = sys.argv[1]
	par_tipo = int(input('Para la funcion f5 eliga tipo escribiendo: 1 (para temperatura) o 2 (para viento): '))
	par_cantidad = int(input('Para la funcion f5 ingrese la cantidad de ciudades con un numero entero: ')) 
	par_sentido = int(input('Para la funcion f5 eliga tipo de orden escribiendo: 3 (para ascendente) o 4 (para descendente): '))
	cantidad_ciudades = int(input('Para las funciones f7 y f8 ingrese un número entero para visualizar esa cantidad de ciudades: '))
	# Llamadas a funciones
	diccionario = salida_f1(datos_SMN)
	viento = salida_f2(diccionario)
	cantidad_ciudades_leidas = salida_f3(diccionario)
	cantidad_ciudades_completas = salida_f4(diccionario)
	top_n_ciudades = salida_f5(diccionario,par_tipo,par_cantidad,par_sentido)
	ciudades_temp = salida_f7(diccionario,cantidad_ciudades)
	ciudades_vel = salida_f8(diccionario,cantidad_ciudades)
	# Para imprimir 
	print ('=' * 197 + '\nf6_mostrar_resumen')
	print ('=' * 197 + '\nf1_leer_observaciones:')
	print (json.dumps(diccionario,indent = 4, ensure_ascii = False ))
	print ("=" * 197 + '\nf2_separar_viento:')
	print (json.dumps(viento, indent = 4, ensure_ascii = False))
	print ("=" * 197)	
	print (f'f3_cantidad_de_ciudades:\n{cantidad_ciudades_leidas}')
	print ("=" * 197)
	print (f'f4_cantidad_de_ciudades_completas:\n{cantidad_ciudades_completas}')
	print ("=" * 197)
	print (f'f5_top_n_de_ciudades:\n {top_n_ciudades}')
	print ('=' * 197 + '\nf7_ciudades_temperatura:')
	print (json.dumps(ciudades_temp,indent = 4, ensure_ascii = False))
	print ('=' * 197 + '\nf8_ciudades_viento:')
	print (json.dumps(ciudades_vel,indent = 4, ensure_ascii = False))

# Imprime por pantalla el resumen con todas las 
# características calculadas. Usar n=5