from abc import ABC, abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def display_message(self):
        return "This is my abstract example"

class Rectangle(shape):
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def area(self):
        return self.width * self.length
    def perimeter(self):
        return 2 * (self.width + self.length)

rectangle1 = Rectangle(20,24)
print(rectangle1.area())
print(rectangle1.perimeter())
print(rectangle1.display_message())