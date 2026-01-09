#WAP that asks user for a no. and prints whether it is +ve, -ve or zero

user = int(input("Enter a number: "))

if (user > 0):
    print("Entered Number is positive")

elif(user < 0):
    print("Entered Number is negative")

else:
    print("Entered Number is 0")