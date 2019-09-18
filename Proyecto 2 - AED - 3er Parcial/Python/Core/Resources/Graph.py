class Graph:
	def __init__(self):
		self.vertex = LinkedList()

	def add_vertex(self, vertex_name):
		self.vertex.add(Vertex(vertex_name))

	def add_edge(self, vertex_origin, vertex_destination):
		pass

	def connectedVertices(self, x):
		pass