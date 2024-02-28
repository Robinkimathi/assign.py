import math
class circle:
    def __init__(self,Radius):
        self.Radius=Radius

    def area(self):
        return self.Radius **2 * math.pi
    
    def parameter(self):
        print ("The Radius is ",self.Radius)

    def perimeter(self):
        return (self.Radius*2) * math.pi

circle = circle (7)
print(circle.area())
print(circle.parameter)
print (circle.perimeter())
circle.parameter()
