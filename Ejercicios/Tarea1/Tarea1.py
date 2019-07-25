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

class Box:
	def __init__(self):
		self.first = None


	def addPosition(self, value, n = 0):
		current = self.first
		max = 0

		while(current):
			current = current.next
			max++

		n = math.floor(math.random()*max)

		count = 0

		if n == 0:
			queue = self.first
			self.first = new Node(value):
			self.first.next = queue
			max++
		else if n > 0:
			before = current = self.first
			
			while current:
				count++
				current = current.next

				if n == count:
					before.next = new Node(value)
					before.next.next = current
					max++

				before = before.next

		

	def print(self):
		pass


	def main():
		caja 1 = Box()

	if __name__ == "__main__":
		main():