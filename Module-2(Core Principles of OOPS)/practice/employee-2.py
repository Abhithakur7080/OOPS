# Base class
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def displayDetails(self):
        print("Name :", self.name)
        print("Id :", self.id)


# Derived class - Manager
class Manager(Employee):
    def __init__(self, name, id, teamSize):
        super().__init__(name, id)
        self.teamSize = teamSize

    def displayDetails(self):
        super().displayDetails()
        print("Team Size :", self.teamSize)


# Derived class - Engineer
class Engineer(Employee):
    def __init__(self, name, id, specialization):
        super().__init__(name, id)
        self.specialization = specialization

    def displayDetails(self):
        super().displayDetails()
        print("Specialization :", self.specialization)


# Driver code
if __name__ == "__main__":
    manager = Manager("Jax", 101, 8)
    engineer = Engineer("William", 202, "Backend Developer")

    print("Manager Details")
    manager.displayDetails()

    print()

    print("Engineer Details")
    engineer.displayDetails()
