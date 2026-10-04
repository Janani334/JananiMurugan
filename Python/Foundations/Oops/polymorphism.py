# Polymorphism means -> the same method can behave differently in different classes.
class Animal:
    def sound(self):
        return "Any sound"

class Bird:
    def sound(self):
        return "Chirp"

class Dog:
    def sound(self):
        return "Bark"

class Cat:
    def sound(self):
        return "Meow"

# animal=Animal()
# dog=Dog()
# cat=Cat()
# bird=Bird()

# animal.sound()
# print(animal.sound())
# cat.sound()
# print(cat.sound())
# bird.sound()
# print(bird.sound())
# dog.sound()
# print(dog.sound())

# or in loop 
animals = [Animal(),Dog(),Bird(),Cat()]
for a in animals:
    print(a.sound())

