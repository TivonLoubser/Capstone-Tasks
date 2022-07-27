# ===== Capstone One =====

import math

print("Hello Investor! \nWelcome to your Finance Calculator")
print("")                                                   # Just used as a spacer

calc_type = input('''Choose either 'investment' or 'bond' from the menu below to proceed:

investment   - to calculate the amount of interest you'll earn on interest
bond         - to calculate the amount you'll have to pay on a home loan
:''')
low_type = calc_type.lower()
    # Above ''' is used to denote a long string of text
    # The .lower() fn is utilized to remove case sensitivity for user input
print("")


if low_type == "investment":
    p = float(input("How much money are you investing:"))   # User inputs all converted to relevant data type i.e. float

    rate = float(input("What is the interest rate (Don't include the %):"))
    r = rate/10

    t = float(input("How many years to maturity:"))

    interest = input("Do you want 'simple' or 'compound' interest:")
    if interest == "simple":                                # Secondary if statement for choice between simple and compound
            print("Total amount =", p*(1+r*t))
    else:
            print("Total amount =", p*math.pow((1+r),t))


elif low_type == "bond":
    p = float(input("What is the present value of the house:"))

    rate = float(input("What is the interest rate (Don't include the %):"))
    i = rate/10

    n = float(input("How many months to maturity:"))
    
    print("Monthly repayment =", (i*p)/(1-(1+i))**(-n))


else:
    print("Error: please enter a valid input (i.e. 'investment' or 'bond')")

    




