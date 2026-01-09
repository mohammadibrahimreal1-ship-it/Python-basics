def mul(a,b):
    #a and b are local variables
    c = a*b
    z = 1   #this z (local variable) created will be destroyed after this function 'returns'
    return c

z = 8       #global varibale
print(z)
print(mul(4,3))


def greet():
    z = 20
    print("Hello")
print(z)