import numpy as np
a = 0.44 # between 0 and 1, a parameter that controls the balance between biological and topological score
b = 0.79 # not defined in the article?

def align(graph1, graph2, a, b, c):
    sim_score = similarity_score(graph1, graph2, a, b)
    P = 0
    C1 = 0
    L = []
    # To do

def compute_score(graph1, graph2, i ,j , M):
    
    s = 0

    neighbor_i = graph1.adjacency[i] # list of i_prime
    neighbor_j = graph2.adjacency[j] # list of j_prime
    temp = []
    for i_prime in neighbor_i:
        # get all edges from i_prime to j_prime
        weight_list = [M[i_prime][j_prime] for j_prime in neighbor_j]
        neighbor_list = [(M[i_prime][j_prime], j_prime) for j_prime in neighbor_j]

        # find index of max edge
        max_weight = max(weight_list)
        index = weight_list.index(max_weight)
        j_dprime = neighbor_list[index].second
        
        # we won't consider any j_prime we already put as result
        neighbor_j.remove(j_dprime)
        # sum the max weight
        s = s + max_weight

    return s/(max(len(neighbor_i),len(neighbor_j)))

# done
def topological_score(graph1, graph2):
    # T = i x j matrix
    # i = no. of vertex in graph1
    # j = no. of vertex in graph2
    T = np.ones((graph1.shape[0], graph2.shape[0]))
    T_prime = np.ones((graph1.shape[0], graph2.shape[0]))
    max_round = 100
    for t in range(1, max_round):
        for i in range(0, graph1.shape[0]):
            for j in range(0, graph2.shape[0]):
                T_prime[i, j] = compute_score(graph1, graph2, i ,j , T)
        
        T = T_prime
    return T

def biological_score(graph1, graph2, b):
    # num_node_1 = no. of vertex in graph1
    # num_node_2 = no. of vertex in graph2
    C = np.zeros((num_node_1,num_node_2)) # not sure how to compute this?
    # should be num_node_1*num_node_2 matrix
    # temporarily initialize as empty

    B = C
    B_prime = np.full_like(B, 1) # create an array with the same dimension as B but filled with 1 for now
    
    
    max_round = 100 #tunable
    for t in range(1,max_round):
    	for i in range(1,num_node_1): # assume each node has ID and I'm calling every one of them
    		for j in range(1,num_node_2):
    			s = ComputeScore(graph1,graph2,i,j,B) # does this give a single number?
    			B_prime[i,j] = b*C[i,j] + (1-b)*s
    				
    	B = B_prime
    
    return B # typo in the PDF? It said T



def similarity_score(graph1, graph2, a, b):
    # num_node_1 = no. of vertex in graph1
    # num_node_2 = no. of vertex in graph2
	S = np.zeros((num_node_1,num_node_2))
	# Similarity score matrix S with forumla rows and forumla columns, indicates the similarity between nodes of two networks
	
	T = topological_score(graph1,graph2)
	B = biological_score(graph1,graph2)
    	# both T and B are matrices
    	
    	
    	# how to iterate through every vertex in graphs?
    	# could we have adjacency list for this implemention (use linked list but not necessarily easier)
    	

    	for i in range(1,num_node_1): # assume each node has ID and I'm calling every one of them
    		for j in range(1,num_node_2):
    		 	S[i,j] = a*T[i,j] + (1-a)B[i,j]
    	
    	return S
    	
