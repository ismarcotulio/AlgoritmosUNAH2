class Memory:
	def __init__(self):
		self.matrix = []
		self.tree = ["root/",["archivo1/",["archivo1.1/",["archivo1.1.1","archivo1.1.2"],"archivo1.2"],"archivo2/",["archivo2.2"],"archivo3"]]



	def FiletoMatrix(self, matrix = self.matrix, filename ="../Memory/Tree1.mem"):
		f = open(filename, "r")
		content = f.read()
		rows = content.split("\n")
		matrix.append(eval('[' + FiletoMatrixInner(rows) + ']'))
		self.matrix = matrix[0]
		f.close()

	def FiletoMatrixInner(self, array, tabs=0, contador=0 , temp=[]):
		if contador < len(array):
			column = array[contador].split("\t")
			string = column[len(column)-1]

			if len(column)-1 < tabs:
				if string[len(string)-1] == "/":
					return "],"+"'"+str(string)+"'"+",["+str(FiletoMatrixInner(array, tabs-1,contador+1))
				else:
					return "],"+"'"+str(string)+"'"+","+str(FiletoMatrixInner(array, tabs,contador+1))

			elif len(column)-1 > tabs:
				if string[len(string)-1] == "/":
					return "'"+str(string)+"'"+",["+str(FiletoMatrixInner(array, tabs+1,contador+1))
				else:
					return "'"+str(string)+"'"+","+str(FiletoMatrixInner(array, tabs,contador+1))	

			else:
				if string[len(string)-1] == "/":
					return "'"+str(string)+"'"+",["+str(FiletoMatrixInner(array, tabs+1,contador+1))
				else:
					return "'"+str(string)+"'"+","+str(FiletoMatrixInner(array, tabs,contador+1))
	 
		return "]"


	def MatrixToFile(self, filename = "../Memory/Tree1.mem"):
		f = open(filename, "w+")
		self.MatrixToFileInner(self.tree, 0, f)
		f.close()

	def MatrixtoFileInner(matrix,tab = 0,fopen):
		for item in range(len(matrix)):
			if isinstance(matrix[item],list):
				toFile(matrix[item],tab+1,fopen)
			else:
				if tab != 0:
					f.write("\n")
				f.write("\t"*tab+str(matrix[item]))

