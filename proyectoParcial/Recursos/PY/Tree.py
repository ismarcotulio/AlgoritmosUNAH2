import * from LinkedList

class Tree:
	def __init__(self):
		self.root = LinkedList()

    def add(self, value, parent = self.root):
        parent.add(value);
    