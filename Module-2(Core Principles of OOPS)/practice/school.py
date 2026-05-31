
class School:
    def __init__(self):
        self.__schoolName = 'DPS'
    def printSchoolName(self):
        print("School name:", self.__schoolName)

class Student(School):
    def __init__(self, name):
        super().__init__()
        self.__studentName = name
    def printStudentName(self):
        print("Student name:", self.__studentName)

# Main function to execute the program
def main():
    # Create a new student object with the name "Raj"
    student = Student("Raj")

    # Print the student's name
    student.printStudentName()

    # Print the school's name
    student.printSchoolName()


# Execute main function
if __name__ == "__main__":
    main()