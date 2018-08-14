
triangle =[]
nombre ="sample.txt"
def archivo(nombre):
	global triangle
	# archivo("sample.txt")
	archivo = open(nombre, "r")
	for linea in archivo.readlines():
		linea = [int(i) for i in linea.split()]
		triangle.append(linea)
	archivo.close()
	return triangle
triangle=archivo(nombre)