#vending machine
#Display the amount due
#Prompt the user to enter a coin
#Accepted denominations for coins are (1, 5, 10, 25)
#Program should ignore any input that is not a valid input and re prompt the user to input a coin
#Process the input and display the updated amount due
#Once the user has inputted at least 50 cents, output how many cents in change the user is owed
#End program

#-----------------------------------------------------------------------------------------------
# initialize amount owed at 50
# before while loop show amount owed : 50
# while true check if the amount owed is zero or less than 0 then break
#
# prompt them an input, 
# validate with a try except when turning into int ; make the except run a continue
# if an inserted amount is not 1, 5, 10, 25 then make them repeat and tell them why
# subtract from total and show amount remaining ;  repeat

def main():
    amount_owed = 50
    print("Vending Machine")
    print("---------------------")
    while True:
        if amount_owed <=0:
            print(f"Change owed: ¢{abs(amount_owed)}") 
            break
        print(f"Amount owed: ¢{amount_owed}")
        
        try:
            amount_submitted = int(input(f"Insert coin: ¢"))
            if amount_submitted not in [1,5,10,25]:
                print("not a valid coin amount")
                continue
            amount_owed -= amount_submitted
                
        except:
            continue
        
    

main()

