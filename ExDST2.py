def recherche_voyelles(phrase:str):
    voyelles="aeyuioAEYUIO"
    res=0
    for element in phrase:
        if element in voyelles:
            res+=1
    return res

print(recherche_voyelles("z(e)r(e)f(y)thgT(Y)G(A)D(A)VHGdfggh(E)r(a)rS(ae)vcxfg"))
