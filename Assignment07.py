# ------------------------------------------------------------------------------------------ #
# Title: Assignment07
# Desc: This assignment demonstrates using data classes
# with structured error handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   Yuying Xie,6/2/2025,Edited code
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables
students: list = []  # a table of student data
menu_choice: str = ""

# Create a Person Class
class Person:
    """
    A collection for personal information process

    ChangeLog: (Who, When, What)
    Yuying Xie, 6/2/2025, Created class
    """
# Add first_name and last_name properties to the constructor
    def __init__(self, first_name:str = "", last_name:str = ""):
        self.first_name = first_name
        self.last_name = last_name
# Create a getter and setter for the first_name property
    @property
    def first_name(self):
        return self.__first_name.title()
    @first_name.setter
    def first_name(self, value):
        if value.isalpha() or value == "":  # is character or empty string
            self.__first_name = value
        else:
            raise ValueError("The first name should not contain numbers.")
# Create a getter and setter for the last_name property
    @property
    def last_name(self):
        return self.__last_name.title()
    @last_name.setter
    def last_name(self, value):
        if value.isalpha() or value == "":  # is character or empty string
            self.__last_name = value
        else:
            raise ValueError("The last name should not contain numbers.")
# Override the __str__() method to return Person data
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    
# Create a Student class the inherits from the Person class
class Student(Person):
    """
    A collection for personal information process

    ChangeLog: (Who, When, What)
    Yuying Xie, 6/2/2025, Created class
    """
# call to the Person constructor and pass it the first_name and last_name data
    def __init__(self, first_name:str = "", last_name: str="", course_name:str = ""):
        super().__init__(first_name, last_name)
        self.__course_name = course_name
# add a assignment to the course_name property using the course_name parameter
# add the getter for course_name
    @property
    def course_name(self):
        return self.__course_name.title()

# add the setter for course_name
    @course_name.setter
    def course_name(self, value):
        self.__course_name = value
# Override the __str__() method to return the Student data
    def __str__(self):
        return f'{self.first_name} {self.last_name} is registered for {self.course_name}'

    def to_comma_sep(self):
        return f"{self.first_name},{self.last_name},{self.course_name}"

# Processing --------------------------------------- #
class FileProcessor:
    """
    A collection of functions that read and write json file

    ChangeLog: (Who, When, What)
    Yuying Xie, 6/3/2025, Created class
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """ This function reads data from a json file and loads it into a list of dictionary rows
        then returns the list filled with student data.

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created class

        :param file_name: string data with name of file to read from

        :return: list - student_objects
        """

        try:
            # Get a list of dictionary rows from the data file
            file = open(file_name, "r")
            json_students = json.load(file)

            # Convert the list of dictionary rows into a list of Student objects
            student_objects = []
            # replace this line of code to convert dictionary data to Student data
            for student in json_students:
                student_obj = Student(
                    first_name = student["FirstName"],
                    last_name = student["LastName"],
                    course_name =student["CourseName"])
                student_objects.append(student_obj)

            file.close()

        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with reading the file.", error=e)

        finally:
            if file.closed == False:
                file.close()

        return student_objects

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """ This function writes data to a json file with data from a list of dictionary rows

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/3/2025, Created class

        :param file_name: string data with name of file to write to
        :param student_data: list of dictionary rows to be writen to the file

        :return: None
        """

        try:
            # Add code to convert Student objects into dictionaries 
            list_of_dictionary_data:list = []
            for student in student_data:
                student_json:dict = {
                    "FirstName": student.first_name,
                    "LastName": student.last_name,
                    "CourseName": student.course_name}
                list_of_dictionary_data.append(student_json)

            file = open(file_name, "w")
            json.dump(list_of_dictionary_data, file, indent=4)
            file.close()
            print("The following data was saved to file!")
            IO.output_student_and_course_names(student_data=student_data)
        except Exception as e:
            message = "Error: There was a problem with writing to the file.\n"
            message += "Please check that the file is not open by another program."
            IO.output_error_messages(message=message,error=e)
        finally:
            if file.closed == False:
                file.close()


# Presentation --------------------------------------- #
class IO:
    """
    A collection of presentation layer functions that manage user input and output

    ChangeLog: (Who, When, What)
    Yuying Xie, 6/3/2025, Created class
    """

    @staticmethod
    def output_error_messages(message: str, error: Exception = None):
        """ This function displays the a custom error messages to the user

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created function

        :param message: string with message data to display
        :param error: Exception object with technical message to display

        :return: None
        """
        print(message, end="\n\n")
        if error is not None:
            print("-- Technical Error Message -- ")
            print(error, error.__doc__, type(error), sep='\n')

    @staticmethod
    def output_menu(menu: str):
        """ This function displays the menu of choices to the user

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created function


        :return: None
        """
        print()  # Adding extra space to make it look nicer.
        print(menu)
        print()  # Adding extra space to make it look nicer.

    @staticmethod
    def input_menu_choice():
        """ This function gets a menu choice from the user

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created function

        :return: string with the users choice
        """
        choice = "0"
        try:
            choice = input("Enter your menu choice number: ")
            if choice not in ("1","2","3","4"):  # Note these are strings
                raise Exception("Please, choose only 1, 2, 3, or 4")
        except Exception as e:
            IO.output_error_messages(e.__str__())  # Not passing e to avoid the technical message

        return choice

    @staticmethod
    def output_student_and_course_names(student_data: list):
        """ This function displays the student and course names to the user

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created Function

        :param student_data: list of dictionary rows to be displayed

        :return: None
        """

        print("-" * 50)
        for student in student_data:

            # Add code to access Student object data instead of dictionary data
            print(student.to_comma_sep())

        print("-" * 50)

    @staticmethod
    def input_student_data(student_data: list):
        """ This function gets the student's first name and last name, with a course name from the user

        ChangeLog: (Who, When, What)
        Yuying Xie, 6/2/2025, Created Function

        :param student_data: list of dictionary rows to be filled with input data

        :return: list
        """

        try:
            # Replace this code to use a Student objects instead of a dictionary objects
            # student_first_name = input("Enter the student's first name: ")
            # if not student_first_name.isalpha():
            #     raise ValueError("The last name should not contain numbers.")
            # student_last_name = input("Enter the student's last name: ")
            # if not student_last_name.isalpha():
            #     raise ValueError("The last name should not contain numbers.")
            # course_name = input("Please enter the name of the course: ")
            
            # student = ["FirstName": student_first_name,
            #            "LastName": student_last_name,
            #            "CourseName": course_name]

            # student_data.append(student)
            
            first_name = input("What is the student's first name? ")
            last_name = input("What is the student's last name? ")
            course_name = input("What is the name of the course? ")
            student=Student(first_name, last_name, course_name)
            student_data.append(student)
            print()
            print(student.__str__())
        except ValueError as e:
            IO.output_error_messages(message="One of the values was the correct type of data!", error=e)
        except Exception as e:
            IO.output_error_messages(message="Error: There was a problem with your entered data.", error=e)
        return student_data


# Start of main body

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
students = FileProcessor.read_data_from_file(file_name=FILE_NAME)

# Present and Process the data
while (True):

    # Present the menu of choices
    IO.output_menu(menu=MENU)

    menu_choice = IO.input_menu_choice()

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        students = IO.input_student_data(student_data=students)
        continue

    # Present the current data
    elif menu_choice == "2":
        IO.output_student_and_course_names(students)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        FileProcessor.write_data_to_file(file_name=FILE_NAME, student_data=students)
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")

print("Program Ended")
