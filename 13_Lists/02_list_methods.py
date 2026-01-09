marks = [2, 8, 41, 10, 9]
list2 = [914, 615]

marks.append(63)    #appends at the END only
print(marks)

marks.pop()         #pop LAST element only
print(marks)

marks.insert(1, 700)    #insert(index, value)
print(marks)

marks.extend(list2)     #concatinates 2 lists
print(marks)

marks.remove(8)     #simply removes 8
print(marks)

marks.reverse()     #reverse the original list
print(marks)

marks.sort()        #sort by assending
print(marks)

marks[4] = 10000    #therefore, mutable
print(marks)