
# Super
class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def getAge(self):
        return self.__age
    
    def setAge(self, newAge):
        self.__age = newAge

    def __str__(self):
        return f"Hello, my name is {self.name} and I am {self.__age} years old."
    

# Sub 1
class Developer(Person):
    def __init__(self, name, age, language):
        super().__init__(name, age)
        self.language = language


    def writeCode(self):
        return f"In {self.language} you print like this: \nprint('Hello World!')"


    def __str__(self):
        return f"{super().__str__()}\nI am a developer and I code in {self.language}."

# Sub 2
class TaxiDriver(Person):
    def __init__(self,name, age, car):
        super().__init__(name, age)
        self.car = car

    def drive(self):
        return "Vrooom"

    def __str__(self):
        return f"{super().__str__()}\nI am a taxi driver and I drive a {self.car}."


def main():

    # Super
    person = Person("Alice", 25)

    print(person, "\n")

    # Sub 1
    dev = Developer("Roy", 29, "Python")

    print(dev)
    print("Age: ", dev.getAge(), "\n")
    print(dev.writeCode(), "\n")

    # Sub 2
    driver = TaxiDriver("Roger", 35, "Chevrolet")

    print(driver)
    print("Age: ", driver.getAge(), "\n")
    print(driver.drive(), "\n")


if __name__ == "__main__":
    main()