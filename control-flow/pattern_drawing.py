#prompts the user for the size of the pattern
pattern_size = int(input("Enter the size of the pattern:"))
# start with first row
row = 1
#while loop for rows
while count < pattern_size:
    #for loop for columns
    for i in range(pattern_size):
        # print * side by side
        print("*", end="")
    # After finishing a row, go to next line
    print()
    count += 1