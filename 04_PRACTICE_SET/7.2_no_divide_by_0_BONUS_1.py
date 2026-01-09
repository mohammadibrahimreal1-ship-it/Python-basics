#WA fucntion safe_divide(a,b) that returns the result of a/b, but returns "Cannot divide by Zero" if b is 0.

def safe_divide(a,b):
    if(b==0):
        print("Cannot divide by Zero")
    else:
        return a/b
    
print(safe_divide(4,2))
print(safe_divide(6,0))