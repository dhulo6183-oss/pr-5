# -------- Base Class --------
class Employee:

    # Constructor (runs when object is created)
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    # Function to show details
    def display(self):
        print("\nEmployee Details")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)


# -------- Manager Class (Inheritance) --------
class Manager(Employee):

    def __init__(self, emp_id, name, age, salary, department):
        super().__init__(emp_id, name, age, salary)   # call Employee constructor
        self.department = department

    def display(self):   # Method Overriding
        super().display()
        print("Department:", self.department)


# -------- Developer Class (Inheritance) --------
class Developer(Employee):

    def __init__(self, emp_id, name, age, salary, language):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def display(self):
        super().display()
        print("Programming Language:", self.language)


# -------- Check Inheritance --------
print("Manager is subclass of Employee:", issubclass(Manager, Employee))
print("Developer is subclass of Employee:", issubclass(Developer, Employee))


# -------- Menu Program --------
employee = None
manager = None
developer = None

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. Add Manager")
    print("3. Add Developer")
    print("4. Show Details")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # Create Employee
    if choice == "1":
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))

        employee = Employee(emp_id, name, age, salary)
        print("Employee Added!")

    # Create Manager
    elif choice == "2":
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        dept = input("Enter Department: ")

        manager = Manager(emp_id, name, age, salary, dept)
        print("Manager Added!")

    # Create Developer
    elif choice == "3":
        emp_id = input("Enter ID: ")
        name = input("Enter Name: ")
        age = int(input("Enter Age: "))
        salary = float(input("Enter Salary: "))
        lang = input("Enter Programming Language: ")

        developer = Developer(emp_id, name, age, salary, lang)
        print("Developer Added!")

    # Show Details (Simple Version)
    elif choice == "4":
        print("\n1. Show Employee")
        print("2. Show Manager")
        print("3. Show Developer")

        show = input("Enter choice: ")

        if show == "1":
            if employee:
                employee.display()
            else:
                print("No Employee Data!")

        elif show == "2":
            if manager:
                manager.display()
            else:
                print("No Manager Data!")

        elif show == "3":
            if developer:
                developer.display()
            else:
                print("No Developer Data!")

        else:
            print("Wrong Choice!")

    # Exit
    elif choice == "5":
        print("Program Ended.")
        break

    else:
        print("Invalid Choice!")
