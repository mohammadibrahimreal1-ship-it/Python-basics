#The __init__ method is special. It's called the constructor. It's automatically run whenever you create a new object from a class.

class Employee:

    def __init__(self, salary, name, bond): #Constructor
        self.salary = salary
        self.name = name
        self.bond = bond

    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name of employee is {self.name}. Salary is {self.salary} and bond is {self.bond} years")

    def get_name(self):
        print(self.name)
    
e1 = Employee(34000, "Allama", 3)
 #print(obj.get_salary())
e1.get_info()
e1.get_name()