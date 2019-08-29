filename = "tree1.mem"
f = open(filename, "r")
content = f.read()

rows = content.split("\n")

tree = []

def FiletoMatrix(matrix = tree):
	matrix.append(eval('[' + FiletoMatrixInner() + ']'))

def FiletoMatrixInner(tabs=0, contador=0 , temp=[], array = rows):
	if contador < len(array):
		column = array[contador].split("\t")
		string = column[len(column)-1]

		if len(column)-1 < tabs:
			if string[len(string)-1] == "/":
				return "],"+"'"+str(string)+"'"+",["+str(FiletoMatrixInner(tabs-1,contador+1))
			else:
				return "],"+"'"+str(string)+"'"+","+str(FiletoMatrixInner(tabs,contador+1))

		elif len(column)-1 > tabs:
			if string[len(string)-1] == "/":
				return "'"+str(string)+"'"+",["+str(FiletoMatrixInner(tabs+1,contador+1))
			else:
				return "'"+str(string)+"'"+","+str(FiletoMatrixInner(tabs,contador+1))	

		else:
			if string[len(string)-1] == "/":
				return "'"+str(string)+"'"+",["+str(FiletoMatrixInner(tabs+1,contador+1))
			else:
				return "'"+str(string)+"'"+","+str(FiletoMatrixInner(tabs,contador+1))
 
	return "]"


FiletoMatrix(tree)
tree2 = tree[0]
print()

print(tree2)

print()

print(tree2[1][0])
print(tree2[1][1][1][1])
print(tree2[1][3][2])
print(tree2[1][4])
print(tree2[1][2])

f.close()
