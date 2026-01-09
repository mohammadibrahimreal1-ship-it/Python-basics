my_dict = {"Name":"Ibrahim", "Age":20, "Course":"Python"}
print(my_dict)

print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

my_dict.pop("Course")       #pops pair of course
print(my_dict)

my_dict.clear()
print(my_dict)