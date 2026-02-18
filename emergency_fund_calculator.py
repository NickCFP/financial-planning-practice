"""

Title: Recommended Emergency Fund Calculator
Author: Nick Holeman
Original Creation Date: February 17th, 2026

Description: This script will ask the user a series of questions to assess their financial
stability, and based on their responses, will recommend how large their emergency fund 
should be.

Financial Logic/Assumptions:
- I will frame emergency fund size in terms of how many months of living expenses it will
cover for a given user (i.e., I recommend you have a $30,000 emergency fund which is enough
to cover ~3 months of living expenses).
- My recommendations of emergency fund size is 3 months of living expenses on
the low end, and 12 months of living expenses on the high end. This is somewhat subjective 
but is in line with industry norms and my professional opinion.
- I have identified multiple variables that directionally impact how small/large an emergency fund
should be. I am purposely choosing variables that are more objective (i.e., do you have 
dependents?) as opposed to questions that are more subjective (i.e., what is your risk 
tolerance?). This script is intended to be the more objective starting point for determining 
emergency fund size. Afterwards, a user could layer on their subjective feelings.
- I am intentionally keeping the mathematical formula in this script very simple. By 
definition, it is impossible to predict when an emergency will occur or how much it will 
cost. Thus, a scientific way of determining the precise size an emergency fund should be is 
not possible.
- Each variable can have a numerical value of between 0-2. Each variable is equally-weighted.
When summed together, the value results in a the user's total risk score. The risk score is
then used to place the user on the spectrum of a 3-month emergency fund to a 12-month 
emergency fund, using a simple linear mapping.
"""

##### Gather inputs. #####
# 1. Gather monthly expenses.
monthly_expenses = float(input("Enter your monthly expenses: "))

# 2. Gather job security.
job_security = float(input("Rank your job security using the following scale "
"(0 = retired, 1 = dual-income, 2 = single-income): "))

# 3. Gather income stability.
income_stability = float(input("Rank your income stability using the following scale "
"(0 = very stable, 1 = somewhat stable, 2 = not stable): "))

# 4. Gather health status.
health_status = float(input("Rank your health status using the following scale "
"(0 = very healthy, 1 = somewhat healthy, 2 = not healthy): "))

# 5. Gather insurance coverage.
insurance_coverage = float(input("Rank your insurance coverage using the following scale "
"(0 = very adequate, 1 = somewhat adequate, 2 = not adequate): "))

# 6. Gather ability to reduce expenses.
ability_to_reduce_expenses = float(input("Rank your ability to reduce expenses using the following scale "
"(0 = very flexible, 1 = somewhat flexible, 2 = not flexible): "))

# 7. Gather dependent details.
has_dependents = float(input("Tell us if you have dependents using the following scale "
"(0 = no dependents, 2 = yes dependents): "))

# 8. Gather primary residence details.
owns_primary_residence = float(input("Tell us if you own or rent your primary residence using the following scale "
"(0 = rent, 2 = own): "))

# 9. Gather support network details.
support_network = float(input("Rank your support network using the following scale "
"(0 = very strong, 1 = somewhat strong, 2 = not strong): "))

# 10. Gather credit access details.
low_cost_credit_access = float(input("Rank your ability to access low-cost credit using the following scale "
"(0 = very strong, 1 = somewhat strong, 2 = not strong): "))

##### Run calculations. #####
recommended_months_of_expenses = 3 + sum([
    job_security,
    income_stability,
    health_status,
    insurance_coverage,
    ability_to_reduce_expenses,
    has_dependents,
    owns_primary_residence,
    support_network,
    low_cost_credit_access
])
recommended_emergency_fund = round(recommended_months_of_expenses * monthly_expenses)

##### Share output. #####
print(
    "I recommend your emergency fund be $", 
      f"{recommended_emergency_fund:,}"
      " which should cover approximately ",
      recommended_months_of_expenses, 
      " months of your living expenses."
      )