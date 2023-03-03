
class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        if x1<x2 and y1>y2:
            self.x1 = x1
            self.y1 = y1
            self.x2 = x2
            self.y2 = y2
        else:
            print("Incorrect coordinates of the rectangles !")
    
    def width(self):
        return self.x2 - self.x1
    def height(self):
        return self.y1 - self.y2

    def area(self):
        pass

class Angka:
    def __init__(self,x1,x2):
        self.x1 = x1
        self.x2 = x2

    def sum(self):
        return self.x1 + self.x2

    def perkalian(self):
        return self.sum() * self.sum()

a1 = Angka(1,2)
print(a1.perkalian())
        
