from Core.Python.Resources.Tree import *

class Memory:
	def __init__(self):
		self.textMatrix = ""
		self.matrix = []
		self.tree = Tree()

	def Load(self,filename):
		verify = self.FiletoMatrix(filename)
		if verify == True:
			self.MatrixtoTree(self.matrix[0][1])
		return verify

	def MatrixtoTree(self, matrix, tab = 0):
		for item in range(len(matrix)):
			if isinstance(matrix[item],list):
				self.MatrixtoTree(matrix[item], tab+1)
			else:
				if self.tree.root.children == None:
					self.tree.root.children = LinkedList()
				if matrix[item][len(matrix[item])-1] == "/":
					print("directorio")
					temp = len(matrix[item])
					name = matrix[item][:temp-1]
					print(name)
					self.tree.addChild(Directory_Node(name))
					self.tree.root = self.tree.root.children.getChild(name)
				else:
					print("archivo")
					print(matrix[item])
					self.tree.addChild(File_Node(matrix[item]))
		#if tab > 0:
		self.tree.root = self.tree.root.parent


	def FiletoMatrix(self, filename ="../Memory/Tree1.mem"):
		f = open(filename, "r")
		content = f.read()
		if content != "":
			rows = content.split("\n")
			self.matrix.append(eval('[' + self.FiletoMatrixInner(rows) + ']'))
			return True
		else:
			return False
		f.close()

	def FiletoMatrixInner(self, array, contador=0):
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
					return "'"+str(string)+"',["+self.FiletoMatrixInner(array,contador+1)
				if columnTabs == columnNextTabs:
					if string[len(string)-1] != "/":
						return "'"+str(string)+"',"+self.FiletoMatrixInner(array,contador+1)
					else:
						return "'"+str(string)+"',[],"+self.FiletoMatrixInner(array,contador+1)						
				if columnTabs > columnNextTabs:
					return "'"+str(string)+"'"+"]"*(columnTabs-columnNextTabs)+","+self.FiletoMatrixInner(array,contador+1)
			else:
				return "'"+str(string)+"'"+"]"*columnTabs


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
				self.textMatrix += "],"
		else:
			self.textMatrix += "'"+str(node.name)+"',"
