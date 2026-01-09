class Employee:
    company = "Asus"    #class attribute

    def __init__(self, name, age, bond, company):   #company here is an instance attribute
        self.name = name
        self.age = age
        self.bond = bond
        self.company = company


    def get_salary(self):
        return self.salary
    
    def get_info(self):
        print(f"Name is {self.name}. Age is {self.age}. Bond is {self.bond}")


e1 = Employee("Muhammad", 45000, 4, "Tesla")
print(e1.company)   #will always print instance attribute whenever present

#btw, if you want to print class attribute only
print(Employee.company)