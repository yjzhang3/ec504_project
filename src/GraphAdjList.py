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
    # print adj list into a text file as output
    sample = open('AdjListOutput.txt', 'w')
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print (vertex, " -> ", edges[0], " edge weight: ", edges[1], file = sample)



# Main driver code
graph = {}

# Store vertices in vertices_list
vertices_list = 0

# Reading into the protein file that can be obtained from string-db.org
# The following example is Homo Sapiens: https://string-db.org/cgi/download?sessionId=%24input-%3E%7BsessionId%7D&species_text=Homo+sapiens
fileget = open ('9606.protein.links.v11.0.txt', 'r')
next(fileget) # ignoring the first line of input
count = 0

protein_map = {} # a map that maps protein id to numbers

for line in fileget:
    # Add score between vertcies by specifying
    # Start vertex, End vertex, Score <--- Fromat
    protein1, protein2, score = line.strip().split()
    if (protein1 not in protein_map):
        # Making sure the map has unique proteins, no repetitive
        protein_map[protein1] = count
        add_vertex(count)
        count += 1
    if (protein2 not in protein_map):
        # Making sure the map has unique proteins, no repetitive
        protein_map[protein2] = count
        add_vertex(count)
        count += 1
    # Add each edge into graph for adj list
    add_edge(protein_map[protein1], protein_map[protein2], score)
print_graph()