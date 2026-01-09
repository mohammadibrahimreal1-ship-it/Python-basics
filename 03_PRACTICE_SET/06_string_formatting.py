"""
String Formatting and f-Strings - 
Using format(), create a sentence:
"My name is John and I am 25 years old."
by passing "John" and 25 as variables.

Do the same using f-strings.
"""

name = "Ibrahim"
age = 25
#Using f string
print(f"My name is {name} and I am {age} years old.")

print("My name is {} and I am {} years old.".format(name, age))