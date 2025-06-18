#-> dict means this function will return a dictionary
def get_menu_dictionary(file_name:str) -> dict:
    '''
    function to load menu item and price into a dictionary
    Input: (string)file_path
    Output: (dictionary)menu
    '''
    data_file = open(file_name, "r")
    menu_dict = {}
    for line_of_data in data_file:
        # split the data at the comma
        item_name_and_price = line_of_data.split(",")
        # get the menu item and price from the list
        item_name = item_name_and_price[0]
        item_price= float(item_name_and_price[1])

        # create an entry in the dictionary for the item and price 
        menu_dict[item_name] = item_price
    data_file.close()
    return menu_dict

def order_items(menu_dict)-> float:
    #open file to make dictionary
    # prompt user
    #check if that is an item in the dictionary
    #if it is then add that to the total price
    #if it is end then show the total price
    # else continue
    total = 0
    while True:
        order = input("Enter order:")
        if order.upper() == "END":
            return total
        for item,price in menu_dict.items():
            if order.upper() == item.upper():
                total += price
                print(f"Total: ${total:.2f}")
            else:
                pass

            


def main():
    while True:
        menu_items = get_menu_dictionary("file.txt")
        total_price = order_items(menu_items)    
        
        print(f"\nTotal: ${total_price}")
        
        again = input("Would you like to place another order (y or n):")
        if again.lower() == "y":
            continue
        else:
            print("Have a nice day!")
            break



main()