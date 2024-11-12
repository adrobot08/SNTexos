def Ajouterk(L:list[float],k:float)->list[float]:
    """ajoute de K chaque élément de la liste[L]"""
    i=0
    L1=[ele+k for ele in L]
    return L1

maListe = [13, 27, 50, 42, 3]
print(Ajouterk(maListe,1))
maListe2 =[13, 8, 0, 4, 3]
print(Ajouterk(maListe2,-1))
maliste3 =[4, 7, -5, -42, 3]
print(Ajouterk(maliste3,2.5))
maliste4 =[9, 5, 2, 42, 3]
print(Ajouterk(maliste4,10))
print(Ajouterk(maliste4,-1))
maliste5 =[6.2,0.6,-4.4,-2.55]
print(Ajouterk(maliste5,-1.12))