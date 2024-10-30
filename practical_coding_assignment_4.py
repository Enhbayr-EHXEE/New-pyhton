class Person:
    # Constructor __init__ to assign default values for the variables
    def __init__(self, nm="name", ag=0):
        self.set_name(nm)
        self.set_age(ag)

    # Getter for the name
    def get_name(self):
        return self.__name

    # Setter for the name with validation
    def set_name(self, nm):
        if nm.isalpha():
            self.__name = nm
        else:
            self.__name = "UnACCEPT"

    # Setter for the age with validation
    def set_age(self, ag):
        if ag > 0:
            self.__age = ag
        else:
            self.__age = 0

    # Getter for the age
    def get_age(self):
        return self.__age

    # Greeting method
    def greetings(self):
        print("Hello", self.__name)

    # __str__ method to return a string representation of the person
    def __str__(self):
        return "The person's name is {} and the age is {}".format(self.__name, self.__age)

# Linear search function (to search for target age)
def linear_search(objects_list, target_age):
    for person in objects_list:
        if person.get_age() == target_age:
            return True
    return False

# Sorted linear search function (assuming the list is sorted by age)
def sorted_linear_search(objects_list, target_age):
    for person in objects_list:
        if person.get_age() == target_age:
            return True
        elif person.get_age() > target_age:
            return False  # Since the list is sorted, we can stop here
    return False

# Binary search function (assuming the list is sorted by age)
def binary_search(objects_list, target_age):
    low = 0
    high = len(objects_list) - 1
    while low <= high:
        mid = (low + high) // 2
        if objects_list[mid].get_age() == target_age:
            return True
        elif objects_list[mid].get_age() < target_age:
            low = mid + 1
        else:
            high = mid - 1
    return False

# Insertion sort function (to sort by age)
def insertion_sort(objects_list):
    for i in range(1, len(objects_list)):
        key_person = objects_list[i]
        j = i - 1
        while j >= 0 and key_person.get_age() < objects_list[j].get_age():
            objects_list[j + 1] = objects_list[j]
            j -= 1
        objects_list[j + 1] = key_person

# Selection sort function (to sort by age)
def selection_sort(objects_list):
    for i in range(len(objects_list)):
        min_index = i
        for j in range(i + 1, len(objects_list)):
            if objects_list[j].get_age() < objects_list[min_index].get_age():
                min_index = j
        objects_list[i], objects_list[min_index] = objects_list[min_index], objects_list[i]

# Bubble sort function (to sort by age)
def bubble_sort(objects_list):
    n = len(objects_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if objects_list[j].get_age() > objects_list[j + 1].get_age():
                objects_list[j], objects_list[j + 1] = objects_list[j + 1], objects_list[j]
                swapped = True
        if not swapped:
            break

# Helper function to print the list of people
def print_objects_list(objects_list):
    for person in objects_list:
        print(person)

def main():
    # Create five Person objects and add them to a list named objects_list
    p1 = Person("Alice", 25)
    p2 = Person("Bob", 30)
    p3 = Person("Charlie", 22)
    p4 = Person("Diana", 28)
    p5 = Person("Eve", 35)
    objects_list = [p1, p2, p3, p4, p5]
    insertion_sort(objects_list)
    print(binary_search(objects_list,2))
    print(linear_search(objects_list,23))
    print(sorted_linear_search(objects_list,30))
    print_objects_list(objects_list)

if __name__ == "__main__":
    main()