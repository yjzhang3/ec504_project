import numpy as np
from GraphAdjList import *
import time

def align(graph1, graph2, a, b, lamb_da):
    sim_score = similarity_score(graph1, graph2, a, b)
    P = 0 # unused variable!?!

    # vertices list of graph1 and graph2
    V1 = graph1['vertex']
    V2 = graph2['vertex']

    # size of V1 and V2
    n_v1 = len(V1)
    n_v2 = len(V2)

    # initialize matrix I and A
    I = np.zeros((n_v1, n_v2))
    A = np.zeros((n_v1, n_v2))

    # 1-d matrix
    C1 = np.zeros(n_v1)
    C2 = np.zeros(n_v2)

    # list of vertices not already selected
    L_i = V1.copy()
    L_j = V2.copy()

    # the output
    # Al = []
    Al = {}
    
    print("Align: calculating first matrix A")
    for i in V1:
        for j in V2:
            
            # neighbor_i = graph1.adjacency[i]
            neighbor_i = neighbors(graph1, i)
            # neighbor_j = graph1.adjacency[j]
            neighbor_j = neighbors(graph2, j)

            temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
            temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

            temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
            temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

            I[i][j] = min(sum(temp),sum(temp2))/max(max(temp3), max(temp4))
            A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]

    print("Align: done calculating first matrix A")
    for n in V1:

        A_list = [(A[i][j], (i,j)) for i in L_i for j in L_j]
        max_A = max(A_list, key = lambda i : i[0])
        ### greedy: select i,j pairing with best score
        (i, j) = max_A[1]
        ### save it into output
        # Al.append((i, j))
        Al[i] = j
        ### don't consider i,j we already select
        L_i.remove(i)
        L_j.remove(j)
 
        # start of Haoming's
        neighbor_i = neighbors(graph1, i)
        neighbor_j = neighbors(graph2, j)
        neighbor_i = set(neighbor_i)
        neighbor_j = set(neighbor_j)

        for i_prime in neighbor_i:
            C1[i_prime] = C1[i_prime] + 1/len(neighbor_i)
        
        for j_prime in neighbor_j:
            C2[j_prime] = C2[j_prime] + 1/len(neighbor_j)
        
        D = np.zeros((n_v1, n_v2))
        for i_prime in neighbor_i:
            for j_prime in neighbor_j:
                D[i_prime][j_prime] = D[i_prime][j_prime] + 1
        # end of Haoming's
    
        ### unused code, unable to verify the meaning from pseudo-code
        # temp_set = neighbor_i.intersection(L_inverse)
        # temp_set_2 = neighbor_j - L_inverse
        # Q = [(i_prime,j_prime) for i_prime in temp_set for j_prime in temp_set_2]
        
        # for i in V1:
        #     for j in V2:
        #         if (i,j) not in Q:
        #             temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
        #             temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

        #             temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
        #             temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

        #             I[i][j] = min(sum(temp) - C1[i], sum(temp2) - C2[j])/max(temp3, temp4) + D[i][j]
        #             A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]

        ### tried this one instead
        for i in V1:
            for j in V2:
                
                neighbor_i = neighbors(graph1, i)
                neighbor_j = neighbors(graph2, j)

                ### sum before subtract C
                temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                I[i][j] = min(sum(temp) - C1[i], sum(temp2) - C2[j])/max(max(temp3), max(temp4)) + D[i][j]
                A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]
                
    return Al

def compute_score(graph1, graph2, i ,j , M):

    
    s = 0
    neighbor_i = neighbors(graph1, i) # list of i_prime
    neighbor_j = neighbors(graph2, j) # list of j_prime

    temp = []
    for i_prime in neighbor_i:
        # get all edges from i_prime to j_prime
        weight_list = [M[i_prime][j_prime] for j_prime in neighbor_j]
        neighbor_list = [(M[i_prime][j_prime], j_prime) for j_prime in neighbor_j]

        # find index of max edge
        max_weight = max(weight_list)
        index = weight_list.index(max_weight)
        j_dprime = neighbor_list[index][1]
        
        # we won't consider any j_prime we already put as result
        neighbor_j.remove(j_dprime)
        # sum the max weight
        s = s + max_weight
        if (len(neighbor_j) == 0):
            break

    return s/(max(len(neighbor_i),len(neighbor_j)))

# done
def topological_score(graph1, graph2):
    print('topological_score: start')
    # T = i x j matrix
    # i = no. of vertex in graph1
    # j = no. of vertex in graph2
    n_v1 = graph1['max_id'] + 1
    n_v2 = graph2['max_id'] + 1

    T = np.ones((n_v1, n_v2))
    T_prime = np.ones((n_v1, n_v2))
    max_round = 10

    V1 = graph1['vertex']
    V2 = graph2['vertex']
    for t in range(1, max_round):
        print('topological_score: iter ', t)
        for i in V1:
            for j in V2:
                start_time = time.time()
                print('topological_score: (i, j) ', i, ' ', j)
                T_prime[i, j] = compute_score(graph1, graph2, i , j, T)
                print("--- %s seconds ---" % (time.time() - start_time))
        
        T = T_prime
    print('topological_score: done')
    return T

def biological_score(graph1, graph2, b):

    print('biological_score: start')
    n_v1 = graph1['max_id'] + 1
    n_v2 = graph2['max_id'] + 1

    # a n_v1 x n_v2 matrix
    C = np.eye(n_v1, n_v2) # not sure how to compute this?
    # should be num_node_1*num_node_2 matrix
    # temporarily initialize as diaginal of '1'

    B = C
    B_prime = np.ones((n_v1, n_v2)) # create an array with the same dimension as B but filled with 1 for now
    
    V1 = graph1['vertex']
    V2 = graph2['vertex']
    
    max_round = 10 #tunable
    for t in range(1,max_round):
        for i in V1:
            for j in V2:
                s = compute_score(graph1,graph2,i,j,B) # does this give a single number?
                B_prime[i,j] = b*C[i,j] + (1-b)*s
                    
        B = B_prime

    print('biological_score: done')
    return B # typo in the PDF? It said T



def similarity_score(graph1, graph2, a, b):
    print('similarity_score: start')
    # num_node_1 = no. of vertex in graph1
    # num_node_2 = no. of vertex in graph2
    n_v1 = graph1['max_id'] + 1
    n_v2 = graph2['max_id'] + 1

    S = np.zeros((n_v1, n_v2))
    # Similarity score matrix S with forumla rows and forumla columns, indicates the similarity between nodes of two networks
    
    T = topological_score(graph1,graph2)
    B = biological_score(graph1, graph2, b)
    # both T and B are matrices
    
    
    # how to iterate through every vertex in graphs?
    # could we have adjacency list for this implemention (use linked list but not necessarily easier)
    V1 = graph1['vertex']
    V2 = graph2['vertex']    

    for i in V1:
        for j in V2:
            S[i,j] = a * T[i,j] + (1-a) * B[i,j]
    
    print('similarity_score: done')
    return S
        
