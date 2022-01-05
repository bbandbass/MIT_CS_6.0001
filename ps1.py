#1 Part A: House Hunting

portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

while current_savings < total_cost * portion_down_payment:
    monthly_savings = annual_salary/12 * portion_saved
    monthly_returns = current_savings * r/12
    current_savings += monthly_savings + monthly_returns
    month += 1
print("Number of months:", month)


#Part B: Saving, with a raise

portion_down_payment = 0.25
current_savings = 0
r = 0.04
month = 0

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi_annual_raise, as a decimal: "))

while current_savings < total_cost * portion_down_payment:
    monthly_savings = annual_salary/12 * portion_saved
    monthly_returns = current_savings * r/12
    current_savings += monthly_savings + monthly_returns
    month += 1
    if month % 6 == 0:
        annual_salary = annual_salary * (1 + semi_annual_raise)
print("Number of months:", month)


#Part C: Finding the right amount to save away

annual_salary = float(input("Enter the starting salary: "))
min_savings_rate = 0
max_savings_rate = 10000
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
down_payment = portion_down_payment * total_cost
step = 0
diff = down_payment #down payment - current savings, current savings now 0 

def diff_payment_savings(savings_rate, salary):
    """
    Calcualtes the difference between your saving after 36 months and
    down payment given the saving rate
    """
    current_savings = 0
    month = 0
    while month < 36:
        monthly_savings = salary/120000 * savings_rate
        monthly_returns = current_savings * r/12
        current_savings += monthly_savings + monthly_returns
        month += 1
        if month % 6 == 0:
            salary = salary * (1 + semi_annual_raise)
    return down_payment - current_savings

if diff_payment_savings(max_savings_rate, annual_salary) > 0:
    print("It is not possible to pay the down payment in three years.")
    exit()

while abs(diff) > 100:
    best_savings_rate = (min_savings_rate + max_savings_rate)/2.0
    if diff_payment_savings(best_savings_rate, annual_salary) > 0:
        min_savings_rate = best_savings_rate
    else:
        max_savings_rate = best_savings_rate
    step += 1
    diff = diff_payment_savings(best_savings_rate, annual_salary)
print("Best savings rate:", round(best_savings_rate/10000, 4))
print("Steps in bisection search:", step)