#this file will demonstrate how for loops work

def main():
    #print integers between 0 and 10
    print("Output numbers between 0 and 10")
    for number in range(11):
        print(number)

    print("Output numbers between 0 and 10")
    for number in range(5,11):
        print(number)

    print("\n\nOutput even numbers between 0 and 10")
    for number in range(0,11,2):
        print(number)

    #print odd numbers between 0 and 10
    print("\n\nOutput odd numbers betwwen 0 and 10")
    for number in range(1,11,2):
        print(number)


   #prompt a user for the start and stop values
   # and print the numbers between start and stop

    #get the start value from the user
    start = int(input("Enter start value:"))
    stop = int(input("Enter stop value:"))
    print(f"\nOutput numbers from {start} to {stop}")
    for number in range(start,stop+1):
        print(number)


    #nested for loops
    #use nested for loops to print multiplication tables from user input
    #user will provide start and stop values
    start = int(input("Enter start value:"))
    stop = int(input("Enter stop value:"))
    print(f"\Print multiplication tables from {start} to {stop}")
    for table in range(start,stop+1):
        print(f"\nDisplaying the {table} multiplication table")
        for multiple in range(1,13):
            product = table*multiple
            print(f"{table} x {multiple} = {product}")
    
main()