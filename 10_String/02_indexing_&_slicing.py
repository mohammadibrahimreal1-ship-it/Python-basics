'''
[start:stop:step]
name = "S a l a h u d d i n"
        0 1 2 3 4 5 6 7 8 9 
'''

#String Indexing
text = "Python"
print(text[0])  # Output: P
print(text[1])  # Output: y
print(text[-1]) # Output: n (last character)
print(text[-2]) # Output: o


#String Slicing
print("\n")
text = "Hello, Python!"
print(text[0:5])   # Output: Hello
print(text[:5])    # Output: Hello (same as text[0:5])
print(text[7:])    # Output: Python! (from index 7 to end)
print(text[::2])   # Output: Hlo Pto!
print(text[-6:-1]) # Output: ython (negative indexing)


#Step Parameter
print("\n")
text = "Python Programming"
print(text[::2])   # Output: Pto rgamn
print(text[::-1])  # Output: gnimmargorP nohtyP (reverses string)



"""
SUMMARY: - 
Indexing allows accessing individual characters.
Positive indexing starts from 0, negative indexing starts from -1.
Slicing helps extract portions of a string.
The step parameter defines the interval for selection.
Using [::-1] reverses a string.

"""