from Automobile import Automobile

def main():
    #create instances of automobile
    auto1 = Automobile("Honda","Accord","23456",2.2,"Alice",2017,"Blue")
    auto2 = Automobile("Ferrari","F-50","12345",4.8,"Bob",2022,"Black")

    

    #change auto1 color
    auto2.set_color("White")

    auto2.set_owner("Frank Ocean")

    auto_list = []
    auto_list.append(auto1)
    auto_list.append(auto2)

    #create a method to print Automobile data
    print("Automobile Data")
    print("----------------")
    for automobile in auto_list:
        automobile.print_data()
        print(f"The {automobile.get_model()} is {automobile.get_age()} years old")
        print("\n")
        
main()