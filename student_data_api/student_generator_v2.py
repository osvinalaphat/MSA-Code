from Student import Student
import datetime


"""
Want a function to write an error message to a log file
Input: (string) error message
Output: None
"""
def write_to_error_log(message: str) -> None:
    #open the log file in append mode
    #write error message to the file in the format 
    #Date: message -> 6/24/2025: Error in datafile on line 5
    #close file
    datetime_today = datetime.datetime.now()
    date = f"{datetime_today.month}/{datetime_today.day}/{datetime_today.year}"
    with open("student_error_log.txt","a") as file:
        file.write(f"{date}. Error: {message}\n")
    
    
'''Function to return a list of student objects
Input: none
Output: list of student objects
'''


def load_students() -> list[Student]:
    student_file = open("student_info.csv","r")
    line_number = 0
    student_list = []
    for line in student_file:
        line_number += 1

        student_info_list = line.split(",")
        
        if len(student_info_list) != 6:
            error_message = f"You don't have all the required information at line {line_number}"
            write_to_error_log(error_message)
            continue
        
        try:
            credit_hours = int(student_info_list[3])
            gpa = float(student_info_list[4])
        except:
            message = f"gpa or credit hours aren't numbers at {line_number}"
            write_to_error_log(message)
        try:
            if gpa <0  or gpa >4.0:
                error_message = f"GPA is incorrect at line {line_number}"
                write_to_error_log(error_message)
                continue
            if credit_hours <0:
                error_message = f"Credit hours can't be negative at line {line_number}"
                write_to_error_log(error_message)
                continue
            kiddo = Student(student_info_list[0],student_info_list[1],student_info_list[2],credit_hours,gpa,student_info_list[5])
            student_list.append(kiddo)
        except:
            error_message = f"Missing information at line {line_number}"
            write_to_error_log(error_message)
            continue
    return student_list
'''
Function to convert student objects to student dictionaries
Input: list of student objects
Output: List of student dictionaries

'''
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    #create a list to store the dictionaries in
    student_dictionary_list = []
    #loop through the student list and write each student's data to a dictionary
    for student in list_of_students:
        #create an empty dictionary
        student_dictionary = {}
        #set the keys and values for the dictionary
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_ID()
        
        #append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    return student_dictionary_list


        #create an empty dictionary
        #set the keys and values to 

    #loop through the student list and write each student's data to a dictionary
    #append the dictionary to the list of dictionaries


'''
Function to get a student dictionaries
Input: None
Output: List of student dictionaries
'''
def get_student_dictionary():
    student_list = load_students()
    # get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)


    return student_dictionaries 


