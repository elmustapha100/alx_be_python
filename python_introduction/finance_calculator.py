
monthly_income = int(float(input("Enter your monthly income: ")))
monthly_expenses = int(float(input("Enter your total monthly expenses: ")))
#Calcuating monthly savings 

monthly_savings = monthly_income - monthly_expenses
#Displying monthly_savings 
print(f"Your monthly savings are ${monthly_savings}.")

#Calculating projected annual savings at an assumed rate of 5% after a year 
projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))
print(f"Projected savings after one year, with interest, is ${projected_savings}.")
