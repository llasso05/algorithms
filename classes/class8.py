"""Create an abstract class Shape with an abstract method area().

Create subclasses Circle and Rectangle that implement area()."""

from abc import ABC, abstractmethod

class Shape:
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self):
        return print("circle")
        
class Rectangle(Shape):
    def area(self):
        return print("rectangle")
    
c = Circle(7)
r = Rectangle(5, 10)

print(c.area())  # Expected: 153.94 (πr²)
print(r.area())  # Expected: 50
