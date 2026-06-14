# ══════════════════════════════════════════════════════════
#   static_keyword.py  —  Static Keyword Practice in Python
#   Topics covered (from 3.static_keyword.md):
#     1. Class (Static) Variables
#     2. Module-level Static Variables
#     3. Static Methods  (@staticmethod)
#     4. Static Block Equivalent (class-body execution)
#     5. Interaction Between Static and Instance Members
# ══════════════════════════════════════════════════════════


# ──────────────────────────────────────────────────────────
# MODULE-LEVEL "STATIC" VARIABLE
# Loaded once per process — acts like a global static constant
# ──────────────────────────────────────────────────────────

APP_VERSION = "1.0.0"          # module-level constant (static-like)
MAX_STUDENTS = 100             # shared configuration


# ──────────────────────────────────────────────────────────
# 1. Class (Static) Variable — Object Counter
#    count is shared among ALL instances, just like Java's
#    static int count.
# ──────────────────────────────────────────────────────────

class Student:
    # Class variable — shared by every Student object
    total_students = 0
    school_name = "Greenwood High"

    def __init__(self, name, roll_no):
        self.name = name               # instance variable
        self.roll_no = roll_no         # instance variable
        Student.total_students += 1    # update shared counter

    def display(self):
        print(f"  Name: {self.name}  |  Roll: {self.roll_no}  |  School: {Student.school_name}")

    @staticmethod
    def get_total():
        """Static method — returns the shared student count."""
        return Student.total_students


# ──────────────────────────────────────────────────────────
# 2. Static Method as a Utility  (@staticmethod)
#    MathUtils groups helper functions — no object needed.
# ──────────────────────────────────────────────────────────

class MathUtils:
    PI = 3.14159          # class (static) constant

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def circle_area(radius):
        return MathUtils.PI * radius * radius   # uses class variable inside static method

    @staticmethod
    def is_even(n):
        return n % 2 == 0


# ──────────────────────────────────────────────────────────
# 3. Static Block Equivalent — One-time Initialization
#    The class body executes ONCE when the class is defined.
#    This mirrors Java's static { } block.
# ──────────────────────────────────────────────────────────

class DatabaseConfig:
    # ↓ this code runs ONCE at class definition time
    print("  [DatabaseConfig] Loading configuration... (runs once at definition)")

    HOST = "localhost"
    PORT = 5432
    DB_NAME = "school_db"

    @staticmethod
    def get_connection_string():
        return f"postgresql://{DatabaseConfig.HOST}:{DatabaseConfig.PORT}/{DatabaseConfig.DB_NAME}"


# ──────────────────────────────────────────────────────────
# 4. Class Variable vs Instance Variable
#    Demonstrates how class variables are SHARED but instance
#    variables are SEPARATE for every object.
# ──────────────────────────────────────────────────────────

class BankAccount:
    bank_name = "National Bank"    # class variable — shared
    interest_rate = 5.0            # class variable — shared

    def __init__(self, owner, balance):
        self.owner = owner          # instance variable — unique per object
        self.balance = balance      # instance variable — unique per object

    def apply_interest(self):
        self.balance += self.balance * (BankAccount.interest_rate / 100)

    def display(self):
        print(f"  Owner: {self.owner}  |  Balance: Rs.{self.balance:.2f}  |  Bank: {BankAccount.bank_name}")

    @staticmethod
    def update_interest_rate(new_rate):
        """Changing this affects ALL accounts — class variable."""
        BankAccount.interest_rate = new_rate
        print(f"  Interest rate updated to {new_rate}% for all accounts.")


# ──────────────────────────────────────────────────────────
# 5. Interaction Between Static and Instance Members
#    A static method cannot directly use self/instance data.
#    It can work with instance data by accepting an object
#    as a parameter, or by creating one internally.
# ──────────────────────────────────────────────────────────

