def desserts():
    print("DESSERTS: ")
    print("(1) Sundae")
    print("(2) Hot Fudge")
    print("(3) Caramel Sundae")
    print("(4) Ice Cream Flurry")
    print("(5) Halo-halo")
    print("(6) Banana Split")
    print("(7) Skip")

def dessertChecker(x):
    if x == 1:
        return "Sundae"
    elif x == 2:
        return "Hot Fudge"
    elif x == 3:
        return "Caramel Sundae"
    elif x == 4:
        return "Ice Cream Flurry"
    elif x == 5:
        return "Halo-halo"
    elif x == 6:
        return "Banana Split"
    elif x == 7:
        return ""
    else:
        return ""