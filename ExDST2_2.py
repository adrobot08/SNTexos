def palindrome(mot:str):
    for i in range(len(mot)):
        if mot[i]!=mot[len(mot)-i-1]:
            return False
    return True

def palindrome2(mot:str):
    inverse=''
    for lettre in mot:
        inverse = lettre + inverse
    return inverse == mot

print(palindrome2("kayak"))
print(palindrome2("motif"))
print(palindrome2("ici"))
print(palindrome2("ressasser"))
print(palindrome2("toto"))
print(palindrome2("lili"))