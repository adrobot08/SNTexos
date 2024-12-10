def occurences(liste:list)->dict:
    dic={}
    for ele in liste:
        if ele not in dic:
            dic[ele]=liste.count(ele)
    return dic

def taille(dic:dict)->int:
    a=0
    for value in dic.values():
        a+=value
    return a

def compare(Liste1:list,Liste2:list)->bool:
    a1=occurences(Liste1)
    a2=occurences(Liste2)
    if len(Liste1)!=len(Liste2):
        return False
    for ele in a1:
        
        if ele not in a2:
            return False
        else:    
            nb_a1=a1[ele]
            nb_a2=a2[ele]
            if nb_a1!=nb_a2:
                return False
        return True

print(compare([3,5,-2,3,3,-2],[5,3,-2,-2,3,3]))
#print(occurences([3,5,-2,3,3,-2]))
#print(taille({3: 3, 5: 1, -2: 2}))

