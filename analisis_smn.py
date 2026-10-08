from funciones import salida_f6
import sys

try :
    with open (sys.argv[1], encoding = 'cp1252') as f:
        salida_f6()
except Exception:
        print ("Ingrese datos validos")
