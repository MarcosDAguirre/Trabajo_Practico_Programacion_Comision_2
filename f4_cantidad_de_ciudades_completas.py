
def salida_f4(dato):
	salida = {}
	contador = 0
	with open (dato, encoding = 'cp1252') as f:
		for i in f:
			linea = i.split(';')
			clave = linea[0].strip()  # clave es una ciudad.
			valor_s_termica = linea[6]
			try:
				float(valor_s_termica)
				contador += 1
			except (ValueError):
				pass
	return contador