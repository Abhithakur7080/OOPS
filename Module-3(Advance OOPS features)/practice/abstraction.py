from abc import ABC, abstractmethod

# ──────────────────────────────────────────────
# ABSTRACTION in Python
#
# Abstraction = hiding internal implementation details
# and showing only the ESSENTIAL features to the user.
#
# In Python we achieve abstraction using:
#   → Abstract Base Classes (ABC)
#   → @abstractmethod decorator
#
# Rules:
#   • A class with ≥1 @abstractmethod is an Abstract Class
#   • You CANNOT instantiate an abstract class directly
#   • Subclass MUST override all abstract methods
# ──────────────────────────────────────────────


# ──────────────────────────────────────────────
# 1. Basic Abstraction — Abstract Class
# ──────────────────────────────────────────────

class Shape(ABC):
    """Abstract class: defines the concept of a Shape."""

    @abstractmethod
    def area(self):
        """Every shape MUST know how to compute its area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Every shape MUST know how to compute its perimeter."""
        pass

    def describe(self):
        """Concrete method — shared by all shapes (not abstract)."""
        print(f"I am a {type(self).__name__} with area={self.area():.2f} "
              f"and perimeter={self.perimeter():.2f}")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


# ──────────────────────────────────────────────
# 2. Partial Abstraction
#    (Abstract class has SOME concrete methods too)
# ──────────────────────────────────────────────

class BankAccount(ABC):
    """
    Abstract class — hides HOW interest is calculated.
    Subclasses reveal their own implementation.
    """

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance          # protected attribute

    # ── Abstract method (MUST be overridden) ──
    @abstractmethod
    def calculate_interest(self):
        pass

    # ── Concrete methods (shared logic) ──
    def deposit(self, amount):
        self._balance += amount
        print(f"[{self.owner}] Deposited Rs.{amount}. Balance = Rs.{self._balance}")

    def withdraw(self, amount):
        if amount > self._balance:
            print("Insufficient funds!")
        else:
            self._balance -= amount
            print(f"[{self.owner}] Withdrew Rs.{amount}. Balance = Rs.{self._balance}")

    def show_balance(self):
        print(f"[{self.owner}] Current Balance = Rs.{self._balance}")


class SavingsAccount(BankAccount):
    INTEREST_RATE = 0.04   # 4%

    def calculate_interest(self):
        interest = self._balance * self.INTEREST_RATE
        print(f"[Savings] Interest = Rs.{interest:.2f}")
        return interest


class CurrentAccount(BankAccount):
    INTEREST_RATE = 0.01   # 1%

    def calculate_interest(self):
        interest = self._balance * self.INTEREST_RATE
        print(f"[Current] Interest = Rs.{interest:.2f}")
        return interest


# ──────────────────────────────────────────────
# 3. Abstract Property
#    (@property + @abstractmethod)
# ──────────────────────────────────────────────

class Employee(ABC):
    """Abstract class using abstract properties."""

    def __init__(self, name):
        self.name = name

    @property
    @abstractmethod
    def role(self):
        """Every employee type MUST define their role."""
        pass

    @property
    @abstractmethod
    def salary(self):
        """Every employee type MUST define their salary."""
        pass

    def display(self):
        print(f"Employee : {self.name}")
        print(f"Role     : {self.role}")
        print(f"Salary   : Rs.{self.salary:,}")


class Manager(Employee):
    @property
    def role(self):
        return "Manager"

    @property
    def salary(self):
        return 120_000


class Developer(Employee):
    @property
    def role(self):
        return "Developer"

    @property
    def salary(self):
        return 95_000


# ──────────────────────────────────────────────
# 4. Template Method Pattern
#    (Abstract class defines the ALGORITHM skeleton;
#     subclasses fill in the steps)
# ──────────────────────────────────────────────

class DataProcessor(ABC):
    """
    Template Method Pattern:
    The `process()` method defines the fixed steps.
    Subclasses only override the variable steps.
    """

    # ── Template method (fixed skeleton — NOT abstract) ──
    def process(self):
        self.read_data()
        self.transform_data()
        self.save_data()

    # ── Abstract steps (subclass fills these in) ──
    @abstractmethod
    def read_data(self):
        pass

    @abstractmethod
    def transform_data(self):
        pass

    # ── Concrete step with default behaviour ──
    def save_data(self):
        print("  → [Default] Saving data to disk...")


class CSVProcessor(DataProcessor):
    def read_data(self):
        print("  → Reading data from CSV file...")

    def transform_data(self):
        print("  → Transforming CSV rows into objects...")


class JSONProcessor(DataProcessor):
    def read_data(self):
        print("  → Fetching data from JSON API...")

    def transform_data(self):
        print("  → Parsing JSON and mapping fields...")

    def save_data(self):                          # overrides default
        print("  → Saving parsed JSON to database...")


# ──────────────────────────────────────────────
# MAIN — Run all examples
# ──────────────────────────────────────────────

if __name__ == "__main__":

    # ── 1. Basic Abstraction ──
    print("=" * 45)
    print(" 1. Basic Abstraction — Shapes")
    print("=" * 45)
    circle = Circle(7)
    rect   = Rectangle(5, 3)
    circle.describe()
    rect.describe()

    # Trying to instantiate abstract class → TypeError
    # s = Shape()   ← would raise: TypeError: Can't instantiate abstract class

    # ── 2. Partial Abstraction ──
    print()
    print("=" * 45)
    print(" 2. Partial Abstraction — Bank Accounts")
    print("=" * 45)
    savings = SavingsAccount("Abhishek", 50_000)
    savings.deposit(10_000)
    savings.withdraw(5_000)
    savings.calculate_interest()
    savings.show_balance()

    print()
    current = CurrentAccount("Riya", 1_00_000)
    current.calculate_interest()

    # ── 3. Abstract Property ──
    print()
    print("=" * 45)
    print(" 3. Abstract Property — Employees")
    print("=" * 45)
    mgr = Manager("Karan")
    dev = Developer("Priya")
    mgr.display()
    print()
    dev.display()

    # ── 4. Template Method Pattern ──
    print()
    print("=" * 45)
    print(" 4. Template Method — Data Processors")
    print("=" * 45)
    print("Processing CSV:")
    csv_proc = CSVProcessor()
    csv_proc.process()

    print()
    print("Processing JSON:")
    json_proc = JSONProcessor()
    json_proc.process()
