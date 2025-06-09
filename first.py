# print hello world
print("Hello world!")

#create a variable to store my name
first_name = "Osvin"

#print "my name is Osvin" 
print("My name is",first_name)

#create a variable to store my last name
last_name = "Alaphat"

#write a statement to display "my full name is first_name last_name"
print("My full name is",first_name,last_name,sep="---")

#create variables to store your age, height, and weight and assign them values
age = 16
height = 67
weight = 120.1

#print a sentence with age, weight, and height
print(f"My name is {first_name} {last_name} \nI am {age} years old and I weigh {weight} lbs")

#get and print the data type for age, weight, and height
print(type(age))
print(type(weight))
print(type(height))

#write 3 print statements using string interpolation (fstring) to print
#descriptive sentences for the data types
#variable age is an int

print(f"variable age is a {type(age)}")
print(f"variable weight is a {type(weight)}")
print(f"variable height is a {type(height)}")

number_1 = 5
number_2 = 7
total = number_1 + number_2
print(f"total: {total}")

number_1 = "5"
number_2 = "7"
total = number_1 + number_2
print(f"total: {total}")