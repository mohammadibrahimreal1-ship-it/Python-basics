#Set methods

s = {1, 2, 3, 4}

s.add(93)
print(s)

s.remove(2)
print(s)
#s.remove(234567)   #throws an error if value is not present

s.discard(234567)  #remove value if present otherwise don't throw an error (alterate for remove)
print(s)