#Class: Class is a blueprint or a template. Eg. Form for an exam that contains name, age, subject, father's name, etc
#Object: Specific instance created from the template (class) Eg. Form which contains the data for John Doe)


class Employee:
    company = "HP"

    def get_salary(self):   
        return 34000

e = Employee()
print(e.get_salary())

e2 = Employee()
print(e2.get_salary())
print(e2.company)




#Self is imp here because self is a way to reference the object of the class which is being created (my defn - self is must paramerter for 1st function... self = e (e is an object here) So, e or e2 are self)