#16.1
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Rectangle):
            return self.area() <= other.area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Rectangle):
            return self.area() >= other.area()
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Rectangle):
            new_area = self.area() + other.area()
            new_width = self.width + other.width
            new_height = new_area / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __mul__(self, n):
        if isinstance(n, (int, float)):
            new_area = self.area() * n
            new_width = self.width * n
            new_height = new_area / new_width
            return Rectangle(new_width, new_height)
        return NotImplemented

    def __rmul__(self, n):
        return self.__mul__(n)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height}, area={self.area()})"

    def __repr__(self):
        return self.__str__()
#16.2
import math

class Fraction:
    def __init__(self, a, b):
        if b == 0:
            raise ValueError("Знаменник не може дорівнювати нулю")
        self.a = a
        self.b = b
        self._normalize()

    def _normalize(self):
        gcd = math.gcd(self.a, self.b)
        self.a //= gcd
        self.b //= gcd
        if self.b < 0:
            self.a = -self.a
            self.b = -self.b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.a, self.b * other.b)
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.b + other.a * self.b, self.b * other.b)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Fraction):
            return Fraction(self.a * other.b - other.a * self.b, self.b * other.b)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a == other.a and self.b == other.b
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b >= other.a * self.b
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b <= other.a * self.b
        return NotImplemented

    def __str__(self):
        return f"{self.a}/{self.b}" if self.b != 1 else f"{self.a}"

    def __repr__(self):
        return f"Fraction({self.a}, {self.b})"