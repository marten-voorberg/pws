import math

class Vector3:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
         return 'Vector3({}, {}, {})'.format(self.x, self.y, self.z)

    def __add__(self, other):
        return Vector3(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
        )

    def __sub__(self, other):
        return Vector3(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )

    def __mul__(self, other):
        return Vector3(
            self.x * other,
            self.y * other,
            self.z * other
        )

    def __truediv__(self, other):
        return Vector3(
            self.x / other,
            self.y / other,
            self.z / other
        )

    # We cannot use the __len__ method because that method always has to return an integer, 
    # whilst the length of a vector can be a float too
    def get_length(self):
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)