#https://angom.myweb.cs.uwindsor.ca/teaching/cs592/592-ST-NSB-NetAlignment.pdf

import networkx as nx

### al = result pair mapping 
def score(al, graph1, graph2):
    match = 0
    size = len(graph1['edges'])
    ### use this to compute LCCS (Largest common component)
    G = nx.Graph() 


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
                G.add_edge(i1, i2)
                
                break
    ### edge correctness score = total correct edge match / total number of edges
    EC_score = match/size
    largest_cc = max(nx.connected_components(G), key=len)
    return EC_score, largest_cc

# LCCS
# get all 'correct' edge map
# make a graph out of it
# find largest connected component