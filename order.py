class Order:
    def __init__ (self, meal,sideMeal,beverage,dessert):
        self.meal = meal
        self.sideMeal = sideMeal
        self.beverage = beverage
        self.dessert = dessert

    def listOrder(self):
        print("Meal: "+str(self.meal))
        print("Side Meal: "+str(self.sideMeal))
        print("Beverage: "+str(self.beverage))
        print("Dessert: "+str(self.dessert))
