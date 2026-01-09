"""Create 2 dict class1 = {"Harry":56, "Bilal":90}
class2 = {"Shamail":56, "Ahmad":90} and merge them"""

class1 = {"Harry":56, "Bilal":90}
class2 = {"Shamail":56, "Ahmad":90}

merged_class = class1 | class2
print(merged_class)