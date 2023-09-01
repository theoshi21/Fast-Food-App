def meals():
    print("MEALS: ")
    print("(1) Chicken Fillet")
    print("(2) Fried Chicken")
    print("(3) Spaghetti")
    print("(4) Spaghetti w/ Chicken")
    print("(5) Nuggets")
    print("(6) Regular Burger")
    print("(7) Cheese Burger")
    print("(8) Burger Deluxe")
    print("(9) Skip")

def mealChecker(x):
    if x == 1:
        return "Chicken Fillet"
    elif x == 2:
        ordering = True
        while(ordering):
            quantity = int(input("Quantity: 1 or 2 piece chicken. "))
            if quantity == 1:
                ordering = False
                return "1 Pc. Fried Chicken"
            if quantity == 2:
                ordering = False
                return "2 Pcs. Fried Chicken:"
    elif x == 3:
        return "Spaghetti"
    elif x == 4:
        return "Spaghetti w/ Chicken"
    elif x == 5:
        print("     FLAVORS: ")
        print("     (1) CHEESE")
        print("     (2) BBQ")
        ordering = True
        while(ordering):
            type = int(input("Flavor: "))
            if type == 1:
                print("     QUANTITY:")
                print("     (1) 6 pcs.")
                print("     (2) 8 pcs.")
                print("     (3) 12 pcs.")
                moreOrdering = True
                while (moreOrdering):
                    quantity = int(input("Quantity: "))
                    if quantity == 1:
                        return "6 pcs. Nuggets [Cheese]"
                    elif quantity == 2:
                        return "8 pcs. Nuggets [Cheese]"
                    elif quantity == 3:
                        return "12 pcs. Nuggets [Cheese]"
            elif type == 2:
                print("     Quantity:")
                print("     (1) 6 pcs.")
                print("     (2) 8 pcs.")
                print("     (3) 12 pcs.")
                moreOrdering = True
                while (moreOrdering):
                    quantity = int(input("Quantity: "))
                    if quantity == 1:
                        return "6 pcs. Nuggets [BBQ]"
                    elif quantity == 2:
                        return "8 pcs. Nuggets [BBQ]"
                    elif quantity == 3:
                        return "12 pcs. Nuggets [BBQ]"
    elif x == 6:
        return "Regular Burger"
    elif x == 7:
        return "Cheese Burger"
    elif x == 8:
        return "Burger Deluxe"
    elif x == 9:
        return ""
    else:
        return ""