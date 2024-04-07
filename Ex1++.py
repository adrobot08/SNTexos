def inputInt(name):
    return int(input("Enter integer '" + name + "': "))

a = inputInt("a")
b = inputInt("b")
a = a * b
a = a + b
if(a==b):
    print("yes")
else:
    print("no")