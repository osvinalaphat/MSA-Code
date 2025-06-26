class Student():


    def __init__(self,fName:str,lName:str,major:str,credit_hours:int,gpa:float,ID):
        self.__fName = fName
        self.__lName = lName
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__ID = ID.strip()

    def set_first_name(self,fName:str):
        self.__fName = fName

    def set_last_name(self,lName:str):
        self.__lName = lName

    def set_major(self,major:str):
        self.__major = major
    
    def set_credit_hours(self,credit_hours:int):
        self.__credit_hours = credit_hours
    
    def set_gpa(self,gpa:float):
        self.__gpa = gpa
    
    
    
    def get_first_name(self):
        return self.__fName 

    def get_last_name(self):
        return self.__lName 

    def get_major(self):
        return self.__major
    
    def get_credit_hours(self):
        return self.__credit_hours 
    
    def get_gpa(self):
        return self.__gpa 

    def get_ID(self):
        return self.__ID

    def get_class_level(self):

        if int(self.get_credit_hours()) <= 30:
            return "Freshman"
        elif int(self.get_credit_hours()) <= 60:
            return "Sophomore"
        elif int(self.get_credit_hours()) <= 90:
            return "Junior"
        else:
            return "Senior"
    def print_data(self):
        print(f"-----------")
        print(f"{self.get_first_name()} {self.get_last_name()}")
        print(f"Class Level: {self.get_class_level()}, Major: {self.get_major()}")
        print(f"GPA:{self.get_gpa()}, ID:{self.get_ID()}")






#create classes