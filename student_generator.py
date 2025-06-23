from Student import Student

def main():
    student_file = open("student_info.txt","r")

    for line in student_file:
        student_info_list = line.split(",")
        try:
            kiddo = Student(student_info_list[0],student_info_list[1],student_info_list[2],int(student_info_list[3]),float(student_info_list[4]),student_info_list[5])
            kiddo.print_data()
            if student_info_list[4] <0  or student_info_list[4] >4.0:
                continue
            if student_info_list[3] <0:
                continue
        except:
            continue

main()