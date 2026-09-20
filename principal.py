import sys

datos_SMN = sys.argv[1]

salida = {}              # fecha y hora en datetime
with open (datos_SMN, encoding = 'cp1252') as f:
    for i in f:
        linea = i.split(';')
        print (linea)
        clave = linea[0].strip()  # clave es una ciudad.
        fecha = linea[1]
        hora = linea[2]
        c_cielo = linea[3]
        visibilidad = linea[4]
        temperatura = float(linea[5])
        s_térmica = linea[6]
        humedad = linea[7]
        viento = linea[8]
        presion = linea[9].strip()

        salida[clave] = {'Fecha':fecha,'Hora':hora,'Condición del cielo':c_cielo,'Visibilidad':visibilidad,'Temperatura':temperatura,'Sensación térmica':s_térmica,'Humedad':humedad,'Viento':viento,'Presión':presion}
print (salida)        

print (salida['Azul']['Visibilidad'])
