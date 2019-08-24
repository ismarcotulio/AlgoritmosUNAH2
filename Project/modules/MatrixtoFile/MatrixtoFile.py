tree = ["root/",["archivo1/",["archivo1.1/",["archivo1.1.1","archivo1.1.2"],"archivo1.2"],"archivo2/",["archivo2.2"],"archivo3"]]
tree2 = [1,2,3]
filename = "tree1.mem"
f = open(filename, "w+")

def toFile(matrix = tree,tab = 0,fopen = f):
	for item in range(len(matrix)):
		if isinstance(matrix[item],list):
			toFile(matrix[item],tab+1)
		else:
			if tab != 0:
				f.write("\n")
			f.write("\t"*tab+str(matrix[item]))

toFile()
f.close()