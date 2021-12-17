
class Circle:

    def __init__(self, radius=1):
        self._radius = radius

    @property
    def r(self):
        return self._radius

    @r.setter
    def r(self, rad):
        if rad < 0:
            raise ValueError("radius can not be negative")
        self._radius = rad

    @property
    def diameter(self):
        return self._radius * 2

    @diameter.setter
    def diameter(self, d):
        self._radius = d / 2

    @property
    def area(self):
        return 3.14 * self._radius ** 2


c = Circle()
print(c.area)

c.r = 2

print(c.area)

c.diameter = 5

print(c.area)

c.r = -2
print(c.area)