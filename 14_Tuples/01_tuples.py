#Tuples() - immutable, ordered collections of items

a = (3, 4, 22, 13, 22)
print(a)
print(a[1])

# a[1] = 15       #error (it's immutable)
# print(a)

b = (1,)    #unlike list, tuple uses comma for creating a single element
print(b)


#Tuple unpacking
tu = (3, 2, 45)
a, b, c = tu
print(tu)

#Common tuple methods:
my_tuple = (1, 6, 6, 3, 4, 6 , 105)

print("\n")
print(my_tuple.count(6))   #count OF (value)
print(my_tuple.index(105))   #index OF (value)

# m_t = my_tuple.count(3) <--- Same answer
# print(m_t)

# m_tu = my_tuple.index(105) <--- Same answer
# print(m_tu)