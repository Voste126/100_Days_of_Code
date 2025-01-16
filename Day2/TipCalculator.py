# Basic Operators
# Learn to use the basic mathematical operators, +, -, *, /, // and **

# PEMDAS
# Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
#operation are prioritized in the order of PEMDAS


print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip_percent= tip/100
tip_to_pay= bill * tip_percent
total_bill = bill + tip_to_pay
bill_per_person = total_bill/people
final = round(bill_per_person,2)

print(f"The bill to be paid per person is: {final}")