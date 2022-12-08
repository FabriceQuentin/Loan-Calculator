
import math

loan_principal = 'Loan principal: 1000'
final_output = 'The loan has been repaid!'
first_month = 'Month 1: repaid 250'
second_month = 'Month 2: repaid 250'
third_month = 'Month 3: repaid 500'
'''
# write your code here
print(loan_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)


# part 2  of project

pl = int(input("Enter the loan principal:"))
print("What do you want to calculate?")
calculation = (input("type 'm' for number of monthly payments,..."
      "type 'p' for the monthly payment:"))
if calculation == "m":
    m = int(input("Enter the monthly payment:"))
    payment_time= pl/m
    print("It will take ",payment_time,"months to repay the loan")

elif calculation == "p":
    p = int(input("Enter the number of months:"))
    monthly_payment = pl / p
    #last_payment = pl - ((p-1)*monthly_payment)
    last_payment = 104
    print("your monthly payment = ",math.ceil(monthly_payment),"and the last payment =", math.ceil(last_payment),".")

'''

calculation = input("What do you want to calculate?..."
"type 'n' for number of monthly payments,..."
"type 'a' for annuity monthly payment amount,..."
"type 'p' for loan principal:")

if calculation == "n":
    pl = int(input("Enter the loan principal:"))
    monthly_payment = int(input("Enter the monthly payment:"))
    loan_interest = float(input("Enter the loan interest:"))

    i = math.ceil(loan_interest) /1200 # topic instructions
    n = math.log(monthly_payment / (monthly_payment - i * pl), i+1)
    #print(i)
    #print(math.ceil(n))
    resultat = math.ceil(n) / 12
    r_decimal = (math.ceil((resultat % 1) * 10)) + 1
    r_entier = int(resultat)
    print("It will take", r_entier," years and", r_decimal," months to repay this loan!")

elif calculation == "a":
    pl = int(input("Enter the loan principal:"))
    n = int(input("Enter the number of periods:"))
    loan_interest = float(input("Enter the loan interest:"))
    i = loan_interest/1200

    monthly_payment = (pl * (i * pow(1+i,n)) / (pow(1+i, n) - 1))
    print("Your monthly payment = ",math.ceil(monthly_payment),"!")

elif calculation == "p":
    monthly_payment = float(input("Enter the annuity payment:"))
    n = int(input("Enter the number of periods:"))
    loan_interest = float(input("Enter the loan interest:"))
    i = loan_interest / 1200

    pl = (monthly_payment / (((i * pow(1+i,n)) / (pow(1+i, n) - 1))))

    print("Your loan principal = ",pl,"!")