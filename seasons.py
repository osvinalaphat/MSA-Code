def main():
    while True:
        # Call the get_month_number function to prompt and get the month number from the user
        month_number = get_month_number()
        season = get_season_name(month_number)
        # Call the get_season_name function to get the name of the season
        # Print the output
        print(f"The Month number is {month_number}")
        print(f"The season is {season}")
        # ask the user if they want to run the program again
        # if y or Y then rerun the program, otherwise end the program
        again = input("Do you want to go again? (y or n): ")
        if again.upper() == "Y":
            print("\n")
        elif again.upper() == "N":
            break
        else:
            print("You're doing it again.")
            print("\n\n")

def get_month_number():
    #validate the input is 1-12
    #reprompt user if input not valid
    while True:
        try:
            current_month = int(input("Enter the month number: "))
            if (current_month<=0 or current_month >12):
                print("THAT is not a month of the year")
            else:
                return current_month
        except:
            print("That is not a number")
    #function:
    # Input:
    # Output: 
    # note: these green lines are required akash pillai

'''def get_season_name(month_number):
    if (month_number <= 2 or month_number== 12):
        season = "Winter"
    elif (month_number <=5):
        season = "Spring"
    elif (month_number <=9):
        season = "Summer"
    elif (month_number < 12):
        season = "Fall"
    return season'''
    
def get_season_name(month_number):
    if (month_number in [12,1,2]):
        season = "Winter"
    elif (month_number in [3,4,5]):
        season = "Spring"
    elif (month_number in [6,7,8]):
        season = "Summer"
    elif ((month_number in [9,10,11])):
        season = "Fall"
    return season


main()