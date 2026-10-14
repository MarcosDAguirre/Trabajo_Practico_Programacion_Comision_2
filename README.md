## Notas del proyecto:

Para iniciar, ejecutar en la consola (a modo de ejemplo):
```bash
python3 analisis_smn.py estado_tiempo20260910.txt
```
o 

```bash
python3 analisis_smn.py para_prueba.txt
```
Al ejecutar estos comandos se ejecuta la funcion f6, la cual muestra la salida de todas las funciones en pantalla (excepto las funciones aux).

Para ejecutar el archivo llamada_a_funciones.py; en la consola se debe ingresar la funcion que se quiere visualizar, seguido de los parametros necesarios.

```bash
python3 llamada_a_funciones.py para_prueba.txt f1
python3 llamada_a_funciones.py para_prueba.txt f2
python3 llamada_a_funciones.py para_prueba.txt f3
python3 llamada_a_funciones.py para_prueba.txt f4
python3 llamada_a_funciones.py para_prueba.txt f5 (1 o 2) (3 o 4) (n)    "Nota  1:temperatura, 2:viento,3: ascendente, 4:descendente, n: cantidad de ciudades"
python3 llamada_a_funciones.py para_prueba.txt f7 (n)    "Nota  n: cantidad de ciudades"
python3 llamada_a_funciones.py para_prueba.txt f8 (n)    "Nota  n: cantidad de ciudades"
python3 llamada_a_funciones.py para_prueba.txt f9
python3 llamada_a_funciones.py para_prueba.txt f10
```

Al ejecutar:

```bash
python3 llamada_a_funciones.py para_prueba.txt f5 1 3 6
```
la funcion f5 muestra el top 6 de ciudades, organizadas en forma ascendente segun sus temperaturas.

El proyecto contiene las siguientes funciones:
```bash
f1
f2
f3
f4
f5
f6
f7
f8
f9
f10
aux_fecha_y_hora
aux_viento
aux_filtro
```
## Descripción de las funciones:
### f1:
Lee una lista (datos_SMN) con los datos del archivo de observaciones del SMN (.txt) y devuelve un diccionario {ciudad: datos}, con los nombres de ciudad limpios y el campo de viento ya separado en dirección y velocidad. La fecha y hora los entrega unificados en tipo datetime (para trabajar a futuro con este dato es conveniente dejarlo de esta manera); y también separados en fecha y hora. Para mejorar la comprension de la función, se incorporaron las funciones aux_viento y aux_fecha_y_hora para que trabajen con esta función. Si a cada una de las filas correspondientes a una ciudad le falta alguna columna, no es incorporada al diccionario.
### f2:
Convierte un campo de viento como 'Norte  3' en (direccion, velocidad). Contempla el caso 'Calma' (sin velocidad numérica). Si su valor es 'Calma', se asigna a la direccion del viento, el valor 'Inexistente' y a su velocidad 0.0. Si el valor de la dirección es 'Direcciones variables' se le asigna el valor 'Variable' y se toma el valor de su velocidad sin modificaciones.
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
### f9:
 Muestra la cantidad de datos faltantes por campo, y en qué estaciones ocurre. 'No se calcula' en Sensación Térmica se considera dato faltante'."Nota" : lista_de_campos: 'Fecha','Hora','Condicion_del_cielo','Visibilidad','Temperatura','Sensacion_termica','Humedad','Viento','Presion'. Calma se toma como dato presente (Direccion inexistente y velocidad del viento 0).
### f10:
Devuelve un diccionario con la cantidad de columnas esperadas que no están presentes en alguna fila (según su ciudad). También indica que ciudades tienen completas sus columnas.
### aux_fecha_y_hora:
Entrega fecha y hora en formato datetime(Y,m,d,H,M). Es utilizada por la función f1.
### aux_viento:
Devuelve una lista con los datos de direccion y velocidad del viento. Es utilizada por la función f1.
### aux_filtro:
Filtra los datos para obtener la cantidad de datos de Temperatura y Sensacion_termica presentes en cada fila (cada una de las filas corresponde a una ciudad). Es utilizada por la función f9.