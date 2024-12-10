'''dic_Mat={"dim":(4,2),(3,2):4}
def somme_mat(M1:dict,M2:dict)->dict:
    if M1["dim"]!=M2["dim"]:
        return False
    M_S={}
    for key in M1.keys():
        if key=="dim":
            M_S["dim"]=M1["dim"]
        elif key in M2:
            M_S[key]=M1[key]+M2[key]
        else:
            M_S[key]=M1[key]
    for key in M2.keys():
        if key=="dim":
            pass
        elif key not in M1:
            M_S[key]=M2[key]
        else:
            pass
    return M_S

M1 = {"dim":(4,2),(3,2):4}
M2 = {"dim":(4,2),(3,2):1,(2,1):3}
M1_2 = {"dim":(4,2),(3,2):4,(1,1):6}
M2_2 = {"dim":(4,2),(3,2):1,(2,1):3,(4,2):5,(1,1):-2}
M1_3 = {"dim":(4,3),(3,2):4,(1,1):6}

print(somme_mat(M1,M2))
print((somme_mat(M1_2,M2_2)))
print((somme_mat(M1_3,M2_2)))'''

'''def renverse(L:list[list]):
    L1=[]
    for i0 in range(len(L[0])):
        L0=[]
        for i1 in range(len(L)):
            L0.append(L[i1][i0])
        L1.append(L0)
    return L1

print(renverse([ [ 5, 4, 1, 5],[ 3, 2, 5, 5],[ 8, 7, 9, 5] ]))

def LigneVersMiniSudoku(ligne: list[int])->list[list[int]]:
    res=[]
    for i in range(3):
        row=[]
        for j in range(3):
            row.append(ligne[3*i+j])
        res.append(row)
    return res

print(LigneVersMiniSudoku([8, 7, 1, 3, 5, 9, 6, 2, 4]))'''

def convertir(a:int):
    nb=""
    while a+1//2!=0:
        nb=str(a%2)+nb
        a=a//2
    return nb

print(convertir(6))
print(convertir(1))
print(convertir(9))
print(convertir(20))
print(convertir(14))