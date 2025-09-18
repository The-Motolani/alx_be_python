# request user input
number = int(input("Enter a number to see its multiplication table:"))
# iterate through numbers 1 - 10 with i representing iterative variable
for i in range(1, 11):
    # for every iterative variable of 1- 10 print formatted string of number * iterative variable on new line
    print(f"{number} * {i} = {number * i}")