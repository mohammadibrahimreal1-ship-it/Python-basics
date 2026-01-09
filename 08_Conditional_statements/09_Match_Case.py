a = int(input("Enter a number b/w 1-10: "))

match a:
    case 1:
        print("You won a charger")
    case 8:
        print("You won $5")
    case 2:
        print("You won a camera")
    case _:
        print("Sorry, you won nothing")      



#Let me have one more example 
IQ = int(input("Enter your IQ: "))

match IQ:
    case 90:
        print("You are an Average")
    case 130:
        print("You are Smart")
    case 170:
        print("You are Genius")
    case _:
        print("Entered IQ number is not in the list")