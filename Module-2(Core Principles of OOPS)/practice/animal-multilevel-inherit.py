class Animal:
    def eat(self):
        print("This animal eats food.")

class Mammal(Animal):
    def feed(self):
        print("This animal feeds its young.")

class Dog(Mammal):
    def bark(self):
        print("This animal barks.")

class Puppy(Dog):
    def play(self):
        print("This puppy plays.")

def main():
    puppy = Puppy()
    puppy.eat()
    puppy.feed()
    puppy.bark()
    puppy.play()

if __name__ == "__main__":
    main()