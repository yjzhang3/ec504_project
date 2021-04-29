import sys

from GraphAdjList import *
from matrix import *

### default file location
file1_location = "./data/set3_a.txt"
file2_location = "./data/set3_b.txt"

if len(sys.argv) > 1:
    if sys.argv[1] == 's':
        if sys.argv[2].isdigit():
            file1_location = "./data/set" + sys.argv[2] + "_a.txt"
            file2_location = "./data/set" + sys.argv[2] + "_b.txt"
        else:
            print("argument after \'s\' need to be digit")
            exit(1)
    elif sys.argv[1] == 'i':
        file1_location = sys.argv[2]
        file2_location = sys.argv[3]
    else:
        print('command ', sys.argv[1], 'is not recogized')
        exit(1)

# the location of the file, relative to where we compile the program
# file1_location = "./data/9606_protein.txt"
# file2_location = "./data/9606_protein.txt"

print("loading graph1 from: ", file1_location)
print("loading graph2 from: ", file2_location)

# making grpah1 and graph2, reading information from the provided file
graph1, graph2, map1, map2 = make_graph(file1_location, file2_location)
print("Making graph: done")

# a, b, lambda should be between 0 and 1
a = 1
b = 0 # we don't use biological data for this testing
lamb_da = 0.5

### called the alignment function
result = align(graph1, graph2, a, b, lamb_da)
### result is a list of tuple, (id_in_graph1, id_in_graph2), basically a bunch of matching between i,j

### TO DO:
### calculate the performance score, using alignment


inv_map1 = {v: k for k, v in map1.items()}
inv_map2 = {v: k for k, v in map2.items()}

### remapped the id to the protein name
mapped_result = [(inv_map1[i], inv_map2[j]) for (i,j) in result]
print('Result:')
print(mapped_result)


### save result into .json file
### which the frontend will read later
