# This program calculates your monthly savings and projects your annual savings with a 5% interest rate.
# Get user's monthly income and expenses
monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your total monthly expenses: "))
# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses
# To calculate annual savings
# (Projected Savings = Monthly Savings * 12 + (Monthly Savings * 12 * 0.05))
annual_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Display the results
print(f"Your monthly savings are: ${user_monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${user_annual_savings}.")