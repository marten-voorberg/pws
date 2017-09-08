import math

class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
         return 'Vector2({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2(
            self.x + other.x,
            self.y + other.y
        )

    def __sub__(self, other):
        return Vector2(
            self.x - other.x,
            self.y - other.y
        )

    def __mul__(self, other):
        return Vector2(
            self.x * other,
            self.y * other
        )

    def __truediv__(self, other):
        return Vector2(
            self.x / other,
            self.y / other
        )

    # We cannot use the __len__ method because that method always has to return an integer, 
    # whilst the length of a vector can be a float too
    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    # The unit vector of a vector is a vector with the same direction, but with a length of 1
    def get_unitvector(self):
        return self / self.get_length()

    def calc_distance_to(self, other):
        vector_between = other - self
        return vector_between.get_length()