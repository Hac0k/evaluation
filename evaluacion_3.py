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

def memoize(function):
    memo = {}
    def wrapper(*args):
      if args in memo:
        return memo[args]
      else:
        rv = function(*args)
        memo[args] = rv
        return rv
    return wrapper



@memoize
def evaluationTree(x, y,tem=[]):
	if y  == len(triangle) or x>y: 
		print tem
		return 0
	# else:
		# if tem == []:
		# 	tem.append(triangle[y][x])
		# acer=max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))
		# tem.append(acer)
		# ans = sum(tem)
		# # ans = triangle[y][x] + max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))
		# print tem
	return triangle[y][x] + max(evaluationTree(x, y+1), evaluationTree(x+1, y+1))


print evaluationTree(0,0)