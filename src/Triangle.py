from src.Figure import Figure
import math


class Triangle(Figure):
    name = "Triangle"
    area = None
    perimeter = None

    def __init__(self, a=None, b=None, c=None):
        self.a = a
        self.b = b
        self.c = c
        if not self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a \
                and self.a > 0 and self.b > 0 and self.c > 0:
            raise ValueError

    def area_triangle(self):  # Площадь вычисляемая
        p2 = (self.a + self.b + self.c) / 2
        self.area = math.sqrt(p2 * (p2 - self.a) * (p2 - self.b) * (p2 - self.c))
        return self.area

    def perimeter_triangle(self):  # Периметр вычисляемое
        self.perimeter = self.a + self.b + self.c
        return self.perimeter
