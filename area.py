import math
class rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
          
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return (self.length*2) + (self.width*2)

rectangle = rectangle (20,10)
print (rectangle.area())
print (rectangle.perimeter())