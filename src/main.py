from GraphAdjList import *
from matrix import *
# the location of the file, relative to where we compile the program
# file1_location = "./data/9606_protein.txt"
# file2_location = "./data/9606_protein.txt"

# testing with small dataset
file1_location = "./data/set2_b.txt"
file2_location = "./data/set2_a.txt"

# making grpah1 and graph2, reading information from the provided file

graph1, graph2 = make_graph(file1_location, file2_location)
print("Making graph: done")
# print(neighbors(graph1, 1))

# a, b, lambda should be between 0 and 1
a = 1
b = 0
lamb_da = 0.5

# called the alignment function
result = align(graph1, graph2, a, b, lamb_da)
### result is a dictionary, {id_in_graph1 : id_in_graph2}, basically a bunch of matching between i,j

### TO DO:
### calculate the performance score, using alignment

print(result)

# save result into .json file
# which the frontend will read later
