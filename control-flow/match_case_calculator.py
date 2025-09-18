# a python script that prompts the user to enter two numbers and select an operation to be performed.
# prompts user  for number
# first number
num1 = int(input("Enter the first number:"))
# second number
num2 = int(input("Enter the second number:"))
# asks user for operation they want to perform
operation = input("Choose the operation (+, -, *, /):") 
# match the operation to the process
match operation:
    case "+":
        addition = num1 + num2
        print(f"The result is {addition}.")
    case "-":
        subtraction = num1 - num2
        print(f"The result is {subtraction}.")
    case "*":
        multiplication = num1 * num2
        print(f"The result is {multiplication}.")
    case "/" if num2 != 0:
        division = num1 / num2
        print(f"The result is {division}.")
    case "/":
        print("You can not divide by 0")
    case _:
        print("Invalid operation selected.")