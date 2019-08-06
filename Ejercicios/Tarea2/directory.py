from contact import *

class BinaryNode:
	def __init__(self,value):
		self.value = value
		self.right = None
		self.left = None
		
class Directory:
	def __init__(self, name):
		self.name = name
		self.root = None

	def BSTAdd(self,value):
		if (not self.root):
			self.root = BinaryNode(value)
		else:
			self.BSTAddInner(value,self.root)

	def BSTAddInner(self, value, current):
		if (current.value.phoneNumber > value.phoneNumber):
			if(not current.left):
				current.left = BinaryNode(value)
			else:
				self.BSTAddInner(value,current.left)
		elif (current.value.phoneNumber < value.phoneNumber):
			if(not current.right):
				current.right = BinaryNode(value)
			else:
				self.BSTAddInner(value,current.right)

	def BSTSearch(self,value):
		return self.BSTSearchInner(value,self.root)

	def BSTSearchInner(self, value, current):
		if(not current):
			return False
		else:
			if (current.value.phoneNumber == value):
				return True
			elif (current.value.phoneNumber > value):
				return self.BSTSearchInner(value, current.left)
			elif (current.value.phoneNumber < value):
				return self.BSTSearchInner(value, current.right)


	def minValueNode(self,current):  
		while(current.left): 
			current = current.left  
		return current

	def BSTDelete(self,value):
		return self.BSTDeleteInner(value, self.root)

	def BSTDeleteInner(self,value,current): 

		if (current is None):
			print ("El nodo seleccionado no existe") 
			return current
		

		if (value < current.value.phoneNumber): 
			current.left = self.BSTDeleteInner(value,current.left) 
		elif(value > current.value.phoneNumber): 
			current.right = self.BSTDeleteInner(value,current.right) 
		else: 
			


			if (current.left is None): 
				temp = current.right  
				current = None 
				print ("Nodo eliminado con exito")
				return temp  
			elif (current.right is None): 
				temp = current.left  
				current = None
				print("Nodo eliminado con exito")
				return temp 
			
			temp = self.minValueNode(current.right) 
			current.value = temp.value 
			current.right = self.BSTDeleteInner(temp.value.phoneNumber, current.right) 
		
		return current

	def menuDirectory(self):
		print("Que desea hacer?")
		print("1-Crear Contacto")
		print("2-Eliminar Contacto")
		print("3-buscar contacto")
		print("4-regresar")
		print(" ")
		choise = input("Opcion: ")
		self.mapMenuDirectory(choise)
	


	def mapMenuDirectory(self, choise):
		
		switcher = {
			"1":self.newContact,
			"2":self.deleteContact,
			"3":self.searchContact,
			"4":self.back
		}
		funct = switcher.get(choise, lambda: self.menuDirectory())
		print(funct())
			

	def newContact(self):
		name = input("Ingrese el nombre del contacto: ")
		lastname = input("Ingrese el apellido del contacto: ")
		phone = input("Ingrese el numero telefonico del contacto: ")
		contact = Contacts(name, lastname, phone)
		self.BSTAdd(contact)
		print(" ")
		self.menuDirectory()

	def deleteContact(self):
		phone = input("Ingrese el numero de telefono del contacto a eliminar: ")
		self.BSTDelete(phone)
		print(" ")
		self.menuDirectory()

	def searchContact(self):
		phone = input("Ingrese el numero de telefono del contacto a buscar: ")
		print(self.BSTSearch(phone))
		print(" ")
		self.menuDirectory()

	def back(self):
		print(" ")

