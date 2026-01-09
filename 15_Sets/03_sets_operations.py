a = {3, 23, 1}
b = {23, 4, 2, 55, 1}

c = a.union(b)  #only unique values from both venn  (Take all values from A and B - removing duplicate)
print(c)

d = a.intersection(b)   #common values only
print(d)