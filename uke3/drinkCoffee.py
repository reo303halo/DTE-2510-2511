
class CoffeeCup:
    def __init__(self, numberOfSips = 10):
        self.numberOfSips = numberOfSips

    def takeOneSip(self):
        self.numberOfSips -= 1
        print("Number of sips left: ", self.numberOfSips)

    def fillCup(self, sips):
        self.numberOfSips += sips



def drinkCoffee(cup):
    if cup.numberOfSips != 0: # Base case
        cup.takeOneSip()
        drinkCoffee(cup)



def main():
    cup = CoffeeCup()
    drinkCoffee(cup)



if __name__ == "__main__":
    main()
    