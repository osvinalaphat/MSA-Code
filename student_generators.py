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
    return
    



def main():
    student_file = open("student_info.txt","r")
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
            kiddo.print_data()
        except:
            error_message = f"Missing information at line {line_number}"
            write_to_error_log(error_message)
            continue
main()

