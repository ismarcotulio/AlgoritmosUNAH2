class LinkedList:
	def __init__(self):
		self.first = None

		def __str__(self):
			current = self.first
			r = []
			while(current):
				r.append(current.value.name)
				current = current.next
			return ",".join(r)

		def add(self, value):
			if not self.first:
				self.first = Node(value)
				return True
			else:
				if alreadyExist() == False:
					current = self.first

					while(current.next):
						current = current.next

					current.next = Node(value)

		def alreadyExist(self, value):
			current = self.first
			while(current):
				if current.value.name == value.name:
					return True
				current = current.next
			return False