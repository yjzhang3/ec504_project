import numpy as np
from GraphAdjList import *


def align(graph1, graph2, a, b, lamb_da):
    sim_score = similarity_score(graph1, graph2, a, b)
    P = 0 # unused variable!?!

    # vertices list of graph1 and graph2
    V1 = graph1['vertex']
    V2 = graph2['vertex']
    print('V1 = ', V1)
    print('V2 = ', V2)
    # size of V1 and V2
    n_v1 = graph1['max_id'] + 1
    n_v2 = graph2['max_id'] + 1

    # initialize matrix I and A
    I = np.zeros((n_v1, n_v2))
    A = np.zeros((n_v1, n_v2))

    P = 0
    # 1-d matrix
    C1 = np.zeros(n_v1)
    C2 = np.zeros(n_v2)

    # this is all i-j pair minus L
    L_inverse = [(i,j) for i in range(n_v1) for j in range(n_v2)]
    # L_inverse = set(L_inverse)
    # the output
    Al = []
    
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
        print('n = ', n)
        print('A = ', A)
        print('L_inverse = ', L_inverse)
        A_list = [(A[i][j], (i,j)) for i,j in L_inverse]
        max_A = max(A_list, key = lambda i : i[0])
        # index = A_list.index(max_A)
        # i = index // n_v2
        # j = index % n_v2
        (i, j) = max_A[1]
        print('(i, j) ', (i, j))
        Al.append((i, j))
        L_inverse.remove((i, j))
        # print('L_inverse = ', L_inverse)
        # L_inverse = set(L_inverse)
 
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
        # question: where did 'i' and 'j' come from?
    
        # temp_set = neighbor_i.intersection(L_inverse)
        # temp_set_2 = neighbor_j - L_inverse
        

        # Q = [(i_prime,j_prime) for i_prime in temp_set for j_prime in temp_set_2]

        # what if they don't have the same number of nodes??
        
        # for i in V1:
        #     for j in V2:
        #         if (i,j) not in Q:
        #             temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
        #             temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

        #             temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
        #             temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

        #             I[i][j] = min(sum(temp) - C1[i], sum(temp2) - C2[j])/max(temp3, temp4) + D[i][j]
        #             A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]

        ### tried this one
        for i in V1:
            for j in V2:
                
                # neighbor_i = graph1.adjacency[i]
                # neighbor_j = graph1.adjacency[j]
                neighbor_i = neighbors(graph1, i)
                neighbor_j = neighbors(graph2, j)

                ### sum before subtract C
                temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                I[i][j] = min(sum(temp) - C1[i], sum(temp2) - C2[j])/max(max(temp3), max(temp4)) + D[i][j]

                ### subtract C before sum
                # temp = [1/len(neighbors(graph1, i_prime)- C1[i]) for i_prime in neighbor_i]
                # temp2 = [1/len(neighbors(graph2, j_prime) - C2[j]) for j_prime in neighbor_j]

                # temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                # temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                # I[i][j] = min(sum(temp), sum(temp2))/max(max(temp3), max(temp4)) + D[i][j]

                A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]

        ### tried again

    return Al

def compute_score(graph1, graph2, i ,j , M):

    
    s = 0
    neighbor_i = neighbors(graph1, i) # list of i_prime
    neighbor_j = neighbors(graph2, j) # list of j_prime

    # print('i = ', i)
    # print('j = ', j)
    # print('neighbor_i ', len(neighbor_i))
    # print('neighbor_j ', len(neighbor_j))
    temp = []
    for i_prime in neighbor_i:
        # get all edges from i_prime to j_prime
        weight_list = [M[i_prime][j_prime] for j_prime in neighbor_j]
        neighbor_list = [(M[i_prime][j_prime], j_prime) for j_prime in neighbor_j]

        # print('len weight_list = ', len(weight_list))
        # print(neighbor_list)
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
    print('T ', T)
    T_prime = np.ones((n_v1, n_v2))
    max_round = 10

    V1 = graph1['vertex']
    V2 = graph2['vertex']
    for t in range(1, max_round):
        print('topological_score: iter ', t)
        for i in V1:
            for j in V2:
                T_prime[i, j] = compute_score(graph1, graph2, i , j, T)
        
        T = T_prime
        print('T ', T)
    return T

def biological_score(graph1, graph2, b):

    print('biological_score: start')
    n_v1 = graph1['max_id'] + 1
    n_v2 = graph2['max_id'] + 1

    # a n_v1 x n_v2 matrix
    C = np.eye(n_v1, n_v2) # not sure how to compute this?
    print('C ', C)
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
        
