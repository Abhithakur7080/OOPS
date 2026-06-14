# ──────────────────────────────────────────────
# INNER CLASSES (Nested Classes) in Python
#
# An "inner class" is a class defined INSIDE another class.
# Purpose: logically group helper types that only make
#          sense within the context of the outer class.
#
# Unlike Java, Python:
#   - Does NOT enforce strict access control
#   - Does NOT auto-bind inner class to outer instance
#   - Passes outer objects EXPLICITLY if needed
#
# Patterns covered:
#   1. Static Nested Class  (independent of outer instance)
#   2. Non-Static Inner Class  (receives outer instance)
#   3. Local Inner Class  (class inside a method)
#   4. Anonymous Behavior  (lambda / one-time inline class)
# ──────────────────────────────────────────────


# ──────────────────────────────────────────────
# 1. Static Nested Class Equivalent
#    - Nested class is INDEPENDENT of outer instance
#    - Accesses outer CLASS variables explicitly
#    - Like Java's static nested class
# ──────────────────────────────────────────────

class Company:
    company_name = "TechCorp"      # class-level (static) variable
    founded_year = 2010

    class Address:
        """Nested class: logically belongs to Company, but
        does not need a Company instance to exist."""

        def __init__(self, city, country):
            self.city = city
            self.country = country

        def display(self):
            # Access outer class variable explicitly via class name
            print(f"Company : {Company.company_name}")
            print(f"Founded : {Company.founded_year}")
            print(f"Address : {self.city}, {self.country}")


# ──────────────────────────────────────────────
# 2. Non-Static Inner Class Equivalent
#    - Inner class RECEIVES outer instance explicitly
#    - Stores it to access outer instance variables
#    - Like Java's non-static inner class
# ──────────────────────────────────────────────

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    class Transaction:
        """Inner class that needs BankAccount instance data."""

        def __init__(self, outer_account, amount, txn_type):
            # Explicitly store reference to outer instance
            self._account = outer_account
            self.amount = amount
            self.txn_type = txn_type

        def execute(self):
            if self.txn_type == "credit":
                self._account._balance += self.amount
                print(f"[CREDIT] Rs.{self.amount} added  "
                      f"| {self._account.owner}'s Balance: Rs.{self._account._balance}")
            elif self.txn_type == "debit":
                if self.amount > self._account._balance:
                    print("Insufficient funds!")
                else:
                    self._account._balance -= self.amount
                    print(f"[DEBIT]  Rs.{self.amount} removed"
                          f"| {self._account.owner}'s Balance: Rs.{self._account._balance}")

    def show_balance(self):
        print(f"[{self.owner}] Current Balance: Rs.{self._balance}")


# ──────────────────────────────────────────────
# 3. Local Inner Class (class inside a method)
#    - Class is defined INSIDE a method/function
#    - Only exists within that method's scope
#    - Good for small, one-off helper logic
# ──────────────────────────────────────────────

class ReportGenerator:

    def generate_html_report(self, title, rows):
        """Generates a simple HTML table report."""

        # Local class — only lives inside this method
        class HTMLTable:
            def __init__(self, header, data_rows):
                self.header = header
                self.rows = data_rows

            def render(self):
                lines = [f"<h2>{title}</h2>", "<table>"]
                lines.append("  <tr>" +
                             "".join(f"<th>{h}</th>" for h in self.header) +
                             "</tr>")
                for row in self.rows:
                    lines.append("  <tr>" +
                                 "".join(f"<td>{cell}</td>" for cell in row) +
                                 "</tr>")
                lines.append("</table>")
                return "\n".join(lines)

        # Create and use the local class immediately
        table = HTMLTable(header=["Name", "Score", "Grade"], data_rows=rows)
        return table.render()

    def generate_text_report(self, items):
        """Generates a plain text bullet report."""

        # Another local class — different helper, same method scope pattern
        class BulletList:
            def __init__(self, data):
                self.data = data

            def render(self):
                return "\n".join(f"  - {item}" for item in self.data)

        bullet = BulletList(items)
        return bullet.render()


