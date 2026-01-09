#TYPE OF argument

#1st - default argument
def add(a,b, plus=0):   #note: always place 'default arg' at very end of parameters 
    return a+b+plus

c = add(3,5)
print(c)

#2nd e.g, with value overwrite of default arg
def add(a,b, plus=0):
    return a+b  

c = add(3,5,2)
print(c)

#Now, keyword argument (often used)
def student(name, age):
    print(f"My name is {name} and age is {age}.")

student(age=20, name="Bilal")