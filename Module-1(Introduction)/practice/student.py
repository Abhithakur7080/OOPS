"""
Student Class Demo (Object-Oriented Programming)

This script demonstrates a simple OOP example in Python.

Concepts shown:
- Class and Object
- Attributes
- Methods
- Setting and displaying object data
"""

class Student:
    def __init__(self):
        self.name = None        # public attribute
        self.rollNumber = None  # public attribute

    # Method to set student details
    def setDetails(self, name: str, rollNumber: int) -> None:
        self.name = name
        self.rollNumber = rollNumber

    # Method to display student details
    def displayDetails(self) -> None:
        print("Name : " + self.name)
        print("Roll Number : " + str(self.rollNumber))


# Driver code
if __name__ == "__main__":
    name = input("Enter student name: ")
    rollNumber = int(input("Enter roll number: "))

    student = Student()
    student.setDetails(name, rollNumber)
    student.displayDetails()
