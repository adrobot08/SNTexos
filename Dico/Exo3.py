def inverse(G:dict)->dict:
    G_inverse={}
    for k in G.keys():
        G_inverse[k]=[]
    for key,value in G.items():
        for ele in value:
            if ele in G_inverse:
                G_inverse[ele]=G_inverse[ele]+[key]
    return G_inverse

print(inverse( {'a':['b','c','e'],'b':['d'],'c':['e'],'d':['c','e'], 'e':[]}))

            
