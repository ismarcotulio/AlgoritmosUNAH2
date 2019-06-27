class Node:
	def __init__(self, item, next = None):
		self.item = item
		self.next = next

	def getItem(self):
		return self.item

	def getNext(self):
		return self.next

	def setItem(self, item):
		self.item = item

	def setNext(self, next):
		self.next = next



class LinkedList:
	def __init__(self, content = []):
		self.first = Node(None, None)
		self.last = self.first
		self.numItems = 0

	def getItem(self, index):
		if(index >= 0 and index < self.numItems):
			cursor = self.first
			for x in range(index):
				cursor = cursor.getNext()
			return cursor.getItem()
		

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
		print("")
		while cursor:
			if cursor.item:
				print(cursor.item.name)
			
			cursor = cursor.getNext()
			


class Person:
	def __init__(self, identity, name):
		self.name = name
		self.identity = identity


def main():
	Person1 = Person("Oscar",1)
	Person2 = Person("Juan",2)
	Person3 = Person("Daniel",3)
	Person4 = Person("Ricardo",4)
	Person5 = Person("Feo",5)
	Person6 = Person("Joao",6)
	Person7 = Person("Doggy",7)
	Person8 = Person("Rene",8)

	Persons = LinkedList()
	Persons2 = LinkedList()
	
	Persons.append(Person2)
	Persons.append(Person4)
	Persons.insert(Person1, 0)
	Persons.insert(Person3, 2)

	Persons2.append(Person6)
	Persons2.append(Person8)
	Persons2.insert(Person5, 0)
	Persons2.insert(Person7, 2)

	PersonsGroup = Persons2.add(Persons)

	item6 = PersonsGroup.getItem(7)

	print("")
	print(item6.name)

	Persons.printer()
	Persons2.printer()
	PersonsGroup.printer()



if __name__ == "__main__":
	main()