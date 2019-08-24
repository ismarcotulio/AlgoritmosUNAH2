filename = "tree1.mem"
f = open(filename, "r")
content = f.read()

rows = content.split("\n")


def FileToMatrix(array = rows, tab = 0):
	for row in range(len(array)):
		column = array[row].split("\t")
		if len(column)-1>tab :
			print(str(len(column)-1)+" es mayor que "+str(tab))
			print(column[len(column)-1])
			temp = []
			temp.append(column[len(column)-1])
			print("matrix actual"+matrix[tab])

			tab += 1
			matrix[tab].append(temp)


		elif len(column)-1<tab:
			print(str(len(column)-1)+" es menor que "+str(tab))
			print(column[len(column)-1])
			tab -= 1
		else:
			print(str(len(column)-1)+" es igual que "+str(tab))
			print(column[len(column)-1])
			if tab==0:
				matrix.append(column[len(column)-1])
			else:
				matrix[tab].append(column[len(column)-1])


def toMatrix(tabs=0, contador=0 , matrix=[], array = rows):
	if contador < len(array):
		column = array[contador].split("\t")
		string = column[len(column)-1]
		
		if len(column)-1 < tabs:
			if string[len(string)-1] == "/":
				print(string)
				matrix.append(string)
				matrix.append([])
				toMatrix(tabs-1,contador+1,matrix[1])
			else:
				matrix.append(string)
				toMatrix(tabs-1,contador+1,matrix)


		elif len(column) > tabs:
			if string[len(string)-1] == "/":
				print(string)
				matrix.append(string)
				matrix.append([])
				toMatrix(tabs+1,contador+1,matrix[1])
			else:
				matrix.append(string)
				toMatrix(tabs+1,contador+1,matrix)


		else:
			if string[len(string)-1] == "/":
				print(string)
				matrix.append(string)
				matrix.append([])
				toMatrix(tabs+1,contador+1,matrix[1])
			else:
				matrix.append(string)
				toMatrix(tabs,contador+1,matrix)
 
	else:
		print("fin")
		return matrix


	








matrix = toMatrix()
print(matrix)

f.close()
