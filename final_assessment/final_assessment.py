import json
import os
############################ Classes ##############################

# class Person
class Person:
    def __init__(self, name="Unknown", age=0):
        self.set_name(name)
        self.set_age(age)
    
    # Getters
    def get_name(self):
        return self.__name
    
    def get_age(self):
        return self.__age
    
    # Setters
    def set_name(self, name):
        if name.isalpha():
            self.__name = name
        else:
            self.__name = "InvalidName"
    
    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            self.__age = 0
    
    def __str__(self):
        return f"Name: {self.__name}, Age: {self.__age}"

# Child class Employee
class Employee(Person):
    def __init__(self, name="Unknown", age=0, employee_id="E000", position="Staff"):
        super().__init__(name, age)
        self.set_employee_id(employee_id)
        self.set_position(position)
    
    # Getters
    def get_employee_id(self):
        return self.__employee_id
    
    def get_position(self):
        return self.__position
    
    # Setters
    def set_employee_id(self, employee_id):
        if employee_id[0]=="E" and employee_id[1:].isdigit():
            self.__employee_id = employee_id
        else:
            self.__employee_id = "InvalidID"
    
    def set_position(self, position):
        self.__position = position
    
    def __str__(self):
        return super().__str__() + f", Employee ID: {self.__employee_id}, Position: {self.__position}"

# Child class Manager
class Manager(Employee):
    def __init__(self, name="Unknown", age=0, employee_id="E000", position="Manager", department="General", team_size=0):
        super().__init__(name, age, employee_id, position)
        self.set_department(department)
        self.set_team_size(team_size)
    
    # Getters
    def get_department(self):
        return self.__department
    
    def get_team_size(self):
        return self.__team_size
    
    # Setters
    def set_department(self, department):
        self.__department = department
    
    def set_team_size(self, team_size):
        if team_size >= 0:
            self.__team_size = team_size
        else:
            self.__team_size = 0
    
    def __str__(self):
        return super().__str__() + f", Department: {self.__department}, Team Size: {self.__team_size}"

# Child class Customer
class Customer(Person):
    def __init__(self, name="Unknown", age=0, customer_id="C000", email="unknown@example.com"):
        super().__init__(name, age)
        self.set_customer_id(customer_id)
        self.set_email(email)
    
    # Getters
    def get_customer_id(self):
        return self.__customer_id
    
    def get_email(self):
        return self.__email
    
    # Setters
    def set_customer_id(self, customer_id):
        if customer_id[0] =="C" and customer_id[1:].isdigit():
            self.__customer_id = customer_id
        else:
            self.__customer_id = "InvalidID"
    
    def set_email(self, email):
        if "@" in email and "." in email:
            self.__email = email
        else:
            self.__email = "InvalidEmail"
    
    def __str__(self):
        return super().__str__() + f", Customer ID: {self.__customer_id}, Email: {self.__email}"

# Class Product
class Product:
    def __init__(self, product_id="P000", name="Unknown", price=0.0):
        self.set_product_id(product_id)
        self.set_name(name)
        self.set_price(price)
    
    # Getters
    def get_product_id(self):
        return self.__product_id
    
    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    
    # Setters
    def set_product_id(self, product_id):
        if product_id[0]=="P" and product_id[1:].isdigit():
            self.__product_id = product_id
        else:
            self.__product_id = "InvalidID"
    
    def set_name(self, name):
        self.__name = name
    
    def set_price(self, price):
        if price >= 0:
            self.__price = price
        else:
            self.__price = 0.0
    
    def __str__(self):
        return f"Product ID: {self.__product_id}, Name: {self.__name}, Price: ${self.__price:.2f}"
    
##################### Stack data structure implementation to manage Order objects ############################
class Stack:
    def __init__(self):
        self.__items = []
    
    def push(self, item):
        self.__items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.__items.pop()
        else:
            print("Stack is empty.")
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.__items[-1]
        else:
            print("Stack is empty.")
            return None
    
    def is_empty(self):
        return len(self.__items) == 0
    
    def size(self):
        return len(self.__items)
    
    def __str__(self):
        return "Stack contains:\n" + "\n".join(str(item) for item in reversed(self.__items))
    
####### search functions ############

# Linear Search
def linear_search(objects_list, target_age):
    for obj in objects_list:
        if obj.get_age() == target_age:
            return True
    return False

# Sorted Linear Search (assuming the list is sorted by age)
def sorted_linear_search(objects_list, target_age):
    for obj in objects_list:
        if obj.get_age() == target_age:
            return True
        elif obj.get_age() > target_age:
            return False
    return False

