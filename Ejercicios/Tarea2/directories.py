from node import *
from directory import *

class Directories:
	def __init__(self, content = []):
		self.first = Node(None, None)
		self.last = self.first
		self.numItems = 0

	def getItem(self, index):
		if(index >= 0 and index <= self.numItems):
			cursor = self.first
			for x in range(index):
				cursor = cursor.getNext()
			return cursor.getItem()
		else:
			return False
		

	def setItem(self, index, item):		
		if(index >= 0 and index < self.numItems):
			cursor = self.first
			for x in range(index):
				cursor = cursor.getNext()
			cursor.setItem(item)

	def add(self, other):
		ll = LinkedList()
		cursor = other.first
		while(cursor != None):
			ll.append(cursor.getItem())
			cursor =  cursor.getNext()
		cursor = self.first
		while(cursor != None):
			if cursor.getItem() != None:
				ll.append(cursor.getItem())
			cursor = cursor.getNext()
		return ll


	def append(self, item):
		cursor = self.first
		if(cursor.getNext() != None):
			while(cursor.getNext() != None):
				cursor = cursor.getNext()
			cursor.setNext(Node(item))
			self.numItems += 1

			
		else:
			cursor.setNext(Node(item))
			self.numItems += 1

	def insert(self, item, index):
		if(index < self.numItems):
			cursor = self.first
			for i in range(index):
				cursor = cursor.getNext()


			#print("el cursor es "+str(cursor.item.name))
			#print("el numero de objetos es "+str(self.numItems))
			#print("el index es "+str(index))
			node = Node(item, cursor.getNext())
			cursor.setNext(node)
			self.numItems += 1
		else:
			self.append(item)

	def printer(self):
		cursor = self.first
		i = 0
		print("")
		while cursor:
			if cursor.item:
				print(str(i)+"-"+str(cursor.item.name))
			
			i = i + 1
			cursor = cursor.getNext()

	def menuDirectories(self):
		print("Que desea hacer?")
		print("1-Crear Directorio")
		print("2-Eliminar Directorio")
		print("3-Editar directorio")
		print("4-salir")
		print(" ")
		choise = input("Opcion: ")
		self.mapMenuDirectories(choise)
	


	def mapMenuDirectories(self, choise):
		
		switcher = {
			1:self.newDirectory,
			2:self.deleteDirectory,
			3:self.editDirectory,
			4:quit
		}
		funct = switcher.get(choise)
		print funct()
			

	def newDirectory(self):
		name = raw_input("Ingrese el nombre del directorio: ")
		directory = Directory(name)
		self.append(directory)
		print("Directorio Creado Exitosamente")
		print(" ")
		self.menuDirectories()

	def deleteDirectory(self):
		pass

	def editDirectory(self):
		self.printer()
		print(" ")
		choise = input("directorio a editar: ")
		directory = self.getItem(choise)
		if directory == False and directory == None:
			print("directorio no encontrado")
			print(" ")
			self.menuDirectories()
		else:
			print("directorio encontrado")
			print(" ")
			directory.menuDirectory()
			self.menuDirectories()	
