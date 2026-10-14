import sys
from analisis_smn import f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, aux_fecha_y_hora, aux_viento, aux_filtro
lista = sys.argv
error = 0
try:
    with open (sys.argv[1], encoding = 'cp1252') as f:
        datos_SMN = [i for i in f]
    Diccionario = f1(datos_SMN)
    funcion = sys.argv[2]
    if funcion == 'f1':
        print (f' f1: \n (entrega diccionario de las ciudades con columnas completas): \n {f1(datos_SMN)} \n \n')
    elif funcion == 'f2':
        print (f' f2: \n (entrega separado el campo direccion y velocidad del viento) \n {f2(Diccionario)} \n \n')
    elif funcion == 'f3':
        print (f' f3: \n (devuelve la cantidad total de ciudades leídas) \n {f3(Diccionario)} \n \n')
    elif funcion == 'f4':
        print (f' f4: \n (devuelve la cantidad de ciudades sin ningún dato faltante) \n {f4(Diccionario)} \n \n')
    elif funcion == 'f5':
        if len(lista) != 6:
            error = 2
            int('h') 
        print (f' f5: \n (devuelve el top n de ciudades) \n {f5(Diccionario,int(lista[3]),int(lista[4]),int(lista[5]))} \n \n')
    elif funcion == 'f7':
        print (f' f7: \n (devuelve la/s ciudad(es)[:n] con la temperatura máxima y con la temperatura mínima) \n {f7(Diccionario,int(lista[3]))} \n \n') 
    elif funcion == 'f8':
        print (f' f8: \n (devuelve la/s ciudad(es)[:n] con velocidades máximas y mínimas de viento) \n {f8(Diccionario,int(lista[3]))} \n \n') 
    elif funcion == 'f9':
        print (f' f9: \n (muestra la cantidad de datos faltantes por campo, y en qué estaciones ocurre) \n {f9(datos_SMN)} \n \n')
    elif funcion == 'f10':
        print (f' f10: \n (devuelve un diccionario con la cantidad de columnas esperadas que no están presentes en alguna fila, según su ciudad. También indica que ciudades tienen completas sus columnas) \n {f10(datos_SMN)}' )
    else:
        error = 1
        int('h')    
except Exception:
    if error == 0:     
        print ('Error')
    elif error == 1:
        print ('Ingrese un nombre de funcion valido')
    elif error == 2:
        print ('Ingrese los argumentos correctos para la funcion f5 ejemplo: f5 2 4 3')
