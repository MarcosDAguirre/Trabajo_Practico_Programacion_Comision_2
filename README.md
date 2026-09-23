## Notas del proyecto:

Para iniciar, ejecutar en la consola (a modo de ejemplo):
```bash
python3 analisis_smn.py estado_tiempo20260910.txt
```
El proyecto contiene 8 funciones en total. Al ejecutar " ~$ python3 analisis_smn.py estado_tiempo20260910.txt analisis_smn.py "; el módulo analisis_smn.py, llama a la funcion f6_mostrar_resumen.py. Esta función solicita los parámetros necesarios (empleando int(input('texto'))), para las otras funciones. Luego  ejecuta a cada una de ellas y finalmente imprime en pantalla los valores solicitados según consignas del trabajo práctico.

El proyecto contiene 8 funciones en total:
```bash
f1_leer_observaciones.py
f2_separar_viento.py
f3_cantidad_de_ciudades.py
f4_cantidad_de_ciudades_completas.py
f5_top_n_ciudades.py
f6_mostrar_resumen.py
f7_ciudades_temperatura.py
f8_ciudades_viento.py
```
##                              Descripción de las funciones:
### f1:
Lee el archivo de observaciones del SMN y devuelve un diccionario  {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento ya separado en dirección  y velocidad.
### f2:
Convierte un campo de viento como 'Norte  3' en (direccion, velocidad). Contempla el caso 'Calma' (sin velocidad numérica).
### f3:
Devuelve la cantidad total de ciudades leídas.
### f4:
Devuelve la cantidad de ciudades sin ningún dato faltante.
### f5:
Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor (o al revés). Reutilizable tanto para temperatura como para viento.
### f6:
Imprime por pantalla las características solicitadas.
### f7:
Devuelve la/s ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima.
### f8:
Devuelve la/s ciudad(es)[:n] con velocidades máximas y mínimas de viento.



