from abc import ABC, abstractmethod

# ──────────────────────────────────────────────
# INTERFACES in Python
#
# Python has NO built-in `interface` keyword (unlike Java/C#).
# We SIMULATE interfaces using Abstract Base Classes (ABC)
# where ALL methods are abstract (no concrete logic).
#
# Interface Rules (Python convention):
#   • All methods are @abstractmethod (no method body)
#   • No instance variables inside the interface
#   • A class can implement MULTIPLE interfaces
#   • Interfaces define a CONTRACT — what must be done, not how
# ──────────────────────────────────────────────


# ──────────────────────────────────────────────
# 1. Basic Interface
# ──────────────────────────────────────────────

class Printable(ABC):
    """Interface: anything that can be printed."""

    @abstractmethod
    def print_details(self):
        pass


class Invoice(Printable):
    def __init__(self, invoice_id, amount):
        self.invoice_id = invoice_id
        self.amount = amount

    def print_details(self):
        print(f"Invoice #{self.invoice_id} | Amount: Rs.{self.amount:,}")


class Receipt(Printable):
    def __init__(self, receipt_id, item):
        self.receipt_id = receipt_id
        self.item = item

    def print_details(self):
        print(f"Receipt #{self.receipt_id} | Item: {self.item}")


# ──────────────────────────────────────────────
# 2. Multiple Interfaces on One Class
#    (Python supports multiple inheritance)
# ──────────────────────────────────────────────

class Flyable(ABC):
    """Interface: anything that can fly."""

    @abstractmethod
    def fly(self):
        pass

    @abstractmethod
    def land(self):
        pass


class Swimmable(ABC):
    """Interface: anything that can swim."""

    @abstractmethod
    def swim(self):
        pass


class Drivable(ABC):
    """Interface: anything that can be driven."""

    @abstractmethod
    def drive(self):
        pass


class Duck(Flyable, Swimmable):
    """Duck implements BOTH Flyable and Swimmable."""

    def fly(self):
        print("Duck flaps its wings and flies low.")

    def land(self):
        print("Duck glides down and lands on water.")

    def swim(self):
        print("Duck paddles across the pond.")


class AmphibiousCar(Drivable, Swimmable):
    """Amphibious car can drive on roads AND swim in water."""

    def drive(self):
        print("Amphibious car drives on the highway.")

    def swim(self):
        print("Amphibious car deploys floats and glides on water.")


# ──────────────────────────────────────────────
# 3. Interface Inheritance (Extending Interfaces)
#    One interface can extend another interface
# ──────────────────────────────────────────────

class Serializable(ABC):
    """Base interface: object can be serialized."""

    @abstractmethod
    def serialize(self):
        pass


class Persistable(Serializable):
    """
    Extended interface: adds save/load on top of Serializable.
    Any class implementing Persistable MUST implement all three methods.
    """

    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def load(self):
        pass


class UserProfile(Persistable):
    """Implements the full Persistable interface (3 methods)."""

    def __init__(self, username):
        self.username = username

    def serialize(self):
        data = f'{{"username": "{self.username}"}}'
        print(f"Serialized → {data}")
        return data

    def save(self):
        print(f"Saving profile '{self.username}' to database...")

    def load(self):
        print(f"Loading profile '{self.username}' from database...")


# ──────────────────────────────────────────────
# 4. Interface as a Contract + Polymorphism
#    Different classes, same interface → swap freely
# ──────────────────────────────────────────────

class PaymentGateway(ABC):
    """
    Interface / Contract for payment gateways.
    Any payment method MUST implement pay() and refund().
    """

    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class UPIPayment(PaymentGateway):
    def pay(self, amount):
        print(f"[UPI]     Paid Rs.{amount} via UPI.")

    def refund(self, amount):
        print(f"[UPI]     Refunded Rs.{amount} to UPI wallet.")


class CardPayment(PaymentGateway):
    def pay(self, amount):
        print(f"[Card]    Paid Rs.{amount} via Credit/Debit Card.")

    def refund(self, amount):
        print(f"[Card]    Refunded Rs.{amount} to card.")


class NetBankingPayment(PaymentGateway):
    def pay(self, amount):
        print(f"[NetBank] Paid Rs.{amount} via Net Banking.")

    def refund(self, amount):
        print(f"[NetBank] Refunded Rs.{amount} to bank account.")


def process_payment(gateway: PaymentGateway, amount: int):
    """
    Polymorphic function — works with ANY PaymentGateway.
    Doesn't care WHICH gateway, only that it follows the contract.
    """
    gateway.pay(amount)


# ──────────────────────────────────────────────
# 5. Default Method via Mixin
#    Python interfaces can provide default behaviour
#    through Mixin classes (not ABC)
# ──────────────────────────────────────────────

class LogMixin:
    """
    Mixin (not ABC) — provides a default log() method.
    Classes can inherit this alongside an interface.
    """

    def log(self, message):
        print(f"[LOG | {type(self).__name__}] {message}")


class Sensor(ABC):
    """Interface: any sensor must be able to read data."""

    @abstractmethod
    def read(self):
        pass


class TemperatureSensor(Sensor, LogMixin):
    """Implements Sensor interface + gets log() from LogMixin."""

    def read(self):
        temp = 36.6
        self.log(f"Temperature reading: {temp}°C")
        return temp


class HumiditySensor(Sensor, LogMixin):
    def read(self):
        humidity = 78
        self.log(f"Humidity reading: {humidity}%")
        return humidity


# ──────────────────────────────────────────────
# MAIN — Run all examples
# ──────────────────────────────────────────────

if __name__ == "__main__":

    # ── 1. Basic Interface ──
    print("=" * 45)
    print(" 1. Basic Interface — Printable")
    print("=" * 45)
    docs = [Invoice(1001, 25_000), Receipt(501, "Laptop")]
    for doc in docs:
        doc.print_details()

    # ── 2. Multiple Interfaces ──
    print()
    print("=" * 45)
    print(" 2. Multiple Interfaces")
    print("=" * 45)
    duck = Duck()
    duck.fly()
    duck.swim()
    duck.land()
    print()
    amp_car = AmphibiousCar()
    amp_car.drive()
    amp_car.swim()

    # ── 3. Interface Inheritance ──
    print()
    print("=" * 45)
    print(" 3. Interface Inheritance — UserProfile")
    print("=" * 45)
    user = UserProfile("abhishek_07")
    user.serialize()
    user.save()
    user.load()

    # ── 4. Interface as Contract + Polymorphism ──
    print()
    print("=" * 45)
    print(" 4. Interface Contract — Payment Gateways")
    print("=" * 45)
    gateways = [UPIPayment(), CardPayment(), NetBankingPayment()]
    for gateway in gateways:
        process_payment(gateway, 5_000)

    print()
    # Refund using a specific gateway
    upi = UPIPayment()
    upi.refund(1_500)

    # ── 5. Default Method via Mixin ──
    print()
    print("=" * 45)
    print(" 5. Default Method (Mixin) — Sensors")
    print("=" * 45)
    temp_sensor = TemperatureSensor()
    humidity_sensor = HumiditySensor()
    temp_sensor.read()
    humidity_sensor.read()

    # Checking interface compliance with isinstance
    print()
    print("isinstance checks (interface contract verification):")
    print(f"  duck isinstance Flyable   → {isinstance(duck, Flyable)}")
    print(f"  duck isinstance Swimmable → {isinstance(duck, Swimmable)}")
    print(f"  amp_car isinstance Drivable → {isinstance(amp_car, Drivable)}")
    print(f"  upi isinstance PaymentGateway → {isinstance(upi, PaymentGateway)}")
