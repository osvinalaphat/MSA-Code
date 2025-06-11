# hours worked daily
# hourly pay rate

#PROCESSING
#yearly pay = 350 * daily_rate * daily hours 
#tax amount = yearly pay * 0.12
#yearly pay with tax deduction = yearly pay -tax amount

# before tax deduction
# tax deduction amount 
# after tax deduction 

#first ask for hours worked and pay rate

def main():
    #get info
    #come back for while loops!!!!!!!!!!!!
    while True:
        try:
            daily_hours_worked = float(input("Enter the number of hours worked daily: "))
            if daily_hours_worked < 0 or daily_hours_worked >24:
                print("ERROR: Hours must be between 0 and 24")
                continue
            daily_pay_rate = float(input("Enter the hourly wage: "))
            if daily_pay_rate <0:
                 print("ERROR: Pay rate must be more than 0")
                 continue
        except:
            print("Please enter numbers")
            continue
        break

    yearly_pay_no_taxes = daily_hours_worked * daily_pay_rate * 350
    tax_amount = yearly_pay_no_taxes*0.12
    yearly_pay_with_taxes = yearly_pay_no_taxes - tax_amount

    print("\n")
    print("Pay Advice")
    print("------------")
    print(f"Hours Worked: {daily_hours_worked:.2f}")
    print(f"Hourly Wage: ${daily_pay_rate:.2f}")
    print(f"Wages Before Taxes: ${yearly_pay_no_taxes:.2f}")
    print(f"Tax Amount: ${tax_amount:.2f}")
    print(f"Annual Wage After Taxes: ${yearly_pay_with_taxes:.2f}")


main()
while True:
    run_code = input("Do you want to run this code again (y or n):")
    if run_code == "y":
        main()
    elif run_code == "n":
        break
    else:
        print("Please use y or n.")
        continue