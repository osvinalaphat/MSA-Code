def main():
    my_name = "osvIN"

    last_name = "ALAPHAT"

    intro = "Hi, my name is Osvin"

    #capitalize a string
    print(my_name.capitalize())
    print(my_name.upper())
    print(last_name.lower())
    print(my_name.upper().startswith("O"))

    print(my_name.startswith("O") or my_name.startswith("o"))
    if((not my_name.startswith("Osv")) and (not my_name.startswith("osv"))): 
        print("That aint my name")
    else:
        print(f"You spelled {my_name.lower().capitalize()} correctly")

    print(f"\nUsing endswith() method")
    print(f"{my_name} ends with 'vin': {my_name.lower().endswith("vin")}")

    print(intro.find("x",4,12))
    print(f"{intro[4:16]}")

    search_letter = "s"
    if(my_name.find(search_letter) == -1): 
        print(f"{search_letter.upper()} was not in {my_name.lower().capitalize()}")
    else:
        print(f"{search_letter} was letter number {my_name.find(search_letter)+1}")

    my_name2 = ""
    for letter in my_name:
        print(letter)
        my_name2 = my_name2 +letter.lower()
    print(f"{my_name2.capitalize()} is {len(my_name2)} characters long!")

    #print the letters in a string along with the index position
    for letter_index in range(len(my_name)):
        print(f"{my_name2[letter_index]} is at index {letter_index}")


    print("\n\n")
    sentence = "I have a dog. My dog is cute. Do you want a dog?"
    # write a program that counts the number of occurences of the word dog
    # in the sentence. Expected output: 3.
    # user a while loop
    # start at the beginning of the string
    # search for the first occurence of the word(dog)
    # if we find a dog add 1 to some variable of dogs we found
    # continue searching the string from the next index after the dog we found
    # do this until we don't find any more dogs  
    temp_dog_position = 0
    dog_findings = 0
    while True:
        if(not sentence.find("dog",temp_dog_position+1) == -1):
            temp_dog_position = sentence.find("dog",temp_dog_position+1)
            dog_findings +=1
            print(f"'dog' found at position {temp_dog_position}")
        else:
            break
    print(f"{dog_findings} instances of the word 'dog' were found")

    start_index = 0
    number_of_dogs = 0
    search_word = "dog"
    # use a while loop
    while True:
        
        dog_index = sentence.find(search_word,start_index)
        # if we find a dog add 1 to some variable of dog we found
        # continue searching the string from the next index after tje dpg we find
        # update the start_index to dog_index+1 
        if dog_index == -1:
            break
        else:
            number_of_dogs +=1
            start_index = dog_index + 1
        #dog this until; we dont find any more dogs
    print(f"There are {number_of_dogs} instances of the word dog")


    txt = "Welcome to the Jungle"


    print(txt)

    splitter = txt.split(" ")
    print(splitter)

    #how to use the split method
    print("\nUsing th split() method")
    car_info = "Ferrarim, f-50, 2021,500000,4.8\n"
    car_data = car_info.split(",")
    print(car_data) 
    make = car_data[0]
    model = car_data[1]
    year = int(car_data[2])
    price = float(car_data[3])
    engine_size = float(car_data[4])

    print(f"{year} {make} {model}")
    print(f"Price: ${price} - Engine: {engine_size}")
main()
