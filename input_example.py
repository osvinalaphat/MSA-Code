#write a pounds to kilograms converter program 
#a user will be prompted for their weight in pounds and the program will output weight in kilograms

# GET INPUT WEIGHT FROM THE USER
# convert weight to a float
#validate that weight is a number.
# if weight is not a number reprompt the user until the input is correct 
def get_positive_float_input():
    while True:
        try:
            user_weight = float(input("Enter your weight in pounds: "))
            #VALIDATE if user weight is positive. If not positive reprompt the user.
            if user_weight <0:
                print("ERROR: Enter a value greater than 0")
                continue
            break
        except:
            print("ERROR: please enter a number")
    return user_weight


def main():
    # get the weight from the user. call the get_positive_float_input_function
    user_weight = get_positive_float_input()
    
    # PROCESSING
    # USE a conversion to convert pounds to kilos: 2.205 lbs = 1 kg
    LBS_TO_KG_CONVERSION = 2.205 
    user_weight_in_kg = user_weight / LBS_TO_KG_CONVERSION

    # OUTPUT
    # print the output to the user in a nice format to 2 decimal places 

    print(f"You weigh {user_weight_in_kg:.2F} kgs")


main()