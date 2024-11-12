def inputInt(msg: str):
    return int(input(msg + ": "))
a = inputInt("Enter number of adult(s)")
e = inputInt("Enter number of child(ren)")
p = a*21 + e*13
print("Le prix d'entré est de", p, "€")
