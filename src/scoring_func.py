#https://angom.myweb.cs.uwindsor.ca/teaching/cs592/592-ST-NSB-NetAlignment.pdf

ran  = [(i,j) for i in range(3) for j in range(3)]
graph_len = 70

def edgeCorr(al,graph_len):
    match= 0
    for pair in range(len(al)):
        if al[pair][0] = al[pair][1]:
            match += 1

    return match/graph_len

ec = edgeCorr(ran,graph_len)
print(ec)
