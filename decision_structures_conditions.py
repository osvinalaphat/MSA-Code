#This file demonstrates decision structures and conditions
def main():
    a = 1451495700
    b = 1231231234

    #exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater than A: {a < b}")
    print(f"A is equal to B: {a == b}")

    #copmarison operators: less than <, greater than >, <= less than or equal to, >= greater than or equal to
    #equal to: ==

    #create a decision structure to determine if a and b are equal
    if a>b:
        print(f"{a} is greater than {b}")
    elif a<b:
        print(f"{b} is greater than {a}")
    else:
        print(f"{a} is equal to {b}")

    #create a decision structure to print a letter grade
    # based on a test score
    #A 100 - 90, B: 89-80, C: 79-70, D:69-60, F: less than 60
    print("Grade Decision: 1")
    test_score = 78
    #           A                   B
    if(test_score <0 or test_score >100):
        print("Score needs to be between 0 and 100...")
    else:
        if (test_score>=90):
            print(f"{test_score} --> A")
        elif(test_score >= 80):
            print(f"{test_score} --> B")
        elif(test_score >= 70):
            print(f"{test_score} --> C")
        elif(test_score >= 60):
            print(f"{test_score} --> D")
        else:
            print(f"{test_score} --> F")
    # Create a decision structure to determine the season: winter, spring, summer, or fall.
    # Ask the user to enter the number of the month and based on the number, determine the season
    # Winter: 12, 1, 2; Spring: 3, 4, 5; Summer: 6, 7, 8; Fall: 9, 10, 11;
    # Output/print the season: It is season

    current_month = int(input("Enter the month number: "))
    if (current_month<0 or current_month >12):
        print("THAT is not a month of the year")
    elif (current_month <= 2 or current_month == 12):
        print("It is Winter season")
    elif (current_month <=5):
        print("It is Spring season")
    elif (current_month <=9):
        print("It is Summer season")
    elif (current_month <=12):
        print("It is Fall season")
        

main()