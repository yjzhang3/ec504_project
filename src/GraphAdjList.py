import networkx as nx
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
################################################ Instructions ################################################
# Goal: parse individual graph into adjacency list and set of vertices
# 1) Download TWO input data from http://string-db.org, save to local directory with this program
# 2) Change line fileget_1 = open ('test1.txt', 'r') and fileget_2 = open ('test2.txt', 'r') to name of input data downloaded
# 3) Run the program, you will see printed out adj list for both of them in the files of AdjListOutput1.txt and AdjListOutput2.txt
# 4) To parse into the actual adj list, look at print functions: graph1 is your first adj list and graph2 is your second adj list
############################################ End of Instructions ################################################
def add_vertex1(v):
    global graph1
    global vertices_list
    if v in graph1:
        print("Vertex ", v, " already exists.")
    else:
        vertices_list = vertices_list + 1
        graph1[v] = []

def add_edge1(v_start, v_end, score):
    global graph1
    # Validation of start vertex
    if v_start not in graph1:
        print("here1")
        print("Vertex ", v_start, "does not exist.")
    # Validation of end vertex
    elif v_end not in graph1:
        print("here2")
        print("Vertex ", v_end, " does not exist.")
    # Validated start and end vertices
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not 
    # imply that an edge exists between v2 and v1
    # for undirected graph: this can be fixed adding neighbor vertex
    # to both start and end vertex
    else:
        temp = [v_end, score]
        graph1[v_start].append(temp)

def print_graph1():
    # print adj list into a text file as output
    sample = open('AdjListOutput1.txt', 'w')
    global graph1
    for vertex in graph1:
        for edges in graph1[vertex]:
            print (vertex, " -> ", edges[0], " edge weight: ", edges[1], file = sample)

# Goal: parse individual graph into adjacency list and set of vertices
# This only works for number not names
def add_vertex2(v):
    global graph2
    global vertices_list
    if v in graph2:
        print("Vertex ", v, " already exists.")
    else:
        vertices_list = vertices_list + 1
        graph2[v] = []

def add_edge2(v_start, v_end, score):
    global graph2
    # Validation of start vertex
    if v_start not in graph2:
        print("here1")
        print("Vertex ", v_start, "does not exist.")
    # Validation of end vertex
    elif v_end not in graph2:
        print("here2")
        print("Vertex ", v_end, " does not exist.")
    # Validated start and end vertices
    # Since this code is not restricted to a directed or 
    # an undirected graph, an edge between v1 v2 does not 
    # imply that an edge exists between v2 and v1
    # for undirected graph: this can be fixed adding neighbor vertex
    # to both start and end vertex
    else:
        temp = [v_end, score]
        graph2[v_start].append(temp)
def print_graph2():
    # print adj list into a text file as output
    sample = open('AdjListOutput2.txt', 'w')
    global graph2
    for vertex in graph2:
        for edges in graph2[vertex]:
            print (vertex, " -> ", edges[0], " edge weight: ", edges[1], file = sample)



# Main driver code
graph1 = {}

# Store vertices in vertices_list
vertices_list = 0

# Reading into the first protein file that can be obtained from string-db.org
fileget_1 = open ('test.txt', 'r')
next(fileget_1) # ignoring the first line of input
count = 0
protein_map1 = {} # a map that maps protein id to numbers

################################################ Visual- please ignore ################################################

#G = nx.Graph(name='Protein Interaction Graph') 
################################################ Visual- please ignore ################################################

for line in fileget_1:
    # Add score between vertcies by specifying
    # Start vertex, End vertex, Score <--- Fromat
    protein1, protein2, score = line.strip().split()
    if (protein1 not in protein_map1):
        # Making sure the map has unique proteins, no repetitive
        protein_map1[protein1] = count
        add_vertex1(count)
        count += 1
    if (protein2 not in protein_map1):
        # Making sure the map has unique proteins, no repetitive
        protein_map1[protein2] = count
        add_vertex1(count)
        count += 1
    # Add each edge into graph for adj list
    add_edge1(protein_map1[protein1], protein_map1[protein2], score)
################################################ Visual- please ignore ################################################
    # G.add_edge(protein_map1[protein1],protein_map1[protein2], weight=score) # 
################################################ Visual- please ignore ################################################
print_graph1()
################################################ Visual- please ignore ################################################
# pos = nx.spring_layout(G)
# plt.figure(figsize=(11,11),facecolor=[0.7,0.7,0.7,0.4])
# nx.draw_networkx(G)
# plt.axis('off')
# plt.show()
################################################ Visual- please ignore ################################################


# Clear global variables
# Main driver code
graph2 = {}

# Store vertices in vertices_list
vertices_list = 0

protein_map2 = {} # a map that maps protein id to numbers

# Reading into the second protein file that can be obtained from string-db.org
fileget_2 = open ('test1.txt', 'r')
next(fileget_2) # ignoring the first line of input

for each in fileget_2:
    proteinA, proteinB, score_2 = each.strip().split()
    # protein not already exist, create vertex 
    if (proteinA not in protein_map2):
        # Making sure the map has unique proteins, no repetitive
        if (proteinA in protein_map1): 
            num = protein_map1[proteinA]
            protein_map2[proteinA] = num
            add_vertex2(num)
        else:
            add_vertex2(count)
            protein_map2[proteinA] = count
            count += 1
    if (proteinB not in protein_map2):
        # Making sure the map has unique proteins, no repetitive
        if (proteinB in protein_map1):
            num = protein_map1[proteinB]
            protein_map2[proteinB] = num
            add_vertex2(num)
        else:
            add_vertex2(count)
            protein_map2[proteinB] = count
            count += 1
    add_edge2(protein_map2[proteinA], protein_map2[proteinB], score_2)
print_graph2() # print the second adj list