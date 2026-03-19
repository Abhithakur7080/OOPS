"""
Rectangle Class Demo (Object-Oriented Programming)

This script demonstrates a simple OOP example in Python.

Concepts shown:
- Class and Object
- Constructors (Default and Parameterized)
- Attributes
- Methods
- Calculating and displaying rectangle area
"""

class Rectangle:
    def __init__(self, length: float = 1.00, width: float = 1.00):
        if length < 0 or width < 0:
            raise ValueError("Length or Width cannot be negative")

        self.length = length
        self.width = width
        self.area = None

    # Method to calculate area
    def calculateArea(self) -> None:
        self.area = self.length * self.width

    # Method to display rectangle details
    def displayDetails(self) -> None:
        if self.area is None:
            self.calculateArea()

        print(f"Length : {self.length:.2f}")
        print(f"Width : {self.width:.2f}")
        print(f"Area : {self.area:.2f}")


# Driver code
if __name__ == "__main__":
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))

    print("\nRectangle using Default Constructor")
    r1 = Rectangle()
    r1.calculateArea()
    r1.displayDetails()

    print("\nRectangle using Parameterized Constructor")
    r2 = Rectangle(length, width)
    r2.calculateArea()
    r2.displayDetails()