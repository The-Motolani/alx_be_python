# This program assumes the year is 2023 and calculates how old you will be in the year 2050 based on your current age.
# requests user input for current age.

# Define function that validates input to ensure age is non-negative
def get_valid_age(prompt):
# Loop until a valid age is entered
    while True:
        try:
            age = int(input(prompt))
            if age >= 0:
                return age
            else:
                print("Age cannot be negative. Please enter a valid age.")
        except ValueError:
            print("Invalid input. Please enter a numeric value for age.")
# Get user's current age
user_current_age = (get_valid_age("How old are you? "))
# Calculate future age in 2050
user_future_age = user_current_age + 27
# Display the result
print(f"In 2050, you will be {user_future_age} years old.")