class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("This animal barks.")

def main():
    dog = Dog()
    dog.eat()
    dog.bark()

if __name__ == "__main__":
    main()