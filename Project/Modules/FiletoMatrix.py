filename = "../Memory/Tree1.mem"
f = open(filename, "r")
content = f.read()

rows = content.split("\n")

tree = []

def FiletoMatrix(matrix = tree):
	matrix.append(eval('[' + FiletoMatrixInner() + ']'))

def FiletoMatrixInner(contador=0 ,tabs=0, array = rows):
	if contador < len(array):
		column = array[contador].split("\t")
		columnTabs = len(column)-1
		string = column[len(column)-1]
		if contador + 1 <len(array):
			columnNext = array[contador+1].split("\t")
			columnNextTabs = len(columnNext)-1
		else:
			columnNext = None
		if columnNext != None:
			if columnTabs < columnNextTabs:
				return "'"+str(string)+"',["+FiletoMatrixInner(contador+1)
			if columnTabs == columnNextTabs:
				if string[len(string)-1] != "/":
					return "'"+str(string)+"',"+FiletoMatrixInner(contador+1)
				else:
					return "'"+str(string)+"',[],"+FiletoMatrixInner(contador+1)					
			if columnTabs > columnNextTabs:
				return "'"+str(string)+"'"+"]"*(columnTabs-columnNextTabs)+","+FiletoMatrixInner(contador+1)
		else:
			return "'"+str(string)+"'"+"]"*columnTabs

FiletoMatrix(tree)
tree2 = tree[0]
print()

print(tree2)

print()

"""print(tree2[1][0])
print(tree2[1][1][1][1])
print(tree2[1][3][2])
print(tree2[1][4])
print(tree2[1][2])"""

f.close()
