def beverages():
    print("BEVERAGES: ")
    print("(1) Coca Cola")
    print("(2) Sprite")
    print("(3) Royal")
    print("(4) Iced Tea")
    print("(5) Coke Float")
    print("(6) Hot Coffee")
    print("(7) Iced Coffee")
    print("(8) Hot Coffee (Vanilla)")
    print("(9) Iced Coffee (Vanilla)")
    print("(10) Skip")

def beverageChecker(x):
    if x == 1:
        return "Coca Cola"
    elif x == 2:
        return "Sprite"
    elif x == 3:
        return "Royal"
    elif x == 4:
        return "Iced Tea"
    elif x == 5:
        return "Coke Float"
    elif x == 6:
        return "Hot Coffee"
    elif x == 7:
        return "Iced Coffee"
    elif x == 8:
        return "Hot Coffee (Vanilla)"
    elif x == 9:
        return "Iced Coffee (Vanilla)"
    elif x == 10:
        return ""
    else:
        return ""