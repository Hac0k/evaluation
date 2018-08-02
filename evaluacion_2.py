"""serie fibannci en reversa
[[3, 0, 0, 0, 0, 0, 0, 0, 0],
[1, 0, 0, 0, 0, 0, 0, 0, 0],
[3, 1, 7, 0, 0, 0, 0, 0, 0],
[3, 1, 10, 2, 0, 0, 0, 0, 0],
[3, 4, 8, 5, 4, 0, 0, 0, 0],
[0, 0, 7, 3, 10, 0, 0, 0, 0],
[5, 6, 5, 0, 3, 0, 7, 0, 0],
[1, 8, 1, 7, 6, 1, 0, 5, 0],
[8, 1, 4, 3, 8, 9, 0, 9, 10]]
el valor de ruta en un variable global para no afectar el funcionamiento 
el metodo dos es sencillo coger el valor anterior y sumarle lo sgts y ver cual que el mayor 
"""


entry =[]
nombre ="sample.txt"

#codigo de formato de archivo 
def archivo(nombre):
	global entry
	# archivo("sample.txt")
	archivo = open(nombre, "r")
	for linea in archivo.readlines():
		linea = [int(i) for i in linea.split()]
		entry.append(linea)
	archivo.close()
	return entry
entry=archivo(nombre)
# fomateo matriz
def format_matriz():
    global entry
    for lists in entry:
        while len(lists) < len(entry[-1]):
            lists.append(0)
        # entry.append(lists)
    
    return entry
# entry = format_matriz()

def Sub_P(l,e):
    global entry

    if len(entry[l]) < len(entry[-1]) :
        ant = entry[l][e]
        izq = entry[l+1][e]
        der = entry[l+1][e+1]
        if ant+izq > ant+der: 
            return izq
        else:
            
            return der

# print Sub_P(2,0)

"""cuatro parametro uno para la fila otr para la posicion del ellemento
"""
# def evaluation_tree(entry,len_matriz,):

def cont_por(l,value_route = [],elem=[0]):

    if len(entry[-1]) == l:
        return value_route,sum(value_route)
    else:
		pos_elemt=elem[-1]
		route_list,pos_elem = Sub_P(l,pos_elemt)
		elem.append(pos_elem)
		value_route.append(route_list)
    return cont_por(l+1)

	
print cont_por(0)