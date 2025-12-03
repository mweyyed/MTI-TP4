from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side
class Bird:
    pass

class Flyable:
    def fly(self):
        print("I can fly!")

class Eagle(Bird, Flyable):
    pass

class Penguin(Bird):
    def swim(self):
        print("I swim instead of flying.")
