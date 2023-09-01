#IDEA TO IMRPOVE: ADD PRICE, HOW MUCH RECEIVED AND THE CHANGE OF THE PERSON

import order
from meal import mealChecker as m
from meal import meals
from beverage import beverages
from beverage import beverageChecker as b
from sideMeal import sideMeals
from sideMeal import sideMealChecker as sm
from dessert import desserts
from dessert import dessertChecker as d


print("xxxxxxxxxxxxxxxxxxxx")
print("       McKylee      ")
print("xxxxxxxxxxxxxxxxxxxx")
print()


inMode = True
while(inMode):
    mode = input("Dine-in or Takeout?: ")
    dine = {"dine-in","Dine-in","Dine-In","dine in","Dine In","Dine","Dine in","dine"}
    takeout = {"Takeout","takeout","takeaway","TAKEOUT","Taekaway","Take-out","take-out"}

    for customerMode in dine:
        if customerMode == mode:
            modeOfCustomer = 1 #1 is dine-in
            print("MODE: Dine-in.")
            inMode = False

    for customerMode in takeout:
        if customerMode == mode:
            modeOfCustomer = 2 #2 is takeout
            print("MODE: Takeout.")
            inMode = False

keepOrder = True

allOrders = []
while(keepOrder):
    meals()
    ordering = True
    while(ordering):
        mealOrder = int(input("PLEASE CHOOSE A MEAL USING THE CORRESPONDING NUMBERS: "))
        if mealOrder >= 1 and mealOrder <= 10:
            cMealOrder = m(mealOrder)
            ordering = False
        else:
            pass
    print()

    sideMeals()
    ordering = True
    while(ordering):
        sideMealOrder = int(input("PLEASE CHOOSE A SIDEMEAL USING THE CORRESPONDING NUMBERS: "))
        if sideMealOrder >= 1 and sideMealOrder <= 7:
            ordering = False
        else:
            pass
    print()

    beverages()
    ordering = True
    while(ordering):
        beverageOrder = int(input("PLEASE CHOOSE A BEVERAGE USING THE CORRESPONDING NUMBERS: "))
        if beverageOrder >= 1 and beverageOrder <= 10:
            ordering = False
        else:
            pass
    print()

    desserts()
    ordering = True
    while(ordering):
        dessertOrder = int(input("PLEASE CHOOSE A DESSERT USING THE CORRESPONDING NUMBERS: "))
        if dessertOrder >= 1 and dessertOrder <= 7:
            ordering = False
        else:
            pass
    print()

    o = order.Order(cMealOrder,sm(sideMealOrder),b(beverageOrder),d(dessertOrder))
    allOrders.append(o)

    ordering = True
    while(ordering):
        customerInput = input("Keep Ordering?: [Y/N] ")
        if customerInput == "Y" or customerInput == "y":
            ordering = False
            pass
        elif customerInput == "N" or customerInput == "n":
            ordering = False
            keepOrder = False
        else:
            print("Invalid Input, try again.")
        print()
if modeOfCustomer == 1:
    print("MODE: DINE-IN")
elif modeOfCustomer == 2:
    print("MODE: TAKEOUT")

orderNumber = 1
for everything in allOrders:
    print("ORDER # " +str(orderNumber))
    orderNumber += 1
    everything.listOrder()
    print()
