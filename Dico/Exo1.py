def min_max(liste:list[int])->dict: 
    """renvoie un dictionnaire
dont les clés sont les chaînes "min" et "max" avec pour valeurs respectives le minimum et le maximum des
nombres de la liste."""
    min, max = liste[0],liste[0] 
    dico_min_max={}
    for ele in liste:
        if ele < min:
            min=ele
            dico_min_max["min"]=ele
        if ele > max:
            max=ele
            dico_min_max["max"]=ele
    return dico_min_max

print(min_max([8,5,9,3,1,7]))


