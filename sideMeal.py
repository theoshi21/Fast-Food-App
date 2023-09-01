def sideMeals():
    print("SIDE MEALS: ")
    print("(1) Fries (S)")
    print("(2) Fries (M)")
    print("(3) Fries (L)")
    print("(4) Peach Mango Pie")
    print("(5) Mango Pie")
    print("(6) Tuna Pie")
    print("(7) Skip")

def sideMealChecker(x):
    if x == 1:
        return "Fries (S)"
    elif x == 2:
        return "Fries (M)"
    elif x == 3:
        return "Fries (L)"
    elif x == 4:
        return "Peach Mango Pie"
    elif x == 5:
        return "Mango Pie"
    elif x == 6:
        return "Tuna Pie"
    elif x == 7:
        return ""
    else:
        return ""
