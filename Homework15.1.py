
# 2-Create Triangle class which will have 4 attributes (sides and the height), and methods for calculating the area,
# perimeter, validation of the triangle, and a method to compare the triangle with other one (Note: this method should check if the Triangles
# are alike or not).


class Triangle:

    def __init__(self, first_side, second_side, third_side, height, *args):
        self.first_side = first_side
        self.second_side = second_side
        self.third_side = third_side
        self.height = height
        self.area = None
        self.perimeter = None
        self.valid = False

    def tr_valid(self):
        if self.first_side + self.second_side >= self.third_side and self.second_side + self.third_side >= self.first_side and self.first_side + self.third_side >= self.second_side:
            self.valid = True
        return f"{self.valid}"

    def tr_perimeter(self):
        self.tr_valid()
        if self.valid is True:
            self.perimeter = self.first_side + self.second_side + self.third_side
            return f"The perimeter of the triangle is {self.perimeter} "
        else:
            return "No triangle"

    def tr_area(self):
        self.tr_valid()
        if self.valid is True:
            self.area = 1 / 2 * max(self.first_side, self.second_side, self.third_side) * self.height
            return f"The area of the triangle is {self.area} "
        else:
            return "No triangle"


my_tr = Triangle(5, 6, 7, 7, 30, 60)
print(my_tr.tr_valid())
print(my_tr.tr_area())
print(my_tr.tr_perimeter())
