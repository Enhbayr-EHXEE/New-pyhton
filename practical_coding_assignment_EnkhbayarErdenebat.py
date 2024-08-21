class Bird:

    def __init__(self,name,age):
        self.set_name(name)
        self.set_age(age)

    def set_name(self,name):
        # Replace spaces with hyphens in the name
        self.__name=name.replace(" ","-")
    
    def set_age(self,age):
        # Checking age is between 1 and 20
        if(age<1):
            self.__age=1
        elif(age>20):
            self.__age=20
        else:
            self.__age=age
    
    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age
    
    def print_name(self):
        # Print name with "can fly"
        print(f"{self.__name} can fly")
    
    def __str__(self):
        # Return suitable info about the object
        return f"bird's name is {self.__name} and age is {self.__age}"

class Cockatoo(Bird):

    def __init__(self,name,age,colour):
        super().__init__(name,age)
        self.set_colour(colour)

    def set_colour(self,colour):
        # Predefined set of colours
        colour_list=["yellow","white","black","blue","brown"]
        if colour.lower() not in colour_list:
            self.__colour="white"
        else:
            self.__colour=colour

    def get_colour(self):
        return self.__colour
    
    def print_name(self):
        # Print name with "can fly"
        print(f"Cockatoo {self.get_name()} can fly")

    def __str__(self):
        # Return suitable info about the object
        return f"{super().__str__()}, and I have {self.__colour} colour"
    
class Ostritch(Bird):

    def __init__(self,name,age,weight):
        super().__init__(name,age)
        self.set_weight(weight)
    
    def set_weight(self,weight):
        # Checking weight is between 1 and 75
        if(weight<1):
            self.__weight=1
        elif(weight>75):
            self.__weight=75
        else:self.__weight=weight

    def get_weight(self):
        return self.__weight
    
    def print_name(self):
        # Print name with "can NOT fly"
        print(f"Ostritch {self.get_name()} can not fly")
    
    def __str__(self):
        # Return suitable info about the object
        return f"{super().__str__()}, and I have {self.__weight} weight"

# checking valueError using try and except method        
def create_bird():
    while True:
        try:
            name = input("Enter bird's name: ")
            age = int(input("Enter bird's age (1-20): "))
            return Bird(name, age)
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")


def create_cockatoo():
    while True:
        try:
            name = input("Enter cockatoo's name: ")
            age = int(input("Enter cockatoo's age (1-20): "))
            colour = input("Enter cockatoo's colour: ")
            return Cockatoo(name, age, colour)
        except ValueError:
            print("Invalid input! Please enter a valid integer for age.")

def create_ostrich():
    while True:
        try:
            name = input("Enter ostrich's name: ")
            age = int(input("Enter ostrich's age (1-20): "))
            weight = int(input("Enter ostrich's weight (1-75): "))
            return Ostritch(name, age, weight)
        except ValueError:
            print("Invalid input! Please enter a valid integer for age and weight.")

def main():
    # Creating objects of Bird, Cockatoo, and Ostrich with user input
    bird_objects = [create_bird() for _ in range(5)]
    cockatoo_objects = [create_cockatoo() for _ in range(5)]
    ostrich_objects = [create_ostrich() for _ in range(5)]

    # Combine all objects into one list
    all_birds = bird_objects + cockatoo_objects + ostrich_objects

    # Loop over the list and call print_name() for birds older than 10
    for bird in all_birds:
        if bird.get_age() > 10:
            bird.print_name()

# starting main function to start the code
if __name__ == "__main__":
    main()