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
        mid_age = objects_list[mid].get_price()
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
            if objects_list[j].get_price() > objects_list[j + 1].get_price():
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
                            managers_lists.append(Manager(name=data["name"],age=data["age"],employee_id=data["employee_id"],position=data["position"],department=data["department"],team_size=data["team_size"]))
                except:
                    print("ERROR")

def save_file(objects_list,file_name):
    data=[]
    with open(file_name, 'w+') as file:
        for obj in objects_list:
            if file_name=="Employee.json":
                obj_type = "Employee"
                obj_data = {
                    "type": obj_type,
                    "name": obj.get_name(),
                    "age": obj.get_age(),
                    "employee_id": obj.get_employee_id(),
                    "position": obj.get_position()
                }
            elif file_name=="Manager.json":
                obj_type = "Manager"
                obj_data = {
                    "type": obj_type,
                    "name": obj.get_name(),
                    "age": obj.get_age(),
                    "team_size": obj.get_team_size(),
                    "employee_id": obj.get_employee_id(),
                    "position": obj.get_position(),
                    "department": obj.get_department()
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
################# Menu Functions ################
# Menu Functions
def insert_menu():
    while True:
        print("\nInsert Menu:")
        print("1. Insert Employee")
        print("2. Insert Manager")
        print("3. Insert Customer")
        print("4. Insert Product")
        print("5. Insert Order")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Enter employee name: ")
            age = int(input("Enter employee age: "))
            employee_id = input("Enter employee ID (e.g., E001): ")
            position = input("Enter position: ")
            emp = Employee(name, age, employee_id, position)
            employees_lists.append(emp)
            print("Employee added successfully.")
        elif choice == '2':
            name = input("Enter manager name: ")
            age = int(input("Enter manager age: "))
            employee_id = input("Enter manager ID (e.g., E002): ")
            position = input("Enter position: ")
            department = input("Enter department: ")
            team_size = int(input("Enter team size: "))
            mgr = Manager(name, age, employee_id, position, department, team_size)
            managers_lists.append(mgr)
            print("Manager added successfully.")
        elif choice == '3':
            name = input("Enter customer name: ")
            age = int(input("Enter customer age: "))
            customer_id = input("Enter customer ID (e.g., C001): ")
            email = input("Enter email: ")
            cust = Customer(name, age, customer_id, email)
            customers_lists.append(cust)
            print("Customer added successfully.")
        elif choice == '4':
            product_id = input("Enter product ID (e.g., P001): ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            prod = Product(product_id, name, price)
            products_lists.append(prod)
            print("Product added successfully.")
        elif choice == '5':
            # For simplicity, an Order can be a string describing the order
            order_description = input("Enter order description: ")
            orders.push(order_description)
            print("Order added to stack successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def search_menu():
    while True:
        print("\nSearch Menu:")
        print("1. Search Employee by Age (linear_search)")
        print("2. Search Manager by Age (linear_search)")
        print("3. Search Customer by Age (sorted_linear_search)")
        print("4. Search Product by Price (binary_search)")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            target_age = int(input("Enter target age: "))
            result = linear_search(employees_lists, target_age)
            print(f"Employee with age {target_age} found: {result}")
        elif choice == '2':
            target_age = int(input("Enter target age: "))
            result = linear_search(managers_lists, target_age)
            print(f"Manager with age {target_age} found: {result}")
        elif choice == '3':
            target_age = int(input("Enter target age: "))
            selection_sort(customers_lists)
            result = sorted_linear_search(customers_lists, target_age)
            print(f"Customer with age {target_age} found: {result}")
        elif choice == '4':
            target_price = float(input("Enter target price: "))
            # Implement a search for products_lists with the target price
            result=binary_search(products_lists,target_price)
            print(f"Product with price {target_price} found: {result}")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def delete_menu():
    global employees_lists
    global managers_lists
    global products_lists
    global customers_lists
    while True:
        print("\nDelete Menu:")
        print("1. Delete Employee by ID")
        print("2. Delete Manager by ID")
        print("3. Delete Customer by ID")
        print("4. Delete Product by ID")
        print("5. Delete Order (Pop from Stack)")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            emp_id = input("Enter employee ID to delete: ")
            initial_len = len(employees_lists)
            for i in range(len(employees_lists)):
                if employees_lists[i].get_employee_id() == emp_id:
                    employees_lists=employees_lists[:i]+employees_lists[(i+1):]
                    break
            if len(employees_lists) < initial_len:
                print("Employee deleted successfully.")
            else:
                print("Employee ID not found.")
        elif choice == '2':
            mgr_id = input("Enter manager ID to delete: ")
            initial_len = len(managers_lists)
            for i in range(len(managers_lists)):
                if managers_lists[i].get_employee_id() == mgr_id:
                    managers_lists=managers_lists[:i]+managers_lists[(i+1):]
                    break
            if len(managers_lists) < initial_len:
                print("Manager deleted successfully.")
            else:
                print("Manager ID not found.")
        elif choice == '3':
            cust_id = input("Enter customer ID to delete: ")
            initial_len = len(customers_lists)
            for i in range(len(customers_lists)):
                if customers_lists[i].get_customer_id() == cust_id:
                    customers_lists=customers_lists[:i]+customers_lists[(i+1):]
                    break
            if len(customers_lists) < initial_len:
                print("Customer deleted successfully.")
            else:
                print("Customer ID not found.")
        elif choice == '4':
            prod_id = input("Enter product ID to delete: ")
            initial_len = len(products_lists)
            for i in range(len(products_lists)):
                if products_lists[i].get_product_id() == prod_id:
                    products_lists=products_lists[:i]+products_lists[(i+1):]
                    break
            if len(products_lists) < initial_len:
                print("Product deleted successfully.")
            else:
                print("Product ID not found.")
        elif choice == '5':
            removed_order = orders.pop()
            if removed_order:
                print(f"Order '{removed_order}' removed from stack.")
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def sort_menu():
    while True:
        print("\nSort Menu:")
        print("1. Sort Employees by Age (Insertion Sort)")
        print("2. Sort Managers by Age (Insertion Sort)")
        print("3. Sort Customers by Age (Selection Sort)")
        print("4. Sort Products by Price (Bubble Sort)")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")

        if choice == '1':
            # Sort employees by age using Bubble Sort
            insertion_sort(employees_lists)
            print("Employees sorted by age (Insertion Sort):")
            print_object(employees_lists)

        elif choice == '2':
            # Sort managers by age using Insertion Sort
            insertion_sort(managers_lists)
            print("Managers sorted by age (Insertion Sort):")
            print_object(managers_lists)

        elif choice == '3':
            # Sort customers by age using Selection Sort
            selection_sort(customers_lists)
            print("Customers sorted by age (Selection Sort):")
            print_object(customers_lists)

        elif choice == '4':
            # Sort products by price using Bubble Sort
            bubble_sort(products_lists)
            print("Products sorted by price (Bubble Sort):")
            print_object(products_lists)

        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")


def display_menu():
    while True:
        print("\nDisplay Menu:")
        print("1. Display All Employees")
        print("2. Display All Managers")
        print("3. Display All Customers")
        print("4. Display All Products")
        print("5. Display All Orders")
        print("6. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            print("\nEmployees:")
            print_object(employees_lists)
        elif choice == '2':
            print("\nManagers:")
            print_object(managers_lists)
        elif choice == '3':
            print("\nCustomers:")
            print_object(customers_lists)
        elif choice == '4':
            print("\nProducts:")
            print_object(products_lists)
        elif choice == '5':
            print("\nOrders Stack:")
            print(orders)
        elif choice == '6':
            break
        else:
            print("Invalid option. Please try again.")

def save_menu():
    while True:
        print("\nSave Menu:")
        print("1. Save Employees to File")
        print("2. Save Managers to File")
        print("3. Save Customers to File")
        print("4. Save Products to File")
        print("5. Back to Main Menu")
        choice = input("Select an option: ")
        
        if choice == '1':
            save_file(employees_lists,"Employee.json")
            print("Employees saved to file successfully.")
        elif choice == '2':
            save_file(managers_lists,"Manager.json")
            print("Managers saved to file successfully.")
        elif choice == '3':
            save_file(customers_lists,"Customer.json")
            print("Customers saved to file successfully.")
        elif choice == '4':
            save_file(products_lists,"Product.json")
            print("Products saved to file successfully.")
        elif choice == '5':
            break
        else:
            print("Invalid option. Please try again.")

def main_menu():
    while True:
        print("\n--- Restaurant Management System ---")
        print("1. Insert Records")
        print("2. Search Records")
        print("3. Delete Records")
        print("4. Display Records")
        print("5. Save Records to File")
        print("6. Sort Records")
        print("7. Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            insert_menu()
        elif choice == '2':
            search_menu()
        elif choice == '3':
            delete_menu()
        elif choice == '4':
            display_menu()
        elif choice == '5':
            save_menu()
        elif choice == '6':
            sort_menu()
        elif choice == '7':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

############ main function ##########################
if __name__ == "__main__":
    read_file("Manager.json")
    read_file("Product.json")
    read_file("Customer.json")
    read_file("Employee.json")
    orders=Stack()
    main_menu()
    