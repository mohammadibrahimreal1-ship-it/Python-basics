"""
3. Tuples and Operations on Tuples
Create a tuple coordinates = (10, 20) and 
3.1 print both elements.
3.2 Try to modify the tuple by setting coordinates[0] = 50 — note what happens.
3.3 Convert the tuple to a list, change its first element to 50, and convert it back to a tuple.
"""

coordinates = (10, 20)
print(coordinates[0])
print(coordinates[1])

# coordinates[0] = 50
# print(coordinates)
#Throws an error as tuples are immutable

corlist = list(coordinates)
corlist[0] = 50
coordinates = tuple(corlist)
print(coordinates)