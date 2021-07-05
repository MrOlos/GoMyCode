class Rectangle:

    def __init__(self, width, length):
        self.width=width
        self.length=length
    def Perimeter(self):
        perimeter=2*(self.width+self.length)
        return perimeter
    def Area(self):
        area=self.width*self.length
        return area

my_rectangle=Rectangle(4, 3)

print("Perimeter:",my_rectangle.Perimeter())
print("Area:", my_rectangle.Area())
