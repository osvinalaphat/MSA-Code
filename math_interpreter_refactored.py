'''
Function to get valid expression inputs from the user.
Input: None
Outputs:  (int) X, (int) Z, (String) Y
'''

def get_valid_expression_inputs():
    while True:
        # prompt the user for an expression
        equation = input("Enter an equation: ")
        # use the split() method to get the parts of the expression
        # check the length of the list returned from .split()
        # if len(list) not = 3, then output incorrect format message
                                #continue
        equation = equation.split()
        if(not len(equation) == 3):
            print("Incorrect format\n")
            continue
        # try:
        #   get X, Y, and Z values from the list
        #   and check if X and Z are integers by converting to int()
        # except:
        #   output Error message and reprompt
                                #continue
        try:
            x = int(equation[0])
            y = equation[1]
            z = int(equation[2])
        except:
            print("Incorrect format\n")
            continue
        # Check that operator is +,-,*,/
        if y not in ["+","-","*","/"]:
            print("Incorrect operators")
            continue
        return x,y,z

        

'''
Functions to evaluate an expression
Inputs: X(int), Y(string), Z(int)
Outputs: answer
'''

def evaluate_expression(x: int, y: str, z: int):
        if y == "+":
            answer = x + z
        elif y == "-":
            answer = x - z
        elif y == "*":
            answer = x * z
        else:
            if z == 0:
                answer = "undefined"
                return answer
                
            answer = x / z
        return answer


def main():
    #call the get_valid_expression_inputs functino to get x,y,z
    while True:
        x,y,z = get_valid_expression_inputs()
        answer = evaluate_expression(x,y,z)

        print(f"{x} {y} {z} = {answer}")

        again = input("Wanna repeat (y or n): ")
        if again.upper() == "Y":
            continue
        else:
            break
    # Call evaluate_expression to get the answer for the expression
    # print the answer
    # ask the user if they want to evaluate another expression
    # rerun the program if the user wants to continue, otherwise end the program 
main()








