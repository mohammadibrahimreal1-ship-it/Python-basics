"""
4. Sets and Set Methods
Create a set my_set = {1, 2, 3, 3, 4} and print it. (What happens to duplicate 3?)

Add 5 to the set, remove 2, and check if 4 is in the set.

Create two sets:

a = {1, 2, 3}
b = {3, 4, 5}

Find their:
Union
Intersection
Difference (a - b)
"""

my_set = {1, 2, 3, 3, 4}
print(my_set)   #3 printed 1x coz sets takes unique values and not duplicates

my_set.add(5)
print(my_set)

my_set.discard(2)
print(my_set)

if(4 in my_set):
    print("Yes, 4 is present in the set")


a = {1, 2, 3}
b = {3, 4, 5}

union = a.union(b)
intersection = a.intersection(b)
difference = a.difference(b) #means - a mein b se kya kya diff elements hain bas unhe hi print karta hain

print(union, intersection, difference)