s = " khan Mohammad ibrahim  " #Stings are immutable
a = len(s)
print(a)

print(s.upper(), s) 
#So, original string remains intacted.. means it is not changed in memeory. We have just created a new/copy/dummy string (IMMUTABILITY)
print(s.title())
print(s.rstrip())
print(s.lstrip())
print(s.capitalize())


text = "Python Python is fun"
print(text.find("is"))
print(text.replace("Python", "DataScience"))

str = "Apple, Banana, Watermelon"
print(str.split(","))
print(",".join(['Apple', 'Banana', 'Watermelon']))