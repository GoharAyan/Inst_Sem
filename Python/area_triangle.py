class Triangle:
    def __init__(self):
        self.base = ""
        self.height = ""

    def get_parameter(self):
        self.base = int(input("Enter base: "))
        self.height = int(input("Enter height: "))

    def triangle_area(self):
        self.area = (self.base * self.height) / 2 
        print("Area of a triangle: ", self.area)

triangle = Triangle()
triangle.get_parameter()
triangle.triangle_area()
