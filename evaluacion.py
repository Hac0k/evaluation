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
nombre ="test.txt"
# pos_in_list = next_value()
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
print entry
def format_matriz():
    global entry
    for lists in entry:
        while len(lists) < len(entry[-1]):
            lists.append(0)
        # entry.append(lists)
    
    return entry
# entry = format_matriz()
#sub-structure para analizar los datos 
# def analitic(pos_list):
# 	global entry
# 	lists = entry[pos_list]
# 	# numero para las sgts posiciones
# 	# brute force code 
# 	# 	for lists in entry:
# # 		i=0
# # 		if len(lists) != 1:
# # 			if lists[i]>lists[i+1]:
# # 				return lists[i]
# # 			else:
# # 				return lists[i+1]
# # 		if len(lists) != 1:
# # 			return lists[0]
# # 		i+=1
# # '''-----------------------------------------------'''
# 	# aqui es quue tiene que ocurrir la magia
# 	if len(lists) <= len(entry[-1]):
# 		route_list,pos_elem next_value(lists)
# 		return route_list
		
	# if len(lists) == len(entry[-1]):
	# 	return next_value(lists,pos_list)
# pos_in_list = next_value()
elem=[0]
def next_value(pos_list,pos_in_list):
	global entry
	lists = entry[pos_list]
	# if len(lists) != 1:
		# print "elemento actual "+str(lists[pos_in_list]) + (" " * 10) + str(lists[pos_in_list])+ " < o > " +" "+str(lists[pos_in_list+1])
	if len(lists) == 1:
		return lists[0]
	else:
		if lists[pos_in_list] > lists[pos_in_list+1]:
			elem.append(pos_in_list)
			return lists[pos_in_list]#''',pos_in_list'''

		else:
			elem.append(pos_in_list +1)
			return lists[pos_in_list+1]#''',pos_in_list +1'''

def evaluation_tree(n,route=[]):
	# para mover listas
	global entry,elem
	if n ==len(entry[-1]):
		return route, sum(route)
	else:
		pos_elemt=elem[-1]
		# route_list""",pos_elem""" = next_value(n,pos_elemt)
		route_list = next_value(n,pos_elemt)
		# elem.append(pos_elem)
		route.append(route_list)
		# print route
		return evaluation_tree(n+1)	
	
	# if pos[i] != int():
	# 	return 1
	# else:




print evaluation_tree(0)