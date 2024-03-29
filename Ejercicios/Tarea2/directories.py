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
			"1":self.newDirectory,
			"2":self.deleteDirectory,
			"3":self.editDirectory,
			"4":quit
		}
		funct = switcher.get(choise,lambda: self.menuDirectories() )
		print(funct())
			

	def newDirectory(self):
		name = input("Ingrese el nombre del directorio: ")
		directory = Directory(name)
		self.append(directory)
		print("Directorio Creado Exitosamente")
		print(" ")
		self.menuDirectories()

	def deleteDirectory(self):
		print("proximamente")
		print("")
		self.menuDirectories()

	def editDirectory(self):
		self.printer()
		print(" ")
		choise = input("directorio a editar: ")
		directory = self.getItem(int(choise))
		if directory == False and directory == None:
			print("directorio no encontrado")
			print(" ")
			self.menuDirectories()
		else:
			print("directorio encontrado")
			print(" ")
			directory.menuDirectory()
			self.menuDirectories()	
