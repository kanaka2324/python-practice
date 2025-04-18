from abc import ABC, abstractmethod
class Shape(ABC):
   def area(self):
      pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
         return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
       return 3.14159 * self.radius * self.radius

# Usage:
rectangle = Rectangle(5, 10)
circle = Circle(3)

print("Area of rectangle:", rectangle.area())
print("Area of circle:", circle.area())