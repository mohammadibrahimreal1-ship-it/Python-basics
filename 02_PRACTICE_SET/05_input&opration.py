num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

operation = input("Choose operation: ")

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        print(num1 / num2)
    case "%":
        print(num1 % num2)
    case "**":
        print(num1 ** num2)
    case "//":
        print(num1 // num2)
        