# Binary Search (assuming the list is sorted by age)
def binary_search(objects_list, target_age):
    low = 0
    high = len(objects_list) - 1
    while low <= high:
        mid = (low + high) // 2
        mid_age = objects_list[mid].get_age()
        if mid_age == target_age:
            return True
        elif mid_age < target_age:
            low = mid + 1
        else:
            high = mid - 1
    return False

######## sorting functions #############

# Bubble Sort
def bubble_sort(objects_list):
    n = len(objects_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i -1):
            if objects_list[j].get_age() > objects_list[j + 1].get_age():
                objects_list[j], objects_list[j + 1] = objects_list[j + 1], objects_list[j]
                swapped = True
        if not swapped:
            break

# Insertion Sort
def insertion_sort(objects_list):
    for i in range(1, len(objects_list)):
        key = objects_list[i]
        j = i -1
        while j >=0 and key.get_age() < objects_list[j].get_age():
            objects_list[j +1] = objects_list[j]
            j -=1
        objects_list[j +1] = key

# Selection Sort
def selection_sort(objects_list):
    for i in range(len(objects_list)):
        min_idx = i
        for j in range(i +1, len(objects_list)):
            if objects_list[j].get_age() < objects_list[min_idx].get_age():
                min_idx = j
        objects_list[i], objects_list[min_idx] = objects_list[min_idx], objects_list[i]

########### saving and reading objects from file #################
customers_lists=[]
products_lists=[]
employees_lists=[]
managers_lists=[]

def read_file(file_name):
        if os.path.isfile(file_name):
            with open(file_name, 'r') as file:
                try:
                    datas = json.load(file)
                    
                    for data in datas:
                        if data["type"] == "Customer":
                            customers_lists.append(Customer(name=data["name"],age=data["age"],customer_id=data["customer_id"],email=data["email"]))
                        elif data["type"] == "Employee":
                            employees_lists.append(Employee(name=data["name"],age=data["age"],employee_id=data["employee_id"],position=data["position"]))
                        elif data["type"] == "Product":
                            products_lists.append(Product(name=data["name"],price=data["price"],product_id=data["product_id"]))
                        elif data["type"] == "Manager":
                            print(data)
                            managers_lists.append(Manager(name=data["name"],age=data["age"],employee_id=data["employee_id"],position=data["position"],department=data["department"],team_size=data["team_size"]))
                except:
                    pass

def save_file(objects_list,file_name):
    data=[]
    with open(file_name, 'w+') as file:
        for obj in objects_list:
            if isinstance(obj, Employee):
                obj_type = "Employee"
                obj_data = {
                    "type": obj_type,
                    "name": obj.get_name(),
                    "age": obj.get_age(),
                    "employee_id": obj.get_employee_id(),
                    "position": obj.get_position()
                }
            elif isinstance(obj, Manager):
                obj_type = "Manager"
                obj_data = {
                    "type": obj_type,
                    "name": obj.get_name(),
                    "age": obj.get_age(),
                    "employee_id": obj.get_employee_id(),
                    "position": obj.get_position(),
                    "department": obj.get_department(),
                    "team_size": obj.get_team_size()
                }
            elif isinstance(obj, Customer):
                obj_type = "Customer"
                obj_data = {
                    "type": obj_type,
                    "name": obj.get_name(),
                    "age": obj.get_age(),
                    "customer_id": obj.get_customer_id(),
                    "email": obj.get_email()
                }
            elif isinstance(obj, Product):
                obj_type = "Product"
                obj_data = {
                    "type": obj_type,
                    "product_id": obj.get_product_id(),
                    "name": obj.get_name(),
                    "price": obj.get_price()
                }
            else:
                continue  # Unknown type
            data.append(obj_data)
        json.dump(data, file)

########### For displaying the objects ##############

def print_object(objects):
    if not objects:
        print("No records found.")
    else:
        for obj in objects:
            print(obj)

if __name__ == "__main__":
    # read_file("Manager.json")
    # read_file("Product.json")
    # read_file("Customer.json")
    # read_file("Employee.json")
    # print_object(managers_lists)
    # print_object(employees_lists)
    # print_object(customers_lists)
    # print_object(products_lists)
    m1=Manager(name="Turuu",age=23,employee_id="E002",position="Manager",department="meadowbank",team_size=12)
    managers_lists.append(m1)
    save_file(managers_lists,"Manager.json")
    