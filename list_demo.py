#this file will demonstrate lists in python
def main():
    #name1= "John"
    #name2= "Mary"

    #create a list of names
    names = ["John","Mary","Alice","Bob"]
    list_of_integers = [10,16,24,42,14,9]
    random_datatype_list = ["Cyd",15,22.3,"Frank"]

    print(names)
    #add an item to the names list
    names.append("Jane")
    list_of_integers.append(5)
    list_of_integers.append(32)
    print(names)

    #get the number of items in a list
    print(f"\nNumber of items in the name list")
    number_of_items = len(names)
    print(f"Number of items in names list: {number_of_items}")

    #get the values from our list
    #get the first value from the list of integers
    print(f"First item in integers list: {list_of_integers[0]}")

    #get the fourth value from the list of integers
    print(f"\nFourth item in integer list: {list_of_integers[3]}")

    print("\nInteger list items")
    for item in list_of_integers:
        print(item)
    #get the number of items in the integer list
    number_of_integer_items = len(list_of_integers)
    for index in range(number_of_integer_items):
        print(f"Item {index}: {list_of_integers[index]}")
main()