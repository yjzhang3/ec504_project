# Goal: parse individual graph into adjacency matrix and set of vertices
# This works for protein names as well as scores 
# Resrouce: https://github.com/joeyajames/Python/blob/master/graph_adjacency-matrix.py 
# Vertex class to store all vertices 
class Vertex:
	def __init__(self, n):
		self.name = n

# Graph class for adjacency matrix
class Graph:
	vertices = {}
	edges = []
	edge_indices = {}
	
	# add vertex into graph
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			for row in self.edges:
				row.append(0)
			self.edges.append([0] * (len(self.edges)+1))
			self.edge_indices[vertex.name] = len(self.edge_indices)
			return True
		else:
			return False
	
	# add edges based on scores
	def add_edge(self, u, v, weight=1):
		if u in self.vertices and v in self.vertices:
			self.edges[self.edge_indices[u]][self.edge_indices[v]] = weight
			self.edges[self.edge_indices[v]][self.edge_indices[u]] = weight
			return True
		else:
			return False

	# print all vertices
	def print_this(self):
		for v, i in sorted(self.edge_indices.items()):
			print(v, end='') 	
		print(' ')		
	# print adjacency matrix 
	def print_graph(self):
		for v, i in sorted(self.edge_indices.items()):
			print(v + ' ', end='')
			for j in range(len(self.edges)):
				print(self.edges[i][j], end='')
			print(' ')   

# Main driver code
g = Graph()

# inserting vertices into list for adjacency matrix 
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

# input format will be: Protein1, Protein2, Score
# this is a generalization of what the input may be
edges = ['AB1', 'AE2', 'BF5', 'CG7', 'DE5', 'DH3', 'EH8', 'FG6', 'FI5', 'FJ2', 'GJ3', 'HI2']
for edge in edges:
	g.add_edge(edge[:1], edge[1:2], edge[2:])

g.print_this()
g.print_graph()
