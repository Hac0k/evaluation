#        [[3], 
#        [1, 0], 
#       [3, 2, 7],
#      [3, 1, 10, 2],
#     [3, 4, 8, 5, 4],
#    [0, 0, 7, 3, 10, 0],
#   [5, 6, 5, 0, 3, 0, 7],
#  [1, 8, 1, 7, 6, 1, 0, 5],
# [8, 1, 4, 3, 8, 9, 0, 9, 10]]
entry =[]
nombre ="sample.txt"
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
print entry
def format_matriz():
    global entry
    for lists in entry:
        while len(lists) < len(entry[-1]):
            lists.append(0)
        # entry.append(lists)
    
    return entry
elem=[0]
def evaluation_tree(n,route=[]):
	global entry,elem
	if n ==len(entry[-1]):
		return route, sum(route)
	else:
		pos_elemt=elem[-1]
		route_list = sub_p(n,pos_elemt)
		route.append(route_list)
		return evaluation_tree(n+1)	

def sub_p(posList,ele):
    global entry
    for x in entry:
        for i in x:
            print i
