import sys
import networkx as nx
from itertools import combinations
from random import random


def ER(n, p):
    V = set([v for v in range(n)])
    E = set()
    for combination in combinations(V, 2):
        a = random()
        if a < p:
            E.add(combination)

    g = nx.Graph()
    g.add_nodes_from(V)
    g.add_edges_from(E)

    return g

if sys.argv[1] == 's':
    filenum = sys.argv[2]
    n = int(sys.argv[3])
# n = 15
p = 0.4
G = ER(n, p)
# print(G.edges)
with open('data/set' + filenum + '.txt', 'w') as f:
    print('protein1','protein2','combined_score', file=f)
    for i,j in G.edges:
        print(i,j,1, file=f)