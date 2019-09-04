from Resources.Tree import *

class Memory:
	def __init__(self):
		self.textMatrix = ""
		self.matrix = []
		self.tree = ["root/",["archivo1/",["archivo1.1/",["archivo1.1.1","archivo1.1.2"],"archivo1.2"],"archivo2/",["archivo2.2"],"archivo3"]]

	def FiletoMatrix(self, filename ="../Memory/Tree1.mem"):
		f = open(filename, "r")
		content = f.read()
		rows = content.split("\n")
		self.matrix.append(eval('[' + FiletoMatrixInner(rows) + ']'))
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


	def MatrixToFile(self, filename = "Memory/Tree1.mem"):
		f = open(filename, "w+")
		self.MatrixToFileInner(self.matrix, f)
		f.close()

	def MatrixToFileInner(self,matrix, f ,tab = 0):
		for item in range(len(matrix)):
			if isinstance(matrix[item],list):
				self.MatrixToFileInner(matrix[item], f, tab+1)
			else:
				if tab != 0:
					f.write("\n")
				f.write("\t"*tab+str(matrix[item]))


	def TreeToMatrix(self, node):
		self.TreeToMatrixInner(node)
		self.textMatrix += "]"
		self.matrix.append(eval('' + self.textMatrix + ''))
		self.matrix = self.matrix[0]


	def TreeToMatrixInner(self, node):
		if isinstance(node,Directory_Node) == True:
			queue = []
			if node.name == "/":
				self.textMatrix += "['"+str(node.name)+"',["
			else:
				self.textMatrix += "'"+str(node.name)+"/',["
			if node.children != None:
				current = node.children.first
				while current != None:
					queue.append(current)
					current = current.next
				for i in range(len(queue)):
					self.TreeToMatrixInner(queue[i])
				self.textMatrix += "],"
			else:
				self.textMatrix += "]"
		else:
			self.textMatrix += "'"+str(node.name)+"',"
