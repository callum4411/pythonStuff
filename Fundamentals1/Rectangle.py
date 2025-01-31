class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return "Area: " + str(self.area()) + "\nPerimeter: " + str(self.perimeter())

class ShapeList:
    def __init__(self):
        self.shapes = []
        self.index = 0

    def add(self, shape):
        if   len(self.shapes) < 10:
            self.shapes.append(shape)
            print("Shape added successfully")
            self.index += 1
        else:
            print("Shape already added")

    def print_shapes(self):
        for shape in self.shapes:
            print(shape)



class TestRectangle:
    @staticmethod
    def main():
        sl = ShapeList()
        rect1 = Rectangle(10,20)
        sl.add(rect1)
        sl.add(Rectangle(15,25))

        sl.print_shapes()


TestRectangle.main()