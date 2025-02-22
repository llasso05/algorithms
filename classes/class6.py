"""Create a base class Animal with a speak() method that prints "Some sound".

Create subclasses Dog and Cat, where:
Dog.speak() prints "Bark"
Cat.speak() prints "Meow"""""


class Dog:
    def speak(self):
        print("Bark")
    
class Cat:
    def speak(self):
        print("Meow")
    
    
animals = [Dog(), Cat()]
for a in animals:
    a.speak()  # Should print "Bark" and "Meow"
