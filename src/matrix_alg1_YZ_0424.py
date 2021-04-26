# Command line in terminal: "python3 GraphAdjList.py text1.txt text2.txt"
# note for adjacency matrix (quoted from Mandy's instructions)

# graph1 is for text1.txt
# graph2 is for text2.txt

# Example
# 1) To get the number of vertcies ----> print(len(graph1))
# 2) To get the list of all nodes to its neighbors ----> print(graph1)
# 3) To get node's neighbors and scores ----> print(graph1[#])
# 4) To get only neighbors --->
# CODE BEGIN
# for edges in graph1[#]:
#   print(edges[0])
# CODE END

lamb_da = 1.1111 # define lambda here 

def align(graph1, graph2, a, b, lamb_da):
    sim_score = similarity_score(graph1, graph2, a, b)
    P = 0
    C1 = 0

    # vertices list of graph1 and graph2
    V1 = graph1['vertex'] # I believe with Mandy's code we can just do graph1, graph2 
    V2 = graph2['vertex']
    # size of V1 and V2
    n_v1 = len(V1)
    n_v2 = len(V2)

    # initialize matrix I and A
    I = np.zeros((n_v1, n_v2))
    A = np.zeros((n_v1, n_v2))

    P = 0
    # 1-d matrix
    C1 = np.zeros(n_v1)
    C1 = np.zeros(n_v2)


    L_inverse = [(i,j) for i in range(n_v1) for j in range(n_v2)] # this literally creates pair, like [(1,2),(7,9)...]
    L_inverse = set(L_inverse)
    # the output
    Al = {}
    
    
    for i in V1:
        for j in V2:
            
            # neighbor_i = graph1.adjacency[i] # get all the neighbors of node i
            
            # neighbor_j = graph1.adjacency[j] # ...j
            neighbor_i = neighbors(graph1, i)
            neighbor_j = neighbors(graph2, j)
            
            neighbor_i = set(neighbor_i)
            neighbor_j = set(neighbor_j)
            # 4) To get only neighbors --->
            #  CODE BEGIN
            # for edges in graph1[#]:
            #   print(edges[0])
            # CODE END
            
            # question: (1) what is #? Node ID (a numberical number or a string)
            # (2) do we want to get all the neighbors from the text file? or store this into a new array, like this
            # neighbor_i = []
            # for edges in graph1[i]:
                # neighbor_i.append(edges[0])
                
            # does this take the sum already? I believe there is a summation sign 
            # temp is still an array for now
            temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
            temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

            temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
            temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

            I[i][j] = min(sum(temp),sum(temp2))/max(temp3, temp4)
            A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]
            
    i  = 0
    j = 0 # clear up the varibles so we can use them for later loops 

    for n in V1:

        A_list = [A[i][j] for i,j in L_inverse]
        max_A = max(A_list)
        index = A_list.index(max_A)
        i_prime = index // n_v2
        j_prime = index % n_v2 # could you explain this?

        Al[i_prime] = j_prime
        # L = L.add(i_prime)
        # L = L.add(j_prime)
        L_inverse = L_inverse.remove(i_prime, j_prime) # typo again? remove i' and j' instead?
        
        
        # Haoming's code goes here (still inside of for n in V1 loop)
        # expect to get matrix C1, C2 and D. 
        
        
        
        
        
        
        # Yujia's code (still inside of for n in V1 loop)
        # not sure what does (i',j) | j.... means, need help 
        # how to remove elements: https://discuss.codecademy.com/t/what-ways-can-we-use-to-remove-elements-from-a-list-in-python/376298
        # I believe it is i', j' that are put into Q, not i',j
        # and should exclude things in L, not L'
        
        # if L is an array of pair of nodes
        
        # for l in range(len(L)): # remove L from the neighbor of i and j 
        #     neighbor_i.remove(L[l])
        #     neighbor_j.remove(L[j])
        
        
        temp_set = neighbor_i.intersection(L_inverse)
        temp_set_2 = neighbor_j - L_inverse
        

        Q = [(i_prime,j_prime) for i_prime in temp_set for j_prime in temp_set_2]
        # what if they don't have the same number of nodes??
        
        for i in V1:
            for j in V2:
                if (i,j) not in Q:
                    temp = [1/len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                    temp2 = [1/len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                    temp3 = [len(neighbors(graph1, i_prime)) for i_prime in neighbor_i]
                    temp4 = [len(neighbors(graph2, j_prime)) for j_prime in neighbor_j]

                    I[i][j] = min(sum(temp) - C1[i], sum(temp2) - C2[j])/max(temp3, temp4) + D[i][j]
                    A[i][j] = lamb_da*sim_score[i][j] + (1 - lamb_da)*I[i][j]
        
        
        
