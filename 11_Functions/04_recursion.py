#Example: Fibonacci (sum of previous 2 values) using Recursion
#Value:   0  1  1  2  3  5  8  13...
#Index:   0  1  2  3  4  5  6 ...

def fib(x):
    #base case
    if (x==0 or x==1):
        return x
    return fib(x-2) + fib(x-1)
print(fib(6))

"""
fib(4) + fib(5)
fib(2) + fib(3) + fib(3) + fib(4)
fib(0) + fin(1) + fib(1) + fib(2) + fib(1) + fib(2) +  fib(2) + fib(3)
fib(0) + fib(1) + fin(1) + fib(0) + fib(1) + fib(1) + fib(0) + fib(1)  + fib(0) + fib(1) + fib(1) + fib(2)

fib(0) + fib(1) + fin(1) + fib(0) + fib(1) + fib(1) + fib(0) + fib(1)  + fib(0) + fib(1) + fib(1) + fib(0) + fib(1)

0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 = 8
"""


#Another e.g,
#Value:   0  1  1  2  3  5  8  13...
#Index:   0  1  2  3  4  5  6 ...

def fib(x):
    #base case
    if (x==0 or x==1):
        return x
    return fib(x-2) + fib(x-1)
print(fib(4))

"""
fib(4)
fib(2) + fib(3)
fib(0) + fib(1) + fib(1) + fib(2)
fib(0) + fib(1) + fib(1) + fib(0) + fib(1)

0+1+1+0+1 = 3
"""