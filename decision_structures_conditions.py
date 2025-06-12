#This file demonstrates decision structures and conditions
def main():
    a = 1451495700
    b = 1231231234

    #exploring conditions
    print(f"A is greater than B: {a > b}")
    print(f"B is greater than A: {b > a}")
    print(f"B is greater than A: {b == a}")

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
    test_score = 77
    #           A                   B
    if ((test_score<= 100) and (test_score>=90)):
        print(f"{test_score} --> A")
    elif((test_score<=90) and (test_score >= 80)):
        print(f"{test_score} --> B")
    elif((test_score<=80) and (test_score >= 70)):
        print(f"{test_score} --> C")
    elif((test_score<=70) and (test_score >= 60)):
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

main()