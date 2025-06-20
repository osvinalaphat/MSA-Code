import random
# frank, mike, Brain S ###J-WALKERS

#basic idea:
    # ask difficult : 1, 2, 3
        #validate
    # ask number of questions: 3-10
        # validate
        # store it in a variable (num_questions)
    # Make questions
        # if difficulty 1 : 0,9; etc
    # ask the question 
    # make a for loop for amount of questions
    # make a for Loop for amount of tries
    # if answer = correct, say correct, add one to correct_amount, and move on
    # if the answer is not correct
        # add 1 to amount of tries and if tries ever equals 3 print the answer and break
    # at the end, report the correct percentage with correct_amount / num_questions        

def main():

    
    #create a random number generator
    random_generator = random.Random()
    
    
    level_difficulty, num_questions = get_questions_info()

    num_correct = equation_prompter(level_difficulty, num_questions, random_generator)
    percent = 100 * num_correct/num_questions
    print(f"\nYou got {num_correct} out of {num_questions} correct: {percent:.2f}%")


def get_questions_info():
    while True:
        try:
            level_difficulty = int(input("Enter question difficulty: "))
            if level_difficulty not in [1,2,3]:
                continue 
            num_questions = int(input("Enter number of questions (3-10): "))
            if num_questions <3 or num_questions > 10:
                print("Needs to be between 3 - 10 questions")
                continue
            break  
        except:
            print("ERROR: Please enter a number.\n")
            continue
    return level_difficulty, num_questions


def equation_prompter(level_diff: int, num_questions: int, random_generator: random):
    num_correct = 0
    for question in range(num_questions):
        if level_diff == 1:
            num1 = random_generator.randint(0,9)
            num2 = random_generator.randint(0,9)
        if level_diff == 2:
            num1 = random_generator.randint(10,99)
            num2 = random_generator.randint(10,99)
        if level_diff == 3:
            num1 = random_generator.randint(100,999)
            num2 = random_generator.randint(100,999)
        for attempt in range (3):
            answer = num1 + num2
            guess = input(f"{num1} + {num2} = ")
            if str(answer) != guess:
                print("Incorrect!\n")
                if attempt == 2:
                    print(f"Correct Answer: {num1} + {num2} = {answer}")
            else:
                print("Correct!\n")
                num_correct += 1
                break
        
    return num_correct




main()