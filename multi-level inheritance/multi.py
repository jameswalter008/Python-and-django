class Organism:
    alive=True

class Animal(Organism):
    def eat(self):
        return "This animal is eating."
class Dog(Animal):
    def bark(self):
        return "This dog is barking."

dog=Dog()
print(dog.bark())