import numpy as np

def align(graph1, graph2, a, b, c):
    sim_score = similarit_score(graph1, graph2, a, b)
    P = 0
    C1 = 0
    L = []
    # To do

def compute_score(graph1, graph2, i ,j , M):
    A = []
    s = 0
    for node in neighbor(i):
        node_prime = 

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

def biologica_score(graph1, graph2, b):
    



def similarity_score(graph1, graph2, a, b):