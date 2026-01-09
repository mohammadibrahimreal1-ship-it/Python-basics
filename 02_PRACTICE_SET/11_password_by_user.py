#Ask user for password until the correct one

real_pass = "IamPass155"
user_pass = input("Enter the passwor: ")

while (user_pass != real_pass):
    user_pass = input("Wrong Password! Try again & enter password: ")

    if(user_pass == real_pass):
        print("Entered password is correct")
    else:
        print("Please enter the correct password") 