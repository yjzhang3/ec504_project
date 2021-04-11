# Goal: parse individual graph into adjacency list and set of vertices
# This only works for number not names
def add_vertex(v):
    global graph
    global vertices_list
    if v in graph:
        print("Vertex ", v, " already exists.")
    else:
        vertices_list = vertices_list + 1
        graph[v] = []

def add_edge(v_start, v_end, score):
    global graph
    # Validation of start vertex
    if v_start not in graph:
        print("Vertex ", v_start, "does not exist.")
    # Validation of end vertex
    elif v_end not in graph:
        print("Vertex ", v_end, " does not exist.")
    # Validated start and end vertices
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not 
    # imply that an edge exists between v2 and v1
    # for undirected graph: this can be fixed adding neighbor vertex
    # to both start and end vertex
    else:
        temp = [v_end, score]
        graph[v_start].append(temp)

def print_graph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print (vertex, " -> ", edges[0], " edge weight: ", edges[1])



# Main driver code
graph = {}

# Store vertices in vertices_list
vertices_list = 0

# Generalized vertex set, can replace with any protein names
add_vertex(1)
add_vertex(2)
add_vertex(3)
add_vertex(4)

# Add score between vertcies by specifying
# Start vertex, End vertex, Score <--- Fromat

add_edge(1, 2, 1)
add_edge(1, 3, 1)
add_edge(2, 3, 3)
add_edge(3, 4, 4)
add_edge(4, 1, 5)
print_graph()
print("Internal representation: ", graph)
print("vertices: ", vertices_list)