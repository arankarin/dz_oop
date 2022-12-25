from src.Figure import Figure

class Rectangle(Figure):
    name = "Rectangle"
    area = None
    perimeter = None

    def __init__(self, a=None, b=None):
        self.a = a
        self.b = b

    def area_rectangle(self): #Площадь вычисляемая
        self.area = self.a * self.b
        return self.area

    def perimeter_rectangle(self): #Периметр вычисляемое
        self.perimeter = (self.a + self.b)*2
        return self.perimeter