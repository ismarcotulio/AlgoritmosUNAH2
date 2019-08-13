import * from Node

class LinkedList:
	def __init__(self):
		self.first = None
	
	def add(self, value):
		if(self.first == None):
			self.first = Node(value)
		else:
			var compare = new Compare();
			if (compare.compare(self.first, value)>0):
				stack = self.first
				self.first = Node(value)
				self.first.next = stack
				return true
			else if(compare.compare(self.first,value)==0):
				stack = self.first.next
				self.first = Node(value)
				self.first.next = stack
				return true
			else: 
				previous = self.first
				current = self.first.next

				while (current):
					if(compare.compare(current,value)<0):
						previous = current
						current = current.next
						return true
					else if (compare.compare(current,value)>0):
						var stack = current
						previous.next = Node(value)
						previous.next.next = stack
						return true
					else:
						previous.next = Node(value)
						previous.next.next = current.next
						return true
					
				

				previous.next = Node(value)
				return true
			
		
			


