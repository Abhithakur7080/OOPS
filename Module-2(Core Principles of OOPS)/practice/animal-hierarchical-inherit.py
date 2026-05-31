class Animal:
    def eat(self):
        print("This animal eats food.")

class Dog(Animal):
    def bark(self):
        print("This animal barks.")

class Cat(Animal):
    def meow(self):
        print("This animal meows.")

def main():
    dog = Dog()
    dog.eat()
    dog.bark()
    cat = Cat()
    cat.eat()
    cat.meow()

if __name__ == "__main__":
    main()