# ──────────────────────────────────────────────
# 4. Anonymous Inner Class Equivalent
#    Python uses:
#      a) Lambda    → one-liner, no state
#      b) Inline small class → when multiple methods/state needed
# ──────────────────────────────────────────────

def get_sorter(reverse=False):
    """
    Returns a sorter object that behaves differently
    based on the `reverse` flag.
    This mimics a Java anonymous class returning custom behavior.
    """

    # Inline small class — anonymous-style, created and returned directly
    class Sorter:
        def __init__(self, desc):
            self._desc = desc

        def sort(self, items):
            return sorted(items, reverse=self._desc)

        def describe(self):
            order = "descending" if self._desc else "ascending"
            print(f"Sorting in {order} order.")

    return Sorter(desc=reverse)


# ──────────────────────────────────────────────
# BONUS: Real-World Pattern — Nested Config Class
#        (common in Django, dataclasses, ORMs)
# ──────────────────────────────────────────────

class Product:
    """
    Outer class represents a Product.
    Inner Meta class holds configuration/metadata —
    a pattern used heavily in Django models.
    """

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    class Meta:
        """Configuration/metadata for the Product class."""
        db_table = "products"
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def display(self):
        print(f"Product  : {self.name}")
        print(f"Price    : Rs.{self.price:,}")
        print(f"Category : {self.category}")
        print(f"DB Table : {Product.Meta.db_table}")


# ──────────────────────────────────────────────
# MAIN — Run all examples
# ──────────────────────────────────────────────

if __name__ == "__main__":

    # ── 1. Static Nested Class ──
    print("=" * 48)
    print(" 1. Static Nested Class — Company.Address")
    print("=" * 48)
    # Create nested object WITHOUT needing an outer instance
    addr = Company.Address("Bangalore", "India")
    addr.display()

    # ── 2. Non-Static Inner Class ──
    print()
    print("=" * 48)
    print(" 2. Non-Static Inner Class — BankAccount.Transaction")
    print("=" * 48)
    account = BankAccount("Abhishek", 50_000)
    account.show_balance()

    # Pass outer object explicitly to inner class
    t1 = BankAccount.Transaction(account, 10_000, "credit")
    t1.execute()

    t2 = BankAccount.Transaction(account, 25_000, "debit")
    t2.execute()

    t3 = BankAccount.Transaction(account, 99_000, "debit")  # should fail
    t3.execute()

    # ── 3. Local Inner Class ──
    print()
    print("=" * 48)
    print(" 3. Local Inner Class — ReportGenerator")
    print("=" * 48)
    gen = ReportGenerator()
    html = gen.generate_html_report(
        title="Student Results",
        rows=[["Alice", 95, "A"], ["Bob", 82, "B"], ["Carol", 77, "B+"]]
    )
    print(html)

    print()
    text = gen.generate_text_report(["Python", "Java", "C++", "JavaScript"])
    print("Tech Stack:")
    print(text)

    # ── 4. Anonymous Behavior (Lambda + Inline Class) ──
    print()
    print("=" * 48)
    print(" 4. Anonymous Behavior")
    print("=" * 48)

    # Lambda for one-liners
    greet = lambda name: print(f"Hello, {name}!")
    greet("Abhishek")

    double = lambda x: x * 2
    print(f"Double of 7 = {double(7)}")

    print()
    # Inline class returned by a function (anonymous-class style)
    asc_sorter = get_sorter(reverse=False)
    desc_sorter = get_sorter(reverse=True)

    nums = [5, 2, 9, 1, 7, 3]
    asc_sorter.describe()
    print("Sorted:", asc_sorter.sort(nums))

    desc_sorter.describe()
    print("Sorted:", desc_sorter.sort(nums))

    # ── BONUS: Nested Config / Meta class ──
    print()
    print("=" * 48)
    print(" BONUS: Nested Meta Class — Product")
    print("=" * 48)
    p = Product("Mechanical Keyboard", 4_500, "Electronics")
    p.display()

    # Access Meta without creating a Product instance
    print()
    print("Meta Info:")
    print(f"  Ordering : {Product.Meta.ordering}")
    print(f"  Verbose  : {Product.Meta.verbose_name_plural}")
