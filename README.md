## Notas del proyecto:

Para iniciar, ejecutar en la consola (a modo de ejemplo):
```bash
python3 analisis_smn.py estado_tiempo20260910.txt
```
El proyecto contiene 8 funciones en total. Al ejecutar " ~$ python3 analisis_smn.py estado_tiempo20260910.txt analisis_smn.py "; el módulo analisis_smn.py, llama a la función salida_f6 del archivo funciones.py Esta función solicita los parámetros necesarios (empleando int(input('texto'))), para las otras funciones. Luego  ejecuta a cada una de ellas y finalmente imprime en pantalla los valores solicitados según consignas del trabajo práctico.

El proyecto contiene 8 funciones en total:
```bash
salida_f1
salida_f2
salida_f3
salida_f4
salida_f5
salida_f6
salida_f7
salida_f8
```
## Descripción de las funciones:
### salida_f1:
Lee el archivo de observaciones del SMN y devuelve un diccionario  {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento ya separado en dirección  y velocidad.
### salida_f2:
Convierte un campo de viento como 'Norte  3' en (direccion, velocidad). Contempla el caso 'Calma' (sin velocidad numérica).
### salida_f3:
Devuelve la cantidad total de ciudades leídas.
### salida_f4:
Devuelve la cantidad de ciudades sin ningún dato faltante.
### salida_f5:
Devuelve las n (por parámetro) ciudades ordenadas según 'campo', de mayor a menor (o al revés). Reutilizable tanto para temperatura como para viento.
### salida_f6:
Imprime por pantalla las características solicitadas.
### salida_f7:
Devuelve la/s ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima.
### salida_f8:
Devuelve la/s ciudad(es)[:n] con velocidades máximas y mínimas de viento.



