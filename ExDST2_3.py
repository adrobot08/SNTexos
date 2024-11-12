def decale(lettre:str,n:int):
    return chr(ord("a")+(ord(lettre)-ord("a")+n) % 26)

print(decale("x",10))

def cesar(mot:str,n:int):
    res=""
    for lettre in mot:
        res+=(decale(lettre,n))
    return res

print(cesar("papa",3))


   
   
     