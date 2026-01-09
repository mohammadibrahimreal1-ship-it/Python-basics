'''
Take a user input string and check if it is a palindrome (same forwards and backwards). e.g, madam, bob, "4554"
'''
string1 = input("Enter a string: ")

if(string1 == string1[::-1]):
    print("Entered string is a Palindrome.")
else:
    print("Entered string is not a Palindrome.")