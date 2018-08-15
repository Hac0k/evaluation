#        [[3], 
#        [1, 0], 
#       [3, 2, 7],
#      [3, 1, 10, 2],
#     [3, 4, 8, 5, 4],
#    [0, 0, 7, 3, 10, 0],
#   [5, 6, 5, 0, 3, 0, 7],
#  [1, 8, 1, 7, 6, 1, 0, 5],
# [8, 1, 4, 3, 8, 9, 0, 9, 10]]
# import copy
# [[1,2],
#  [3,4]]
triangle =[]
nombre ="exercise.txt"
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
memo={}
def memoize(function):
    # memo = {}
    def wrapper(*args):
      if args in memo:
        return memo[args]
      else:
        rv = function(*args)
        memo[args] = rv
        return rv
    return wrapper


temp_x=[]
temp_y=[]
@memoize
def evaluationTree(x, y):
	
	temp_x.append(x)
	temp_y.append(y)
	# acer=max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))
	# tem.append(acer)
	# ans = triangle[y][x] + max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))
	# ans = sum(tem)
	# print tem
		
	if y  == len(triangle) or x>y: 
		return 0
	return triangle[y][x] + max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))


# print evaluationTree(0,0)


def total(tem=[]):
	total= evaluationTree(0,0)
	print memo
	# if tem == []:
	# 	tem.append(triangle[0][0])
	print total
	print "x values "
	print temp_x
	print "y values "
	print temp_y
	print "numeracion de "
	for x,y in zip(temp_x,temp_y):
		print triangle[y][x]
	# 	if x < len(triangle[-1]) or  y < len(triangle[-1]):
		# tem.append(triangle[y][x])
	# for i in range(0,len(triangle)):
	# 	acer=max(evaluationTree(x, i), evaluationTree(x+1, i))
	# 	# acer=acer/len(triangle[i])
	# 	tem.append(acer)
	return tem,total
print total()