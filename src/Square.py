from src.Figure import Figure


class Square(Figure):
    name = "Square"
    area = None
    perimeter = None

    def __init__(self, a=None):
        self.a = a

    def area_squara(self):  # Площадь вычисляемая
        self.area = self.a ** 2
        return self.area

    def perimeter_rectangle(self):  # Периметр вычисляемое
        self.perimeter = self.a * 4
        return self.perimeter
