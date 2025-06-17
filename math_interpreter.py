def main():
    #while true
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

        # if operator not in [+.-.*,/]
        # output some error message
        # reprompt the user
                                #continue
        # Determine the operation to carry out based on the value of the operator
        # Use if/elif/else block to check what operator and carry out the code
        #output the answer
        if y == "+":
            answer = x + z
        elif y == "-":
            answer = x - z
        elif y == "*":
            answer = x * z
        else:
            if z == 0:
                print(f"{x} / {z} = undefined")
                continue
            answer = x / z
        print(f"{x} {y} {z} = {answer}")
        break



    # equation = input("Enter an equation (+,-,*,/): ")
    #6 + 9
    # ["6", "+", "9"]
    pass

main()