class Employee:
    company = "TechCorp"      # class (static) variable

    def __init__(self, name, salary):
        self.name = name           # instance variable
        self.salary = salary       # instance variable

    @staticmethod
    def company_info():
        """Can access class variable via class name, not self."""
        print(f"  Company: {Employee.company}")

    @staticmethod
    def compare_salary(emp1, emp2):
        """Static method that accepts instances as parameters."""
        if emp1.salary > emp2.salary:
            print(f"  {emp1.name} earns more (Rs.{emp1.salary})")
        elif emp2.salary > emp1.salary:
            print(f"  {emp2.name} earns more (Rs.{emp2.salary})")
        else:
            print("  Both earn equally.")

    def display(self):
        print(f"  Employee: {self.name}  |  Salary: Rs.{self.salary}  |  Company: {Employee.company}")


# ══════════════════════════════════════════════════════════
#   MAIN — Run all practice examples
# ══════════════════════════════════════════════════════════

if __name__ == "__main__":

    # ── Module-level static variable ──────────────────────
    print("=" * 50)
    print("  Module-level Static Variables")
    print("=" * 50)
    print(f"  App Version : {APP_VERSION}")
    print(f"  Max Students: {MAX_STUDENTS}")

    # ── 1. Class Variable — Student Counter ───────────────
    print()
    print("=" * 50)
    print("  1. Class Variable — Student Counter")
    print("=" * 50)
    s1 = Student("Aarav", 101)
    s2 = Student("Priya", 102)
    s3 = Student("Rohit", 103)

    s1.display()
    s2.display()
    s3.display()

    # All objects share the same total_students
    print(f"\n  Total students (via class)  : {Student.total_students}")
    print(f"  Total students (via method) : {Student.get_total()}")
    print(f"  Total students (via object) : {s1.total_students}")   # still shared value

    # ── 2. Static Method as Utility ───────────────────────
    print()
    print("=" * 50)
    print("  2. Static Method — MathUtils")
    print("=" * 50)
    # Called directly on class — no object needed
    print(f"  add(7, 3)           = {MathUtils.add(7, 3)}")
    print(f"  multiply(4, 5)      = {MathUtils.multiply(4, 5)}")
    print(f"  circle_area(r=7)    = {MathUtils.circle_area(7):.4f}")
    print(f"  is_even(42)         = {MathUtils.is_even(42)}")
    print(f"  is_even(17)         = {MathUtils.is_even(17)}")

    # ── 3. Static Block Equivalent ────────────────────────
    print()
    print("=" * 50)
    print("  3. Static Block Equivalent — DatabaseConfig")
    print("=" * 50)
    # Note: the class-body print already ran at definition time (above)
    conn = DatabaseConfig.get_connection_string()
    print(f"  Connection String: {conn}")

    # ── 4. Class Variable vs Instance Variable ────────────
    print()
    print("=" * 50)
    print("  4. Class Variable vs Instance Variable — BankAccount")
    print("=" * 50)
    acc1 = BankAccount("Aarav", 10000)
    acc2 = BankAccount("Priya", 25000)

    print("  Before interest:")
    acc1.display()
    acc2.display()

    acc1.apply_interest()
    acc2.apply_interest()
    print("\n  After 5% interest:")
    acc1.display()
    acc2.display()

    # Change class variable — affects ALL accounts
    print()
    BankAccount.update_interest_rate(7.5)
    acc1.apply_interest()
    acc2.apply_interest()
    print("  After 7.5% interest (rate changed for all):")
    acc1.display()
    acc2.display()

    # ── 5. Interaction — Static vs Instance ───────────────
    print()
    print("=" * 50)
    print("  5. Static & Instance Interaction — Employee")
    print("=" * 50)
    e1 = Employee("Anil", 55000)
    e2 = Employee("Sunita", 72000)

    e1.display()
    e2.display()

    print()
    Employee.company_info()                   # static method via class
    Employee.compare_salary(e1, e2)           # static method with instance args
