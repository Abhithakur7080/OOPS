"""
Employee Class Demo (Object-Oriented Programming)

This script demonstrates a simple OOP example in Python.

Concepts shown:
- Class and Object
- Private Attributes (Encapsulation)
- Getter and Setter Methods
- Salary Validation
- Displaying Employee Details
"""

class Employee:
    def __init__(self, name: str, employeeId: int, salary: float) -> None:
        self.name = name
        self._employeeId = employeeId  # protected attribute
        self.__salary = 0.00  # private attribute

        self.setSalary(salary)

    # Method to set salary with validation
    def setSalary(self, newSalary: float) -> None:
        if newSalary < 0:
            print("Invalid salary")
            self.__salary = 0.00
        else:
            self.__salary = newSalary

    # Method to get salary
    def getSalary(self) -> float:
        return self.__salary

    # Method to display employee details
    def displayEmployeeDetails(self) -> None:
        print("Name : " + self.name)
        print("Employee Id : " + str(self._employeeId))
        print("Salary : {:.2f}".format(self.__salary))


# Driver code
if __name__ == "__main__":

    name = input("Enter name: ")
    employeeId = int(input("Enter employee ID: "))
    salary = float(input("Enter initial salary: "))
    newSalary = float(input("Enter new salary: "))

    # Create an Employee object
    employee = Employee(name, employeeId, salary)

    # Get and print the salary
    print("Salary : {:.2f}".format(employee.getSalary()))

    # Update the salary
    employee.setSalary(newSalary)

    # Display employee details
    employee.displayEmployeeDetails()