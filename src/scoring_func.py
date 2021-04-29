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
