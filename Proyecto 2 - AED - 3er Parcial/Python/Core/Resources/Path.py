class Path:
	def __init__(self):
		self.paths = []

	def findPaths(self, graph, vertex, destination, path = [], visited = [], weight = 0):
		visited.append(vertex)
		path.append(vertex)
		if (vertex == destination):
			print()
			print("%s la ruta es: " %(path))
			self.paths.append(path)
		else:
			for k,v in graph:
				for k2,v2 in v:
					if(not k2 in visited):
						print(k2)
						self.findPaths(graph, k2, destination, path, visited, weight)
		path.pop()
		visited.pop()

