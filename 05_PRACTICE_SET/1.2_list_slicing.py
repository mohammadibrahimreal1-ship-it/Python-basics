"""
Create a list of numbers from 1 to 10.

Print the first three numbers using slicing.
Print the last three numbers using slicing.
"""
# list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#Above jaisa bhi kar sakte h but aise hi zehen me aa gaya so I created using below method (wasie hi lol)
list = [i for i in range(1,11)]
print(list)

print(list[:3])
print(list[-3:])