import math


class Vector3:
    """ A three dimention vector with three elements (x, y, z) """

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, b):
        return Vector3(self.x + b.x, self.y + b.y, self.z + b.z)

    def __sub__(self, b):
        return Vector3(self.x - b.x, self.y - b.y, self.z - b.z)

    def __mul__(self, s):
        return Vector3(self.x * s, self.y * s, self.z * s)

    def __truediv__(self, s):
        return Vector3(self.x / s, self.y / s, self.z / s)

    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def normalize(self):
        m = self.magnitude()
        return Vector3(self.x/m, self.y/m, self.z/m) if m != 0 else Vector3()

    def dot(self, b):
        return self.x*b.x + self.y*b.y + self.z*b.z

    def cross(self, b):
        return Vector3(self.y*b.z - self.z-b.y,
                       self.z*b.x - self.x*b.z,
                       self.x*b.y - self.y*b.x)
