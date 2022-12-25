from src.Figure import Figure
import math

class Circle(Figure):
    name = "Circle"
    area = None
    perimeter = None

    def __init__(self, r=None):
        self.r = r



    def area_circle(self): #Площадь вычисляемая
        self.area = self.r ** 2 * math.pi
        self.area = float('{:.4f}'.format(self.area))
        return self.area

    def perimeter_circle(self): #Периметр вычисляемое
        self.perimeter = 2 * math.pi * self.r
        return self.perimeter