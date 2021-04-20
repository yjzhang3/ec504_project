import networkx as nx
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
from matplotlib import cm

# All rights reserved Mandy Yao, Yujia Zhang, Ronnakon Rattanakornphan, Haoming Yi
# Reference from and modified to: https://towardsdatascience.com/visualizing-protein-networks-in-python-58a9b51be9d5
################################################ Instructions ##################################################
# Goal: To generate protein network visual
# 1) Download one input data from http://string-db.org, save to local directory with this program
# 2) Command line in terminal: "python3 GraphAdjList.py text1.txt"
# 3) Run the program, may take a bit
############################################ End of Instructions ###############################################

# Main driver code
if len(sys.argv) != 2: #check input arguments to be two text files
    sys.exit("Input argument must be a text files")

# Reading into the first protein file that can be obtained from string-db.org
fileget_1 = open (sys.argv[1], 'r')
next(fileget_1) # ignoring the first line of input
count = 0
protein_map1 = {} # a map that maps protein id to numbers
# Store vertices in vertices_list
vertices_list = 0
G = nx.Graph(name='Protein Interaction Graph') 
for line in fileget_1:
    # Add score between vertcies by specifying
    # Start vertex, End vertex, Score <--- Fromat
    protein1, protein2, score = line.strip().split()
    if (protein1 not in protein_map1):
        # Making sure the map has unique proteins, no repetitive
        protein_map1[protein1] = count
        count += 1
    if (protein2 not in protein_map1):
        # Making sure the map has unique proteins, no repetitive
        protein_map1[protein2] = count
        count += 1
    G.add_edge(protein_map1[protein1],protein_map1[protein2], weight=score)
pos = nx.spring_layout(G)
plt.figure(figsize=(11,11),facecolor=[0.7,0.7,0.7,0.4])
nx.draw_networkx(G)
plt.axis('off')
plt.show()