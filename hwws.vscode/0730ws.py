class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
# p1 = Point(1, 3)       
# print(p1)     

class Rectagle:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def get_area(self):
        wide = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return wide * height

    
    def get_perimeter(self):
        wide = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return 2 * (wide + height)

    def is_square(self):
        wide = abs(self.p1.x - self.p2.x)
        height = abs(self.p1.y - self.p2.y)
        return wide == height
         

######(입력값)
p1 = Point(1, 3)
p2 = Point(3, 1)
r1 = Rectagle(p1, p2)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.is_square())

p3 = Point(3, 7)
p4 = Point(6, 4)
r2 = Rectagle(p3, p4)
print(r2.get_area())
print(r2.get_perimeter())
print(r2.is_square())



