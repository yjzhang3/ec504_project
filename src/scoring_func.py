
#https://angom.myweb.cs.uwindsor.ca/teaching/cs592/592-ST-NSB-NetAlignment.pdf

# ran  = [(i,j) for i in range(3) for j in range(3)]
# graph_len = 70

# def edgeCorr(al,graph_len):
#     match= 0
#     for pair in range(len(al)):
#         if al[pair][0] = al[pair][1]:
#             match += 1

#     return match/graph_len

# ec = edgeCorr(ran,graph_len)
# print(ec)

### al = result pair mapping 
def edgeCorr(al, graph1, graph2):
    match = 0
    size = len(graph1['edges'])
    ### loop over all edges in graph1
    for edge in graph1['edges']:
        ### map edge (i1, i2) to (j1, j2)
        i1 = edge[0]
        i2 = edge[1]

        j1 = al[i1]
        j2 = al[i2]
        for neighbor in graph2[j1]:
            ### if edge (j1, j2) exist in graph2, score + 1
            if neighbor[0] == j2:
                match += 1
                break
    ### score = total correct edge match / total number of edges
    return match/size

####################################################################
# using random set generated artificially
# generate a random graph for DFS
# and compute LSCC (this is specifically designed for a randomly generated graph)

import networkx as nx
from itertools import combinations
from random import random
import numpy as np

def ER(n, p):
    V = set([v for v in range(n)])
    #print(V)
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)
    #print(E)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)


    return g

# https://www.geeksforgeeks.org/connected-components-in-an-undirected-graph/
def NCC(G):
    visited = [False for i in range(G.number_of_nodes())]
    cc = []
    for v in range(G.number_of_nodes()):
        if visited[v] == False:
            temp = []
            cc.append(DFS(G,temp,v,visited))
    return cc
         
def DFS(G,temp,v,visited):
    #print(visited)
    visited[v] = True
    temp.append(v)
    for nbr in G.adj[v]:
        if visited[nbr] == False:
            temp = DFS(G,temp,nbr,visited)
    return temp # return an array that connects with each other

def LSCC(G1,G2): # G1<G2
    visited1 = [False for i in range(G1.number_of_nodes())]
    visited2 = [False for i in range(G2.number_of_nodes())]
    ccc = [] # common connected components
    cc1 = []
    cc2 = [] # connected components in g1 and g2
    
    for v1 in range(G1.number_of_nodes()):
        if v1 in G2.nodes: # find the common seed
            if visited1[v1] == False:
                temp1 = []
                cc1.append(DFS(G1,temp1,v1,visited1))
            if visited2[v1] == False:
                temp2 = []
                cc2.append(DFS(G2,temp2,v1,visited2))
        
            set1 = set(temp1)
            set2 = set(temp2)
            ccc.append(set1.intersection(set2))
            
    return len(ccc)

n1 = 15
p1 = 0.76
n2 = 7
p2 = 0.554
G1 = ER(n1,p1)
G2 = ER(n2,p2)
print(NCC(G1))
print(NCC(G2))
print(LSCC(G1,G2))
