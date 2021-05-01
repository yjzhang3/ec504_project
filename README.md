# NETAL on Protein Protein Interaction Networks
This project aims to implement a novel graph alignment algorithm called NETAL that aligns protein-protein interaction networks (PPIN) of small sample size that mimics bigger sample size of different species. In order to provide evidence that the algorithm is applicable to study possible evolutionary relationships, we computed the global alignment between several artificially generated PPINs smaller in size. A greedy approach then evaluated the alignment performance based on edge correctness and largest common connected components. The validation of the implementation using smaller graphs shows the promising results in terms of performance and robustness. A visual website also validates the results of alignment. 

## Instructions for Running the Code:
SCC-file location: /projectnb/ec504/ronrat/proj
If run from within SCC, make sure to load python3 module ‘module load python3’

All the commands are run from /projectnb/ec504/ronrat/proj directory. There’s 3 ways to run the code.
1. Running without command line argument. 
    - python ./src/main.py
    - This will use a default file location, hard-coded in main.py
2. Running with option ‘s’. 
    - python ./src/main.py s 3
    - This will use simple graph file located in ./data/
    - The number following the ‘s’ argument indicate which sample/set it will call
    - ./src/main.py s 3 will use ./data/set3_a.txt as graph1 and ./data/set3_b.txt as graph2
3. Running with option ‘i’. 
    - python ./src/main.py i ./data/set3_a.txt ./data/set3_b.txt
    - This will take 2 additional command line arguments, which is 2 file location
    - Note: the 1st graph have to be smaller (has less vertices) than 2nd graph

## Instruction for Running Front End:



## References:
[1]https://academic.oup.com/bioinformatics/article/29/13/1654/185807#92200279   

[2]https://string-db.org/cgi/input?sessionId=bdFKVErETbx4&input_page_show_search=on

[3]https://www.ebi.ac.uk/training/online/courses/network-analysis-of-protein-interaction-data-an-introduction/the-sources-of-data-underlying-biological-networks/ 

[4]https://www.ncbi.nlm.nih.gov/books/NBK56024/

[5]https://www.sciencedirect.com/topics/biochemistry-genetics-and-molecular-biology/protein-protein-interaction-networks 

[6]https://journals.sagepub.com/doi/10.4137/CIN.S4744 

[7]https://angom.myweb.cs.uwindsor.ca/teaching/cs592/592-ST-NSB-NetAlignment.pdf 

[8]https://www.educative.io/edpresso/how-to-implement-a-graph-in-python 

[9]https://core.ac.uk/download/pdf/82965079.pdf 

