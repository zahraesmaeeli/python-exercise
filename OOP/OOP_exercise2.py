import math
from abc import ABC,abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):

    def __init__(self,tool,arz):
        self.tool=tool
        self.arz=arz
    def area(self):
        return self.tool*self.arz


class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius

class Triangle(Shape):
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return 0.5*self.base*self.height

############################################
Circle=Circle(2)
print(Circle.area())