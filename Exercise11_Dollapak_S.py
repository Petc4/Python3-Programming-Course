layer = int(input("How many layers of pyramid? : "))
for x in range(layer):
    y=1+2*x
    print(" "*(layer-x) +"*"*(y))
