def main():
    #the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice","Bob","Jerry", "Jane", "Bill"]

    #print the students name and score together
    for index in range(len(scores)):
        print(f"{students[index]}: {scores[index]}")

    #create a dictionary of names and scores
    student_scores = {
        "Alice": 55,
        "Bob" : 75,
        "Jerry" : 87,
        "Jane": 82,
        "Bill": 91
    }

    #print Bob and Jane's scores
    print(student_scores["Bob"])
    print(student_scores["Alice"])

    #print all students data in the student scores dictionary
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

    #Create a car dictionary to store, make, model, year, value, engine size
    car_1 = {"make": "Ferrari", "model":"F-50", "year":2021, "value": 50000, "engine":4.8}

    #get all my car information
    print("\nGet the car information")

    for characteristic, characteristic_value in car_1.items():
        print(f"{characteristic} : {characteristic_value}")

    car_2 = {"make":"Honda","model":"Accord","year":2015,"value":15000}

    #create a list of dictionaries
    dictionary_list = [car_1,car_2]

    print("\nDisplay all cars information")
    for car in dictionary_list:
        print("\nCar information:")
        for feature,value in car.items():
            print(f"{feature} : {value}")
        #print(car)

    #create a dictionary of dictionaries
    car_dictionary = {"Ferrari": car_1, "Honda":car_2}

    # write a for loop to display the car informations
    # Ferrari
    # Print all the ferrari info
    # Honda
    # Print all the honda car info 

    for make,car in car_dictionary.items():
        print(f"\nCar Information: {make}")
        for car_info in car:
            print(f"{car_info} : {car[car_info]}")
main()