class Animal:
    alive:True

    def eat(self):
        return "This animal is eating."
    def sleep(self):
        return "This animal is sleeping."

class Rabbit(Animal):
    def hop():
        return "This rabbit is hopping."
class Fish(Animal):
    def swim():
        return "This fish is swimming."
class Eagle(Animal):
    def fly(self):
        return "This eagle is flying."

rabbit=Rabbit()
fish=Fish()
eagle=Eagle()

print(rabbit.eat())
print(fish.sleep())
print(eagle.fly())