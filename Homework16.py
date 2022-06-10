class Rectangular(object):
    created_rectangular = 0

    def __new__(cls, *args, **kwargs):
        self = super().__new__(cls)
        cls.created_rectangular += 1
        return self

    def __init__(self, *args):
        self.a, self.b, self.c, self.d = args

    def my_sorted_tuple(self):
        return sorted((self.a, self.b, self.c, self.d))

    def __eq__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f"Not supported type {type(other)}")

        return self.my_sorted_tuple() == other.my_sorted_tuple()

    def __gt__(self, other):
        if not isinstance(other, Rectangular):
            raise TypeError(f"Not supported type {type(other)}")

        my_first_rect = self.my_sorted_tuple()
        my_second_rect = other.my_sorted_tuple()
        is_greater = True
        for i in range(4):
            if my_first_rect[i] <= my_second_rect[i]:
                is_greater = False
                break
        return is_greater

    def alike(self, other):
        return self.my_sorted_tuple()[0] / other.my_sorted_tuple()[0] == self.my_sorted_tuple()[1] / \
               other.my_sorted_tuple()[1]

    def r_area(self):
        self.r_area = self.my_sorted_tuple()[0] * self.my_sorted_tuple()[2]
        return self.r_area

    def r_perimeter(self):
        self.r_perimeter = sum(self.my_sorted_tuple())
        return self.r_perimeter


rectangle_1 = Rectangular(8, 4, 4, 8)
rectangle_2 = Rectangular(8, 8, 4, 4)

print(f"Equal rectangles : {rectangle_1 == rectangle_2}")
print(f"First rectangle is greater : {rectangle_1 > rectangle_2}")
print(f"Area : {rectangle_1.r_area()}")
print(f"Perimeter : {rectangle_1.r_perimeter()}")
print(f"Rectangle count {Rectangular.created_rectangular}")
